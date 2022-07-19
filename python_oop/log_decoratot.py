'''
    Created by dl on 2022/7/18
    PROJECT_NAME：lagou_test
'''
import logging

# 设置基本配置
logging.basicConfig(level=logging.DEBUG)
# 自定义 logger
logging = logging.getLogger('log')

# 定义装饰器

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.debug(f"装饰器{log_decorator.__name__}  - > 传入 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper