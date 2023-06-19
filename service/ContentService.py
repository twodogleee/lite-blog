from dao import ContentDao as contentDao
from entity.ContentEntity import DbContent, Content, ContentReq
from service import BasicService as basicService
import time
import datetime
import os
from config import FILE_PATH


# 根据id查询文章信息
def get_content_by_id(id: int):
    return basicService.success(contentDao.get_content_by_id(id))


# 查询文章信息列表
def get_content_page(req: ContentReq):
    offset = (req.page - 1) * req.pageSize
    limit = req.pageSize
    req.page = offset
    req.pageSize = limit
    return basicService.success(contentDao.get_content_page(req))


# 保存文章信息
def save_content(content: Content):
    content.id = int(time.time())
    content.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return basicService.success(True) if contentDao.save_content(DbContent(**content.dict())) else basicService.fail(
        '操作失败')


# 修改文章信息
def update_content(content: Content):
    return basicService.success(True) if contentDao.update_content(DbContent(**content.dict())) else basicService.fail(
        '操作失败')


# 根据id删除menu
def del_content(id: int):
    content = contentDao.get_content_by_id(id)
    if content:
        return basicService.fail('操作失败')
    folder_path = FILE_PATH
    file_path = os.path.join(folder_path, content.file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
    return basicService.success(True) if contentDao.del_content(id) else basicService.fail(
        '操作失败')
