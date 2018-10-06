#线程属性的使用
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

def loop3(in1,in2,in3):
    print("loop3 run is",time.ctime());
    print("loop3 is canshu",in1,in2,in3);
    time.sleep(5);
    print("loop3 end is ",time.ctime());

def main():
    print("Start is",time.ctime());
    t1=threading.Thread(target=loop1,args=("我是第一个参数",));
    t1.setName("thread01");
    t1.start();

    t2=threading.Thread(target=loop2,args=("我是二线程的第一个参数","我是二线程的第二个参数"));
    t2.setName("thread02");
    t2.start();

    t3=threading.Thread(target=loop3,args=("我是三线程的第一个参数","我是三线程的第二个参数","我是三线程的第三个参数"));
    t3.setName("thread03");
    t3.start();

    t1.join();
    t2.join();
    t3.join();

    time.sleep(3);
    for thr in threading.enumerate():
        print("当前运行的线程是：{0}".format(thr.getName()));
    print("当前运行的线程数有：{0}".format(threading.activeCount()));

    print("main is end",time.ctime());

if __name__=='__main__':
    main();
    while True:
        time.sleep(1);

