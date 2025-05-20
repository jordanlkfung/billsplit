from fastapi import APIRouter, Depends, File, UploadFile
from typing import Annotated

receipt_router = APIRouter()

@receipt_router.get('/{id}')
async def getReceipt(id):
    pass

@receipt_router.get('/{receipt_id}/{user}')
async def getAmountOwed(receipt_id, user):
    '''
    returns amount the user owes on the receipt, will also return who is owed the money
    '''
    pass

@receipt_router.post('/upload')
async def uploadReceipt(file:Annotated[UploadFile, File()]):
    '''
    call to ocr with file
    '''
    pass

@receipt_router.put('/pay')
async def pay():
    pass

@receipt_router.put('/payment_received')
async def markReceived():
    pass

@receipt_router.post('/items')
async def addItem():
    pass

@receipt_router.get('/items')
async def getItems():
    pass

@receipt_router.delete('/items')
async def deleteItem():
    pass

@receipt_router.put('/items')
async def updateItem():
    pass

@receipt_router.get('/open')
async def openReceipts(offset:int = 0, limit:int = 10):
    '''
    retrieve all unpaid receipts

    returns amount, name of item purchased, receipt id
    '''
    pass

