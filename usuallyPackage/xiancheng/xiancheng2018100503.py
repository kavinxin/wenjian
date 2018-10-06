#采用python3的新线程方法处理
import time
import threading
def loop1(in1):
    print("loop1 run is",time.ctime());
    print("loop1 is canshu",in1);
    time.sleep(4);
    print("loop1 end is",time.ctime());

def loop2(in1,in2):
    print("loop2 run is",time.ctime());
    print("loop2 is canshu",in1, in2);
    time.sleep(2);
    print("loop2 end is",time.ctime());

def main():
    print("Start is",time.ctime());
    t1=threading.Thread(target=loop1,args=("china",));
    t1.start();
    t2=threading.Thread(target=loop2,args=("japab","england"));
    t2.start();
    t1.join();
    t2.join();
    print("End is",time.ctime());

if __name__ == '__main__':
    main();
    while True:
        time.sleep(1);

