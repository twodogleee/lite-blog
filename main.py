"""
这是fastApi主程序的入口
"""

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles

# 引入所有接口层
from controller import testController, userController, menuController, contentController

from dao import engine
from entity import Base

import service.BasicService as basicService

import re
from config import FILE_PATH

# 地址匹配 用来匹配请求地址是否需要登录
auth_url = r"(/admin)"

app = FastAPI(
    # 创建一个FastAPI实例
    # 这里的变量 app 会是 FastAPI 类的一个「实例」。
    # 这个实例将是创建你所有 API 的主要交互对象。
    # 这个 app 同样在命令中被 uvicorn 所引用:uvicorn main:app --reload
    title='lite-blog接口文档',
    description='lite-blog是一个轻量化的博客应用',
    version='1.0.0',
    docs_url='/doc',  # swagger
    redoc_url='/reDoc'  # reDoc
)
# 静态文件夹配置
# app.mount("/static", StaticFiles(directory="static"), name="static")

# 将所有接口层加入路由
# 等同于java中的springMvc 将接口注册到服务器中进行路由
app.include_router(testController, prefix='/test', tags=['测试'])
app.include_router(userController, prefix='/user', tags=['用户相关接口'])
app.include_router(menuController, prefix='/menu', tags=['菜单栏相关接口'])
app.include_router(contentController, prefix='/content', tags=['文章相关接口'])
app.mount("/file", StaticFiles(directory=FILE_PATH), name="file")

# 允许跨域访问的来源地址
origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]
# 添加跨域请求处理
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 请求拦截
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    # 请求地址
    print(f"Request {request.method} {request.url}")
    # 判断请求地址中是否有需要登录才能访问的地址
    match = re.search(auth_url, request.url.path)
    # 如果需要认证
    if match:
        # 获取请求头中的token
        token = request.headers.get('token')
        # 判断token是否合法
        if basicService.check_token(token):
            return JSONResponse(
                status_code=401,
                content={'status': 401, 'msg': '非法操作，请登录后操作'}
            )
            # raise HTTPException(status_code=401, detail='非法操作，请登录后操作')

    # print(request.headers.get('token'))
    # 调用下一个中间件或路由处理程序
    response = await call_next(request)
    return response


# 如果该模块作为主程序执行
if __name__ == '__main__':
    # 创建数据库表
    Base.metadata.create_all(bind=engine)
    # 设置服务器参数
    # uvicorn等同于java中的tomcat
    uvicorn.run(app, host="127.0.0.1", port=8080)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
