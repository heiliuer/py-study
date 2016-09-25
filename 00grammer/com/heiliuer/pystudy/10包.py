# 目录中只有包含 _init_.py文件的系统才识别为包
from _collections_abc import __all__


# 为了解决window不区分大小写，但是模块名区分大小写的问题，模块设计者需要包中的__init__.py文件中加入__all__集合（告诉python模块索引系统，这个包包含哪些模块（模块区分大小写））  
# __all__={"echo","surround",""}；
