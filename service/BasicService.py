def suc(data):
    return {'status': 200, 'msg': 'suc', 'data': data}


def fail(msg: str):
    return {'status': 500, 'msg': msg}
