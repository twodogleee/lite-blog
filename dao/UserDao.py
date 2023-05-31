from entity.UserEntity import DbUser
from sqlalchemy.orm import Session
from dao import getDb


# 根据用户名&密码 查询用户信息
def getUserByUsernameAndPassword(user: DbUser):
    return getDb().query(DbUser).filter(DbUser.username == user.username and DbUser.password == user.password).first()


# 根据userId查询用户信息
def getUserById(userId: str):
    return getDb().query(DbUser).filter(DbUser.id == userId).first()


# 根据用户名查询用户
def getUserByUserName(userName: str):
    return getDb().query(DbUser).filter(DbUser.username == userName).first()


# 创建用户信息
def createUser(user: DbUser):
    db = getDb()
    db.add(user)
    db.refresh(user)
    db.commit()
    return user


# 根据用户名修改密码
def updatePasswordByUsername(user: DbUser):
    db = getDb()
    sql = "UPDATE tb_user SET password=%s WHERE username=%s"
    params = (user.password, user.username)
    db.execute(sql, params)
    db.commit()
    db.refresh(user)
    return user
