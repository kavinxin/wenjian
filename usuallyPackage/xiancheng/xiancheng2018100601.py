#可重入锁的案例：可重入锁，即表示一把锁可支持多次请求，不用在第一次请求之后释放后再请求，可以在不释放的前提
#下支持多次请求所思
import time
import threading
num=0;
suo=threading.RLock();
def main():

    for x in range(5):
        t=mythread();
        t.start();

class mythread(threading.Thread):
    def run(self):
        global num;
        time.sleep(1);
        if suo.acquire(timeout=1):
            num+=1;
            msg="you haved a suo"+"----"+self.name+"----"+str(num);
            print(msg);
        suo.acquire();
        suo.release();
        suo.release();

if __name__=='__main__':
    main();
    while True:
        time.sleep(1);


