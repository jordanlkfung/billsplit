import uuid
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.receipt import Receipt

class users_receipt_association_table(Base):
    __tablename__ = 'user_receipt_association_table'

    user_id:Mapped[uuid.UUID] = mapped_column(ForeignKey('user.id'), nullable=True)
    user_name:Mapped[str] = mapped_column(nullable=True)
    user_to_pay:Mapped[uuid.UUID] = mapped_column(ForeignKey('user.id'), nullable=True)
    user_to_pay_name:Mapped[str] = mapped_column(nullable=True)
    receipt_id:Mapped[uuid.UUID] = mapped_column(ForeignKey('receipt.id'))
    paid:Mapped[bool] = mapped_column(default=False)
    payment_method:Mapped[str] = mapped_column(nullable=True)
    item_index:Mapped[int]

class user_groups_table(Base):
    __tablename__ = "user_groups_table" 
    user_id:Mapped[uuid.UUID] = mapped_column(ForeignKey('user.id')) 
    group_id:Mapped[uuid.UUID] = mapped_column(ForeignKey('group.id'))
    user:Mapped['User'] = relationship(back_populates='user')

class receipt_item_association_table(Base):
    __tablename__ = 'receipt_item_association'

    index:Mapped[int]
    receipt_id:Mapped[uuid.UUID] = mapped_column(ForeignKey('receipt.id'))
    item_name:Mapped[str]
    amount:Mapped[float]
    receipt:Mapped['Receipt'] = relationship(back_populates='items')
