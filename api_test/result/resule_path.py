import os
#获取当前目录
def result_path():
    resuilt_path = os.path.split(os.path.realpath(__file__))[0]
    return resuilt_path




if __name__ == '__main__':
    s = result_path()
    print(s)