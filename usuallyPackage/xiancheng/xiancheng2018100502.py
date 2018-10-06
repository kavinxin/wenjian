#含参数的线程案例
import time
import _thread
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
    print(("start is",time.ctime()));
    _thread.start_new_thread(loop1,("kavin",));
    _thread.start_new_thread(loop2,("tina","bill",));
    print("end is ",time.ctime());

if __name__ == '__main__':
    main();
    while True:
        time.sleep(1);



