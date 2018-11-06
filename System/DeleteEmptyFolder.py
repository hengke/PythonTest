# coding: utf-8
import os #  引入文件操作库


def CLeanEmptyFiles(dir):
    """
    CLean empty files, 清理空文件夹和空文件
    :param path: 文件路径，检查此文件路径下的子文件
    :return: None
    """
    if os.path.isdir(dir):
        try:
            for item in os.listdir(dir):
                if item != 'System Volume Information':  # windows下没权限删除的目录：可在此添加更多不判断的目录
                    CLeanEmptyFiles(os.path.join(dir, item))
            if not os.listdir(dir):
                os.rmdir(dir)
                print("移除空目录：" + dir)
        except:
            pass
        else:
            pass
    elif os.path.isfile(dir): # 如果是文件
        if os.path.getsize(dir) == 0: # 文件大小为0
            os.remove(dir) # 删除这个文件
            print("移除空文件：" + dir)


if __name__ == "__main__": # 执行本文件则执行下述代码
    path = input("请输入文件夹路径:") # 输入路径
    CLeanEmptyFiles(path)
