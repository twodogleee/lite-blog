from entity.TokenEntity import DbToken
from sqlalchemy.orm import Session
from dao import SessionLocal
from sqlalchemy import and_, text


# 根据userId查询token
def get_token_by_user_id(userId: str):
    with SessionLocal() as db:
        return db.query(DbToken).filter(DbToken.user_id == userId).first()


# 根据tokenStr查询token
def get_token_by_token_str(token_str: str):
    with SessionLocal() as db:
        return db.query(DbToken).filter(DbToken.token_str == token_str).first()


# 保存token
def save_token(token: DbToken):
    with SessionLocal() as db:
        result = db.add(token)
        flag = db.commit()
        return flag is None


# 修改token
def update_token(token: DbToken):
    with SessionLocal() as db:
        sql = text('UPDATE tb_token SET token_str=:token_str,expires_time=:expires_time WHERE user_id=:user_id')
        params = {'token_str': token.token_str, 'expires_time': token.expires_time, 'user_id': token.user_id}
        result = db.execute(sql, params)
        db.commit()
    return result.rowcount != 0
