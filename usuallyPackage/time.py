import time
import datetime
from datetime import datetime
print(type(time.time));
print("*"*20);
t=time.localtime();
print(t);
print(type(t));
print("*"*20);
print(t.tm_hour);
print("*"*20);
for x in t:
    print(x,end="\n");
print("*"*20);
tt=time.asctime(t);
print(type(tt));
print("*"*20);
print(time.ctime(time.mktime(t)));
print("*"*20);
print(tt)
print("*"*20);
p=time.strftime("%Y年%m月%d日:%H:%M:%S",t);
print(p);
print("*"*20);
print(datetime.date(2018,9,18));
print(datetime.date(2018,9,18).year);
print(datetime.date(2018,9,18).month);
print(datetime.date(2018,9,18).day);
print(datetime.date(2018,9,18).weekday());
print("*"*20);

