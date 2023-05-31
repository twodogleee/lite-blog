from dao import UserDao as userDao
from entity.UserEntity import DbUser, User, UpdateUser
from service import BasicService as basicService


def login(user: User):
    dbUser = DbUser(**user.dict())
    dbUser = userDao.getUserByUsernameAndPassword(dbUser)
    if dbUser:
        dbUser.password = None
        return basicService.suc(dbUser)
    return basicService.fail('用户名或密码错误')


def updatePassword(user: UpdateUser):
    updateUser = User(**user.dict(), exclude={'oldPassword'})
    dbUser = DbUser(**updateUser.dict())
    dbUser.password = user.oldPassword
    # 以现有用户及密码查询是否存在
    dbUser = userDao.getUserByUsernameAndPassword(dbUser)
    if dbUser is None:
        return basicService.fail('密码错误')
    # 密码改为需要修改的密码
    dbUser.password = user.password
    return basicService.toResult(userDao.updatePasswordByUsername(dbUser))
