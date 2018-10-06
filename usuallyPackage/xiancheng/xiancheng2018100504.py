import time
import threading
def fun():
    print("start beging!",time.ctime());
    time.sleep(3);
    print("fun is end!",time.ctime());

print("main is start!",time.ctime());
t1=threading.Thread(target=fun,args=());
t1.daemon=True;
t1.start();
time.sleep(1);
print("main is over!",time.ctime());