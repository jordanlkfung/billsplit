from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from app.models.receipt import Receipt
from app.models.owner import Owner
from app.models.association_tables import users_receipt_association_table, user_groups_table, receipt_item_association_table
from app.schemas.receipt import ReceiptItem, GeneratedReceipt
from typing import List
class ReceiptService:
    async def checkReceiptOwner(self, receipt_id, user_id, db:AsyncSession):
        stmt = select(Receipt.owner).where(Receipt.id == receipt_id)
        try:
            res = await db.execute(stmt)
            owner_id = res.scalar_one()

            stmt = select(Owner.type).where(Owner.id == owner_id)
            res = await db.execute(stmt)
            owner_type = res.scalar_one()


            if owner_type == 'user':

                if owner_id != user_id:
                    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
            
            else:
                stmt = select(user_groups_table.user_id).where((user_groups_table.group_id == owner_id) & (user_groups_table.user_id == user_id))

                res = await db.execute(stmt)

                data = res.scalar_one_or_none()

                if not data:
                    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
                
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    async def getReceiptById(self, id, db:AsyncSession):
        stmt = select(Receipt).where(Receipt.id == id)
        try:
            res = await db.execute(stmt)

            data = res.one_or_none()

            return data
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    async def getOpenReceipts(self, user_id, db:AsyncSession):
        stmt = select(users_receipt_association_table).where((users_receipt_association_table.user_id == user_id) & (users_receipt_association_table.paid == False))
        try:
            res = await db.execute(stmt)

            data = res.mappings()

            return data
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    

    async def addReceiptItem(self, receipt_id, items:List, db:AsyncSession):
        for i, item in enumerate(items):
            item_instance = receipt_item_association_table(index = i, receipt_id = receipt_id, item_name = item.name, amount = item.amount)
            db.add(item_instance)
        
        await db.commit()


    
    async def generateReceipt(self, receipt_id, db:AsyncSession):
        stmt = select(Receipt.amount).where(Receipt.id == receipt_id)
        try:
            res = await db.execute(stmt)

            total_amount = res.scalar_one()

            stmt = select(receipt_item_association_table.item_name, receipt_item_association_table.amount).where(receipt_item_association_table.receipt_id == receipt_id)

            res = await db.execute(stmt)

            items = res.all()

            return GeneratedReceipt(total_amount=total_amount, itmes=[ReceiptItem(name=name, amount=amount) for name, amount in items])

        except Exception:
            raise
        

