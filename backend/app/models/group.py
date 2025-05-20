import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING, List
from app.database import Base

if TYPE_CHECKING: #type checking needed to pass flake test
    from app.models.association_tables import user_groups_table
    from app.models.user import User

class Group(Base):
    __tablename__ = 'group'
    
    id:Mapped[uuid.UUID] = mapped_column(ForeignKey('owner.id'), default=uuid.uuid4)
    name:Mapped[str]
    users:Mapped[List['User']] = relationship(secondary='user_groups_table', back_populates='groups')
    users_associations:Mapped[List['user_groups_table']] = relationship(back_populates='group')
    