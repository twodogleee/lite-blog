"""

初始化数据库相关配置及数据相关操作对象

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_PATH

# 创建一个引擎对象，连接到SQLite数据库
engine = create_engine(
    DB_PATH, connect_args={"check_same_thread": False}
)

# 创建sqlSession
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
