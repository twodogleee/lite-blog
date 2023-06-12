from entity.MenuEntity import DbMenu
from sqlalchemy.orm import Session
from dao import SessionLocal
from sqlalchemy import and_, text


# 根据id查询菜单信息
def get_menu_by_id(id: int):
    with SessionLocal() as db:
        return db.query(DbMenu).filter(DbMenu.id == id).first()


# 查询菜单集合
def get_menu_list():
    with SessionLocal() as db:
        return db.query(DbMenu).order_by(DbMenu.level, DbMenu.id).all()


# 保存菜单信息
def save_menu(menu: DbMenu):
    with SessionLocal() as db:
        result = db.add(menu)
        flag = db.commit()
        return flag is None


# 修改菜单信息
def update_menu(menu: DbMenu):
    with SessionLocal() as db:
        '''
     # id
    id: int
    # 标题
    title: str
    # 内容
    content: str
    # 上级id
    sup_id: int

        '''
        sql = text('UPDATE tb_menu SET title=:title,content=:content,sup_id=:sup_id WHERE id=:id')
        params = {'title': menu.title, 'content': menu.content, 'sup_id': menu.sup_id, 'id': menu.id}
        result = db.execute(sql, params)
        db.commit()
    return result.rowcount != 0


# 根据id删除menu
def del_menu(id: int):
    with SessionLocal() as db:
        db.query(DbMenu).filter(DbMenu.id == id).delete()
        flag = db.commit()
        return flag is None
