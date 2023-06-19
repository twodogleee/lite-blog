from entity.ContentEntity import Content, ContentReq
from fastapi_utils.inferring_router import InferringRouter
from service import ContentService as contentService
from fastapi import File, UploadFile, Form
import os
from config import FILE_PATH

# 生成路由 这个路由可以匹配返回的model不用手动申明
contentController = InferringRouter()


# 根据id查询文章信息
@contentController.get('/getContentById/{id}')
async def get_content_by_id(id: int):
    return contentService.get_content_by_id(id)


# 查询文章信息列表
@contentController.post("/getContentPage")
async def get_content_page(req: ContentReq):
    return contentService.get_content_page(req)


# 保存文章信息
@contentController.post("/admin/save")
async def save_content(content: Content):
    return contentService.save_content(content)


# 修改文章信息
@contentController.post("/admin/update")
async def update_content(content: Content):
    return contentService.update_content(content)


# 根据id删除menu
@contentController.get("/admin/delContent/{id}")
async def del_content(id: int):
    return contentService.del_content(id)


# 上传md文件并保存文章关联信息
@contentController.post("/uploadMd")
async def upload_md(file: UploadFile = File(...),
                    title: str = Form(...),
                    menu_id: int = Form(...)):
    save_dir = FILE_PATH  # 指定保存文件的目录
    file_name = file.filename
    save_path = os.path.join(save_dir, file_name)  # 拼接保存文件的完整路径
    '''
    # 文章标题
    title: str
    # .md文件名
    file_name: str
    # 菜单id
    menu_id: Optional[int] = 0
    '''
    with open(save_path, 'wb') as f:
        f.write(file.file.read())  # 将文件内容写入到保存路径中
        return contentService.save_content(
            Content(**dict({"title": title, "file_name": file_name, "menu_id": menu_id})))
