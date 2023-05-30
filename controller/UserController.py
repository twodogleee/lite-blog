from fastapi import APIRouter

userController = APIRouter()


@userController.get('/login')
async def userLogin():
    return {'msg': '登录成功'}
