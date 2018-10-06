#生产者消费者模型queue的使用和线程工厂风的写法
import threading
import time
import queue

class producer(threading.Thread):
    def run(self):
        global queue;
        count=0;
        while True:
            if queue.qsize()<1000:
                for i in range(100):
                    count+=1;
                    msg="生产产品"+str(count);
                    queue.put(msg);
                    print(msg);
            time.sleep(0.5);

class customer(threading.Thread):
    def run(self):
        global queue;
        count=0;
        while True:
            if queue.qsize()>1000:
                for i in range(3):
                    msg=self.name+'消费了'+queue.get();
                    print(msg);
            time.sleep(1);

def main():
    global queue
    queue=queue.Queue();
    for i in range(500):
        queue.put('初始产品'+str(i));
    for i in range(3):
        p=producer();
        p.start();
    for i in range(3):
        c=customer();
        c.start();

if __name__=='__main__':
    main();
    while True:
        time.sleep(3);






