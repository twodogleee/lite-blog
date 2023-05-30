from entity.UserEntity import User, UserOrm
from sqlalchemy.orm import Session


# 根据用户名&密码 查询用户信息
def getUserByUsernameAndPassword(user: UserOrm, db: Session):
    return db.query(UserOrm).filter(UserOrm.username == user.username and UserOrm.password == user.password).first()


# 根据userId查询用户信息
def getUserById(userId: str, db: Session):
    return db.query(UserOrm).filter(UserOrm.id == userId).first()


# 根据用户名查询用户
def getUserByUserName(userName: str, db: Session):
    return db.query(UserOrm).filter(UserOrm.username == userName).first()


# 创建用户信息
def createUser(user: UserOrm, db: Session):
    db.add(user)
    db.refresh(user)
    db.commit()
    return user


# 根据用户名修改密码
def updatePasswordByUsername(user: UserOrm, db: Session):
    sql = "UPDATE tb_user SET password=%s WHERE username=%s"
    params = (user.password, user.username)
    db.execute(sql, params)
