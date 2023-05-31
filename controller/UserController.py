from entity.UserEntity import User
from fastapi_utils.inferring_router import InferringRouter
from service import UserService as userService

# 生成路由 这个路由可以匹配返回的model不用手动申明
userController = InferringRouter()


@userController.post('/login')
async def userLogin(user: User):
    return userService.login(user)


@userController.get('/getUserById/v1/{userId}')
async def getUserById(userId: str):
    return 'test'
