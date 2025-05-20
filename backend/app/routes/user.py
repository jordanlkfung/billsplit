import jwt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


user_router = APIRouter()

@user_router.post('/login')
async def login():
    '''
    Login route
    Args:
        email
        password
    
    Returns
        On success
            status code 200
            JWT token in Authorization header
    '''
    pass

@user_router.post('/signup')
async def signup():
    '''
    Sign Up Route
    Args:
        email
        password
    '''
    pass

@user_router.put('/update')
async def update():
    '''
    update route
    allows users to update fields in their profile
    ex.
        password
        venmo account/payment account
        name
    '''
    pass

@user_router.get('/friends')
async def getFriends():
    '''
    reterieves all the users friends
    '''
    pass

@user_router.post('/addFriend')
async def addFriend():
    '''
    adds friend
    takes in user id of friend
    returns 204 if successful
    '''
    pass

@user_router.get('/profile')
async def getProfile():
    '''
    returns the users profile
    '''
    pass


@user_router.get('/transactions/')
async def getTransactions(offset:int = 0, limit:int = 10):
    '''
    retrieves all transactions
        transactions are completed payments
    '''
    pass



