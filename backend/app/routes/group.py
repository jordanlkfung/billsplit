from fastapi import Depends, APIRouter


group_router = APIRouter()

@group_router.post('/create')
async def createGroup():
    pass

@group_router.get("/")
async def getGroup():
    pass

@group_router.post("/add")
async def addUserToGroup():
    pass

