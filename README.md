# lite-blog
一个轻量化的博客应用

## 简介:
关于lite-blog则字面意思**轻量化的博客**，目的就是打造一个很轻量化的博客应用。其实市面上有很多成熟的博客应用了，但是对于个人来讲写笔记什么的只用markdown，很多功能用不上显的些许臃肿。于是便有了该项目计划，主打一个**轻量**方便服务器到期迁移。
更主要当做学习！刚好还能搭一个轻量化的web应用，如果以后用得着还能copy过去改吧改吧。



## 技术及框架:

- python+fastApi
- sqlLite
- next.js

### python环境
调试环境python=3.10.10

```shell
#依赖
pip install -r requirements.txt
#加速镜像安装
pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#docker 运行
docker build -t lite-blog:lates .
docker run -d -p 8080:8080 lite-blog:lates
#挂载数据目录
docker run -d -p 8080:8080 -v /path/db:/data/db -v /path/file:/data/file lite-blog:lates

#访问
http://IP:8080
```

## 核心功能:

### 前端主要功能:
1. 文章分类及导航
2. 文章列表能正常显示
3. 文章详情直接解析.md能正常展示md的结构及md目录,以及图片内容
4. 支持更换主页背景图片
5. 页面路由控制
6. 简单的后管

### 后端主要功能:
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
5. 快速迁移

## 施工计划:
1. 后端项目搭建
2. 完成后端核心功能开发
3. 前端项目搭建
4. 完成前端核心功能开发



