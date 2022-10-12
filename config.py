import os


#fastapi 启动配置文件
class Config(object):
    """配置类"""
    #数据库连接信息
    HOST = "b38k252828.zicp.vip"
    PORT = "58997"
    PWD = "root"
    USER = "123456"
    DBNAME = "reggie"

    # 数据库配置
    SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DBNAME}"

class Text(object):
    """描述配置"""
    TITLE = "datacenter"
    VERSION = "v1.0"
    DESCRIPTION = "datacenter"


class FilePath(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 后端服务项目目录

    LOG_FILE_PATH = os.path.join(BASE_DIR, "logs") # 日志文件路径
    if not os.path.isdir(LOG_FILE_PATH): os.mkdir(LOG_FILE_PATH)

    LOG_NAME = os.path.join(LOG_FILE_PATH, 'log.log')