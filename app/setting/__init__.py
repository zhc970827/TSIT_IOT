import os

env = os.getenv("ENV", "")
if env:
    # 如果有虚拟环境 则是 生产环境
    print("----------生产环境启动------------")
    from .production_config import config
else:
    # 没有则是开发环境
    print("----------开发环境启动------------")
    from .development_config import config