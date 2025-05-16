import uuid
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, String, Float, Boolean
from typing import TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING: #type checking needed to pass flake test
    from app.models.owner import Owner


users_receipt_association_table = Table(
    'user_receipt_association_table',
    Base.metadata,
    Column('user_id', ForeignKey('user.id')),
    Column('receipt_id', ForeignKey('receipt.id')),
    Column('item_name', String, nullable=True),
    Column('amount', Float),
    Column('paid', Boolean, default=False)
)

class Receipt(Base):
    __tablename__ = 'receipt'

    id:Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    upload_date:Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    transaction_date:Mapped[datetime] = mapped_column(nullable=True)
    institution:Mapped[datetime] = mapped_column(nullable=True)
    amount:Mapped[float] = mapped_column(nullable=True)
    owner:Mapped['Owner'] = relationship(back_populates='receipts')