from dao import TokenDao as tokenDao
from entity.TokenEntity import DbToken
import time


def success(data):
    return {'status': 200, 'msg': 'success', 'data': data}


def fail(msg: str):
    return {'status': 500, 'msg': msg}


def to_result(data):
    if (data):
        return success(data)
    else:
        return fail('查询为空或者操作失败')


# 判断token是否过期
def check_token(token_str: str):
    # 根据token字符串 获取token信息
    db_token = tokenDao.get_token_by_token_str(token_str)
    # 如果db token信息为空 则失败
    if db_token is None:
        return True
    # 获取当前时间戳
    timestamp = int(time.time())
    # token过期
    if timestamp >= db_token.expires_time:
        return True
    return False
