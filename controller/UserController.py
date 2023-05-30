from fastapi import Depends
from entity.UserEntity import User, UserOrm
from dao import get_db
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

# 生成路由 这个路由可以匹配返回的model不用手动申明
userController = InferringRouter()


@userController.post('/login')
async def userLogin(user: User, db: Session = Depends(get_db)):
    userOrm = UserOrm(**user.dict())
    # db = SessionLocal()

    db.add(userOrm)
    db.commit()
    db.refresh(userOrm)
    # print(userOrm)
    return userOrm


@userController.get('/getUserById/v1/{userId}')
async def getUserById(userId: str, db: Session = Depends(get_db)):
    return db.query(UserOrm).filter(UserOrm.id == userId).first()
