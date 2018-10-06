from datetime import datetime as dt;
import os
import shutil
print(dt.now());
print(os.getcwd());
os.chdir("/Users/xinhai/");
print(os.getcwd());
os.chdir("/Users/xinhai/PycharmProjects/untitled/usuallyPackage");
print(os.getcwd());
ld=os.listdir();
for x in ld:
    print(x,end="\n");
gt=os.getenv("PATH");
print(gt);
print(os.name);
print(os.curdir);
print(os.pardir);
print(os.sep);
print(os.linesep);
ac=os.path.abspath(".");
print(ac);
print(os._exists("/hone"));
print(os._Environ);
help(os.altsep);
help(shutil);