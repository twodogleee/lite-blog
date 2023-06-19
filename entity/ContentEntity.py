from sqlalchemy import Column, Integer, String, BigInteger

from pydantic import BaseModel
from typing import Optional, List
from entity import Base

"""
文章列表
"""


# 文章 的数据库对象 sqlalchemy模型
class DbContent(Base):
    __tablename__ = 'tb_content'
    # id
    id = Column(BigInteger(), primary_key=True)
    # 文章标题
    title = Column(String())
    # .md文件名
    file_name = Column(String())
    # 菜单id
    menu_id = Column(BigInteger())
    # 创建时间
    create_time = Column(String())


# 文章 的pydantic对象 pydantic模型
class Content(BaseModel):
    # id
    id: Optional[int] = None
    # 文章标题
    title: str
    # .md文件名
    file_name: str
    # 菜单id
    menu_id: Optional[int] = 0
    # 创建时间
    create_time: Optional[str] = None

    class Config:
        orm_mode = True


# 文章查询
class ContentReq(BaseModel):
    menu_id: Optional[str] = None
    page: int
    pageSize: int
