from entity.UserEntity import DbUser
from sqlalchemy.orm import Session
from dao import SessionLocal
from sqlalchemy import and_, text


# 根据用户名&密码 查询用户信息
def getUserByUsernameAndPassword(user: DbUser):
    with SessionLocal() as db:
        return db.query(DbUser).filter(and_(DbUser.username == user.username, DbUser.password == user.password)).first()


# 根据userId查询用户信息
def getUserById(userId: str):
    with SessionLocal() as db:
        return db.query(DbUser).filter(DbUser.id == userId).first()


# 根据用户名查询用户
def getUserByUserName(userName: str):
    with SessionLocal() as db:
        return db.query(DbUser).filter(DbUser.username == userName).first()


# 创建用户信息
def createUser(user: DbUser):
    with SessionLocal() as db:
        result = db.add(user)
        flag = db.commit()
        return flag is None


# 根据用户名修改密码
def updatePasswordByUsername(user: DbUser):
    with SessionLocal() as db:
        sql = text("UPDATE tb_user SET password=:password WHERE username=:username")
        params = {"password": user.password, "username": user.username}
        result = db.execute(sql, params)
        db.commit()
    return result.rowcount != 0
