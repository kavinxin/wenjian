#多进程的处理,多进程的一般写法
import multiprocessing
import time

def co(i):
    while True:
        print("当前的时间为：",time.ctime());
        time.sleep(i);

def main():
    t=multiprocessing.Process(target=co,args=(5,));
    t.start();


if __name__ == '__main__':
    main();
