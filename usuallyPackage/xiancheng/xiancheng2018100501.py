#未含参数的线程案例
import time
import _thread
def loop1():
    print("loop1 run is :",time.ctime());
    time.sleep(4);
    print("loop1 rend is :",time.ctime());

def loop2():
    print("loop2 run is ",time.ctime());
    time.sleep(2);
    print("loop2 end is ",time.ctime());

def main():
    print("start is ",time.ctime());
    _thread.start_new_thread(loop1,());
    _thread.start_new_thread(loop2,());
    print("end is ",time.ctime());

if __name__ == '__main__':
    main();
    while True:
        time.sleep(1);

