"""
这是fastApi主程序的入口
"""

import uvicorn
from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles

# 引入所有接口层
from controller import testController, userController

from dao import engine
from entity import Base


app = FastAPI(
    # 创建一个FastAPI实例
    # 这里的变量 app 会是 FastAPI 类的一个「实例」。
    # 这个实例将是创建你所有 API 的主要交互对象。
    # 这个 app 同样在命令中被 uvicorn 所引用:uvicorn main:app --reload
    title='lite-blog接口文档',
    description='lite-blog是一个轻量化的博客应用',
    version='1.0.0',
    docs_url='/docs',  # swagger
    redoc_url='/reDoc'  # reDoc
)
# 静态文件夹配置
# app.mount("/static", StaticFiles(directory="static"), name="static")

# 将所有接口层加入路由
# 等同于java中的springMvc 将接口注册到服务器中进行路由
app.include_router(testController, prefix='/test', tags=['test'])
app.include_router(userController, prefix='/user')

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
