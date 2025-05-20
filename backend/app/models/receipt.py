import uuid
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import Table, Column, ForeignKey, String, Float, Boolean
from typing import TYPE_CHECKING, List
from app.database import Base

if TYPE_CHECKING: #type checking needed to pass flake test
    from app.models.owner import Owner
    from app.models.association_tables import receipt_item_association_table


# users_receipt_association_table = Table(
#     'user_receipt_association_table',
#     Base.metadata,
#     Column('user_id', ForeignKey('user.id'), nullable=True), #user the owes the money
#     Column('user_name', String, nullable=True), #this is for people that don't have an account
#     Column('owed_id', ForeignKey('user.id')), #user who is owed the money
#     Column('owed_name', String, nullable=False),
#     Column('receipt_id', ForeignKey('receipt.id'), nullable=True),
#     Column('item_name', String, nullable=True),
#     Column('amount', Float, nullable=True),
#     Column('paid', Boolean, default=False),
#     Column('payment_method', String, nullable=True) #this is for ones that have been paid already
# )

class Receipt(Base):
    __tablename__ = 'receipt'

    id:Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    upload_date:Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    transaction_date:Mapped[datetime] = mapped_column(nullable=True)
    institution:Mapped[datetime] = mapped_column(nullable=True)
    amount:Mapped[float] = mapped_column(nullable=True)
    owner:Mapped['Owner'] = relationship(back_populates='receipts')
    items:Mapped[List['receipt_item_association_table']] = relationship(back_populates='receipt')
