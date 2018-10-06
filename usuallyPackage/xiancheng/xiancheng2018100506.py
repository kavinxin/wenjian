#线程锁的处理
import threading
import time
sum=0;
lopsum=1000000;
lock=threading.Lock();
def add():
    global sum,lopsum;
    for i in range(1,lopsum):
        lock.acquire();
        sum+=1;
        lock.release();

def jian():
    global sum,lopsum;
    for x in range(1,lopsum):
        lock.acquire();
        sum-=1;
        lock.release();

def main():
    print("Now is start",time.ctime());
    t1=threading.Thread(target=add,args=());
    t2=threading.Thread(target=jian,args=());
    t1.start();
    t2.start();

    t1.join();
    t2.join();
    print("sum=",sum);
    print("End is now",time.ctime());

if __name__ == '__main__':
    main();
    while True:
        time.sleep(1);
