import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List
from app.database import Base

if TYPE_CHECKING: #type checking needed to pass flake test
    from app.models.receipt import Receipt

class Owner(Base):
    __tablename__ = 'owner'

    id:Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type:Mapped[str]
    name:Mapped[str]
    receipts:Mapped[List['Receipt']] = relationship(back_populates='owner')



