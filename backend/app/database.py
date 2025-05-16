import contextlib
from typing import AsyncIterator
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncConnection, AsyncSession


class Base(DeclarativeBase):
    pass

class DatabaseSessionManager:
    def __init__(self):
        self._engine:AsyncEngine | None = None
        self._sessionmaker:async_sessionmaker | None = None

    def init(self, host:str):
        self._engine = create_async_engine(host)
        self._sessionmaker = async_sessionmaker(bind=self._engine, expire_on_commit=False, autocommit=False)
        
    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager not initalized")
        async with self._engine.begin() as conn:
            try:
                yield conn
            except Exception:
                await conn.rollback()
                raise
    
    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager not initalized")
        session:AsyncSession = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager not initalized")
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None
    
    async def create_all(self, conn:AsyncConnection):
        await conn.run_sync(Base.metadata.create_all)
    
    async def drop_all(self, conn:AsyncConnection):
        await conn.run_sync(Base.metadata.drop_all)
        
sessionmanager = DatabaseSessionManager()

async def get_db():
    async with sessionmanager.session() as db: 
            yield db
