from sqlalchemy import Column, Integer, String, BigInteger

from pydantic import BaseModel
from typing import Optional, List
from entity import Base

"""
菜单
"""


# 菜单的数据库对象 sqlalchemy模型
class DbMenu(Base):
    __tablename__ = 'tb_menu'
    # id
    id = Column(BigInteger(), primary_key=True)
    # 标题
    title = Column(String())
    # 内容
    content = Column(String())
    # 上级id
    sup_id = Column(BigInteger())
    # 层级
    level = Column(Integer())


# 菜单的pydantic对象 pydantic模型
class Menu(BaseModel):
    # id
    id: Optional[int] = None
    # 标题
    title: str
    # 内容
    content: str
    # 上级id
    sup_id: Optional[int] = 0
    # 层级
    level: Optional[int] = 1

    class Config:
        orm_mode = True


class MenuVo(BaseModel):
    # 菜单下的子集
    children: List[Menu]
