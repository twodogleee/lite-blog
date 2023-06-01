from entity.UserEntity import User, UpdateUser
from fastapi_utils.inferring_router import InferringRouter
from service import UserService as userService

# 生成路由 这个路由可以匹配返回的model不用手动申明
userController = InferringRouter()


# 后管登录
@userController.post('/login')
async def userLogin(user: User):
    return userService.login(user)


# 修改初始密码
@userController.post('/updatePassword')
async def updatePassword(user: UpdateUser):
    return userService.updatePassword(user)


@userController.get('/getUserById/v1/{userId}')
async def getUserById(userId: str):
    return 'test'
