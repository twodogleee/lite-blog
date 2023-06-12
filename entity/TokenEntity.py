from sqlalchemy import Column, Integer, String, BigInteger

from pydantic import BaseModel
from typing import Optional
from entity import Base

"""
token
"""


# token的数据库对象 sqlalchemy模型
class DbToken(Base):
    __tablename__ = 'tb_token'
    # userId
    user_id = Column(String, primary_key=True)
    # token
    token_str = Column(String(255))
    # 失效时间
    expires_time = Column(BigInteger())


# token的pydantic对象 pydantic模型
class Token(BaseModel):
    # 用户id
    user_id: str
    # token
    token_str: str
    expires_time: int

    class Config:
        orm_mode = True
