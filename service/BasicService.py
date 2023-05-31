def suc(data):
    return {'status': 200, 'msg': 'suc', 'data': data}


def fail(msg: str):
    return {'status': 500, 'msg': msg}


def toResult(data):
    if (data):
        return suc(data)
    else:
        return fail('查询为空或者操作失败')
