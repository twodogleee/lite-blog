from entity.ContentEntity import DbContent, ContentReq
from sqlalchemy.orm import Session
from dao import SessionLocal
from sqlalchemy import and_, text, desc


# 根据id查询文章详细信息
def get_content_by_id(id: int):
    with SessionLocal() as db:
        return db.query(DbContent).filter(DbContent.id == id).first()


# 分页查询文章列表
def get_content_page(req: ContentReq):
    with SessionLocal() as db:
        query = db.query(DbContent)
        if req.menu_id:
            query = query.filter(DbContent.menu_id == req.menu_id)
        return query.order_by(desc(DbContent.create_time)).offset(req.page).limit(req.pageSize).all()


# 保存文章信息
def save_content(content: DbContent):
    with SessionLocal() as db:
        result = db.add(content)
        flag = db.commit()
        return flag is None


# 修改文章信息
def update_content(content: DbContent):
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
        sql = text(
            'UPDATE tb_content SET title=:title,file_name=:file_name,menu_id=:menu_id,create_time=:create_time  WHERE id=:id')
        params = {'title': content.title, 'file_name': content.file_name, 'menu_id': content.menu_id,
                  'create_time': content.create_time,
                  'id': content.id}
        result = db.execute(sql, params)
        db.commit()
    return result.rowcount != 0


# 根据id删除menu
def del_content(id: int):
    with SessionLocal() as db:
        db.query(DbContent).filter(DbContent.id == id).delete()
        flag = db.commit()
        return flag is None
