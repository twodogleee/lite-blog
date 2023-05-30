from sqlalchemy import Column, Integer, String

from pydantic import BaseModel
from typing import Optional
from entity import Base

"""
user实体类
"""


# user的数据库对象 sqlalchemy模型
class UserOrm(Base):
    __tablename__ = 'tb_user'
    # userId
    id = Column(String, primary_key=True)
    # 用户名
    username = Column(String(50))
    # 密码
    password = Column(String(255))
    # 邮件地址
    email = Column(String(255))


# user的pydantic对象 pydantic模型
class User(BaseModel):
    id: Optional[str] = None
    # 用户名
    username: str
    # 密码
    password: str
    # 邮件地址
    email: Optional[str] = None

    class Config:
        orm_mode = True
