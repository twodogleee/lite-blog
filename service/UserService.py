from dao import UserDao as userDao
from entity.UserEntity import DbUser, User, UpdateUser
from service import BasicService as basicService
from hashlib import md5


# 后管登录
def login(user: User):
    user.password = md5(user.password.encode()).hexdigest().upper()
    dbUser = DbUser(**user.dict())
    dbUser = userDao.getUserByUsernameAndPassword(dbUser)
    if dbUser:
        dbUser.password = None
        return basicService.suc(dbUser)
    return basicService.fail('用户名或密码错误')


# 修改初始密码
def updatePassword(user: UpdateUser):
    updateUser = User(**user.dict(), exclude={'oldPassword'})
    dbUser = DbUser(**updateUser.dict())
    dbUser.password = md5(user.oldPassword.encode()).hexdigest().upper()
    # 以现有用户及密码查询是否存在
    dbUser = userDao.getUserByUsernameAndPassword(dbUser)
    if dbUser is None:
        return basicService.fail('原密码错误')
    # 密码改为需要修改的密码
    dbUser.password = md5(user.password.encode()).hexdigest().upper()
    return basicService.toResult(userDao.updatePasswordByUsername(dbUser))
