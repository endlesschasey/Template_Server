from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from logger import logger
from config import Setting

Base = declarative_base()

def get_sync_engine():
    try:
        return create_engine(
            Setting.SQLALCHEMY_DATABASE_URL,
            connect_args={"options": "-c timezone=Asia/Shanghai"},
        )
    except Exception as e:
        logger.exception("Error creating synchronous engine: %s", str(e))
        raise

engine = get_sync_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 尝试设置异步引擎
try:
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

    def get_async_engine():
        try:
            async_db_url = Setting.SQLALCHEMY_DATABASE_URL.replace('postgresql://', 'postgresql+asyncpg://')
            return create_async_engine(
                async_db_url,
                future=True,
                connect_args={"command_timeout": 60},  # 移除 'options' 参数
            )
        except Exception as e:
            logger.exception("Error creating asynchronous engine: %s", str(e))
            return None

    async_engine = get_async_engine()
    if async_engine:
        AsyncSessionLocal = sessionmaker(
            class_=AsyncSession,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            bind=async_engine
        )
    else:
        logger.warning("Async database engine creation failed. Async features will not be available.")
        AsyncSessionLocal = None
except ImportError:
    logger.warning("asyncpg not installed. Async database features will not be available.")
    async_engine = None
    AsyncSessionLocal = None

# 确保导出所有需要的对象
__all__ = ['Base', 'engine', 'async_engine', 'SessionLocal', 'AsyncSessionLocal']