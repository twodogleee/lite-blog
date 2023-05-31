"""

初始化数据库相关配置及数据相关操作对象

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_PATH
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import Session

# 创建一个引擎对象，连接到SQLite数据库
engine = create_engine(
    DB_PATH,
    connect_args={"check_same_thread": False},
    poolclass=QueuePool,
    pool_size=2,
    max_overflow=10,
    pool_timeout=30
)

# 创建连接池
# pool = QueuePool(
#     creator=engine.connect,
#     max_overflow=10,  # 连接池中最多可以创建的连接数
#     pool_size=2,  # 连接池中保持的连接数
# )

# 创建 SessionLocal 数据库会话对象
# 这儿使用了连接池 可以直接实例化SessionLocal来访问数据库 用完之后会被连接池回收
# 如: db = SessionLocal() 即可
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

"""
这个地方我直接使用了 sqlalchemy的链接池来控制链接的频繁创建
并没有使用fastApi的依赖注入
我想的是所有的数据库操作抽离到了dao层,执行完操作返回再执行下一步的业务逻辑,讲道理能解决大部分的并发问题
fastApi属于多线程框架,如果在同一个线程中使用了不同的数据库会话可能会造成查询结果错误
例如，如果在一个会话中修改了一个对象，但在另一个会话中查询了同一个对象，那么查询结果可能会不正确，因为它没有反映出先前的修改。这是因为每个会话都有自己的缓存，不同的会话之间无法共享缓存。
此外，如果在多个会话中同时执行操作，可能会导致并发问题，例如死锁和竞态条件。这是因为每个会话都有自己的事务，而事务之间的交互可能会导致并发问题。
最好使用相同的数据库会话对象来执行整个调用中的所有操作，以确保数据的一致性和正确性。如果需要在多个线程中执行操作，则可以使用线程本地存储来确保每个线程都使用自己的数据库会话对象。
比如fastApi中推荐操作:
# 定义依赖项函数
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# 在路由中使用依赖项函数
@app.get("/")
async def read_root(db = Depends(get_db)):
    # 在此处执行数据库操作
    # ...
    return {"message": "Hello World"}
在api层将数据库的会话对象通过依赖注入,然后在下层方法中用参数接受而达到使用同一个数据库会话对象,可以保证在同一个调用中不会出现不一样的结果
"""


def getDb() -> Session:
    return SessionLocal()
