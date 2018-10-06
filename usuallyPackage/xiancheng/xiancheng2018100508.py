import threading
import time
sem=threading.Semaphore(3);
def func():
    if sem.acquire():
        for i in range(5):
            print(threading.current_thread().getName()+'get sem!');
            time.sleep(5);
            sem.release();
            print(threading.current_thread().getName()+'release sem!');

for i in range(10):
    t1=threading.Thread(target=func,args=());
    t1.start();
