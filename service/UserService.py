from dao import UserDao as userDao
from entity.UserEntity import DbUser, User
from service import BasicService as basicService


def login(user: User):
    dbUser = DbUser(**user.dict())
    dbUser = userDao.getUserByUsernameAndPassword(dbUser)
    if dbUser:
        return basicService.suc(dbUser)
    return basicService.fail('用户不存在')
