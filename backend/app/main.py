from contextlib import asynccontextmanager
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.database import sessionmanager
from typing import AsyncGenerator

load_dotenv()


def init_app(init_db: bool = True):

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        if init_db:
            url = os.getenv("URL")
            
            if not url:
                raise RuntimeError("Missing URL environment variable")
            
            sessionmanager.init(url)
            print("Server is starting")

        yield

        if init_db and sessionmanager._engine is not None:
            await sessionmanager.close()
            print("Server is shutting down")

    server = FastAPI(title="FastAPI server", lifespan=lifespan)

    
    return server

app = init_app()
