import configparser
import pathlib
from pathlib import Path


def read_dirs(ini_filename, section, arg):
    """
    通过ini文件名,节和参数取得要操作的多个目录
    """
    current_path = pathlib.PurePath(__file__).parent
    inifile = current_path.joinpath(ini_filename)

    # cf是类ConfigParser的实例
    cf = configparser.ConfigParser()

    # 读取ini文件
    cf.read(inifile)

    # 读取work节 和 searchpath参数 
    return cf.get(section, arg).split(",")


def locate_file(base_dir, keywords):
    p = Path(base_dir)
    files = p.glob(keywords)
    return list(files)


dirs = read_dirs('search.ini', 'work', 'searchpath')
# ['/Users/edz', '/tmp']
keywords = '**/*BBC*'

# 定义存放查找结果的列表
result = []

# 从每个文件夹中搜索文件
for dir in dirs:
    files = locate_file(dir, keywords)
    result += files

# 将PosixPath转为字符串
# pathlib 库为了规避不同操作系统路 径写法的差异，就把路径统一定义为 PosixPath() 对象。因此，你在使用这些路径的时 候，需要先将 PosixPath 对象转换为字符串类型。
print([str(r) for r in result])
