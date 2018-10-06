import os
import shutil
import random
print(os.curdir);
print(os.pardir);
print(os.sep);
path="/"+"home/tina"+"/";
print(path);
print(os.name);
list1=[1,2,3,4,5,6,7,8,9,10];
for x in list1:
    print(x,"\n");
print("-"*20);
path1=os.path.abspath(".");
print(path1);
print("-"*20);
print(os.curdir);
print("-"*20);
print(os.path.basename("."));
print("-"*20);
print(os.path.basename("/Users/xinhai/PycharmProjects/untitled/usuallyPackage/bao.py"));
print("-"*20);
bd="/home/kavin";
tg="wahaha.th";
print(os.path.join(bd,tg));
print("-"*20);
print(os.path.isdir("."));
print("-"*20);
print(os.path.isdir("whaha.th"));
print("-"*100);
print(os.path.exists("bao.py"));
print("-"*100);
cs=shutil.copy("/Users/xinhai/PycharmProjects/untitled/usuallyPackage/bao.py","/Users/xinhai/PycharmProjects/untitled/xuexi/pao.py");
print(cs);
rst=shutil.copyfile("/Users/xinhai/PycharmProjects/untitled/usuallyPackage/bao.py","/Users/xinhai/PycharmProjects/untitled/xuexi/kong.py");
print(rst);
print("-"*100);
rst1=shutil.make_archive("/Users/xinhai/PycharmProjects/untitled/usuallyPackage/xuexi","zip","/Users/xinhai/PycharmProjects/untitled/xuexi");
print(rst1);
print(os.listdir("/Users/xinhai/PycharmProjects/untitled/usuallyPackage/"));
print(rst1);
print(random.random());
print("-"*100);
l=[str(i)+"haha" for i in range(0,10)];
rt=random.choice(l);
print(rt);
for p in l:
    print(p,"\n");
print("-"*100);
print(random.randint(0,100));






