#多进程中生产者消费者模型
import time
import multiprocessing

def xiaofeizhe(xiaofei):
    print("消费者开始 %s:" % time.ctime());
    while True:
        i=xiaofei.get();
        if i is None:
            break;
        print("消费者拿出的是： ",i);
    print("东西被拿走的时间： %s:" % time.ctime());

def shengchanzhe(shangpin ,shengchan):
    for i in shangpin:
        print("东西被创造的时间是： ",time.ctime());
        shengchan.put(i);
        print(("东西放进仓库的时间是： %s" % time.ctime()));

def main():
    q=multiprocessing.JoinableQueue();
    xiaofeizhe1=multiprocessing.Process(target=xiaofeizhe,args=(q,));
    xiaofeizhe1.start();
    xiaofeizhe2=multiprocessing.Process(target=xiaofeizhe,args=(q,));
    xiaofeizhe2.start();
    shangpin=[1,2,3,4,5];
    shengchanzhe(shangpin,q);
    q.put(None);
    q.put(None);
    xiaofeizhe2.join();
    xiaofeizhe1.join();

if __name__ == '__main__':
        main();
