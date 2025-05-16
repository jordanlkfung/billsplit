import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey
from typing import TYPE_CHECKING, List
from app.database import Base
from app.models.owner import Owner

if TYPE_CHECKING: #type checking needed to pass flake test
    from app.models.group import Group

user_groups_table = Table(
    "user_groups_table", 
    Base.metadata, 
    Column('user_id', ForeignKey('user.id')), 
    Column('group_id', ForeignKey('group.id'))

    )
class User(Owner):
    __tablename__ = 'user'
    id:Mapped[uuid.UUID] = mapped_column(ForeignKey('owner.id'), default=uuid.uuid4)
    email:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str]
    groups:Mapped[List['Group']] = relationship(secondary=user_groups_table)

