import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List
from app.database import Base

if TYPE_CHECKING: #type checking needed to pass flake test
    from app.models.user import user_groups_table, User

class Group(Base):
    __tablename__ = 'group'
    
    id:Mapped[uuid.UUID] = mapped_column(ForeignKey('owner.id'), default=uuid.uuid4)
    name:Mapped[str]
    users:Mapped[List['User']] = relationship(secondary=user_groups_table)
    