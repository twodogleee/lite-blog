# lite-blog
一个轻量化的博客应用

## 简介:
关于lite-blog则字面意思**轻量化的博客**，目的就是打造一个很轻量化的博客应用。其实市面上有很多成熟的博客应用了，但是对于个人来讲写笔记什么的只用markdown，很多功能用不上显的些许臃肿。于是便有了该项目计划，主打一个**轻量**方便服务器到期迁移。主要当做学习！



## 技术及框架:

- python+fastApi
- sqlLite
- next.js

### python环境
python=3.10.10
```
// 目前其他依赖版本,用idea一键构建导入的依赖.使用的venv虚拟环境
anyio             3.7.0
click             8.1.3
exceptiongroup    1.1.1
fastapi           0.95.2
h11               0.14.0
httptools         0.5.0
idna              3.4
pip               22.3.1
pydantic          1.10.8
python-dotenv     1.0.0
PyYAML            6.0
setuptools        65.5.1
sniffio           1.3.0
SQLAlchemy        2.0.15
starlette         0.27.0
typing_extensions 4.6.2
uvicorn           0.22.0
uvloop            0.17.0
watchfiles        0.19.0
websockets        11.0.3
wheel             0.38.4

```

```
pip install sqlalchemy
pip install fastapi-utils

```

## 核心功能:

### 前台:
1. 文章分类及导航
2. 文章列表能正常显示
3. 文章详情能正常展示md的结构及md目录,以及图片内容
4. 支持更换主页背景图片
5. 页面路由控制

### 后管:
1. 新增/删除/覆盖.md文件
2. md文件中可附带图片
3. 支持实际的阅读量统计
4. 支持简单的后管登录(不做权限管理)
5. 支持文章分类管理
6. 支持将文章放到指定分类中

## 可能会有:
1. 看板娘
2. 背景音乐
3. 鼠标样式
4. 评论
5. 自动化部署
6. 快速迁移

## 施工计划:
1. 后端项目搭建
2. 完成后端核心功能开发
3. 前端项目搭建
4. 完成前端核心功能开发



