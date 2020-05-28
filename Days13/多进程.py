from os import getpid
from multiprocessing import Process
from time import time,sleep
from random import randint
def download_task(filename):
    print('开始下载进程，进程号[%d]'%getpid())
    print('开始下载文件%s'%filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，耗时%d秒'%(filename,time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task,args=('Python从入门到住院',))
    p2 = Process(target=download_task,args=('FUjian hot',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总计耗时%.2f'%(end-start))
if __name__ == '__main__':
    main()