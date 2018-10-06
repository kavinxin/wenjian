#度进程的工业风写法, 以及主进程和子进程的id获取
import time
import multiprocessing
import os

class jincheng(multiprocessing.Process):

    def __init__(self,i):
        super().__init__();
        self.i=i;

    def run(self):
        while True:
            print("当前的时间为: %s" % time.ctime());
            time.sleep(3);

def main():
    j=jincheng(5);
    j.start();
    print("主进程为：",os.getppid());
    print("子进程为：",os.getpid());


if __name__=='__main__':
    main();