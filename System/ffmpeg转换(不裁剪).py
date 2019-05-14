# coding: utf-8
import os #  引入文件操作库

def ffmpegAviToMp4(dir):
    """
    使用ffmpeg从avi转换mp4
    :param file: 文件路径，绝对路径
    :return: None
    """
    if os.path.isdir(dir):
        try:
            for item in os.listdir(dir):
                if item != 'System Volume Information':  # windows下没权限删除的目录：可在此添加更多不判断的目录
                    ffmpegAviToMp4(os.path.join(dir, item))
            if not os.listdir(dir):
                # os.rmdir(dir)
                print("空目录：" + dir)
        except:
            pass
        else:
            pass
    elif os.path.isfile(dir): # 如果是文件
        filepath,fullflname = os.path.split(dir)
        fname,ext = os.path.splitext(fullflname)
        out = os.path.join(filepath,(fname + ".mp4"))
        if (not os.path.isfile(out)) and ext == ".avi":
            cmd = "D:\\Tools\\FFmpeg\\bin\\ffmpeg.exe"
            cmd = cmd + " -i \"" + dir + "\""
            cmd = cmd + " -map 0 -c:v libx264 "
            cmd = cmd + "\"" + out + "\""
            # print(cmd)
            os.system(cmd)
        else:
            pass



if __name__ == "__main__": # 执行本文件则执行下述代码
    path = input("请输入文件夹路径:") # 输入路径
    # path = r"F:\FFOutput\python\2017年老男孩最新全栈python第2期视频教程(小边)"
    ffmpegAviToMp4(path)
