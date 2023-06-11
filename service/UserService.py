from dao import UserDao as userDao
from entity.UserEntity import DbUser, User, UpdateUser
from service import BasicService as basicService
from hashlib import md5
from entity.TokenEntity import DbToken
from dao import TokenDao as tokenDao
import time


# 后管登录
def login(user: User):
    user.password = md5(user.password.encode()).hexdigest().upper()
    db_user = DbUser(**user.dict())
    db_user = userDao.getUserByUsernameAndPassword(db_user)
    # 用户不为空
    if db_user:
        db_user.password = None
        # 获取当前用户的token
        db_token = tokenDao.get_token_by_user_id(db_user.id)
        # 当前系统时间戳
        timestamp = int(time.time())
        # token字符串
        token_str = md5(('token' + db_user.id + str(timestamp)).encode()).hexdigest().upper()
        # token过期时间
        ex_time = timestamp + 30
        # token不为空
        if db_token:
            db_token.token_str = token_str
            db_token.expires_time = ex_time
            # 修改token
            token_flag = tokenDao.update_token(db_token)
        else:
            db_token = DbToken(**{'user_id': db_user.id, 'token_str': token_str, 'expires_time': ex_time})
            # 写入token
            token_flag = tokenDao.save_token(db_token)
        # token更新成功 则返回token
        if token_flag:
            return basicService.success(token_str)
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
    return basicService.to_result(userDao.updatePasswordByUsername(dbUser))
