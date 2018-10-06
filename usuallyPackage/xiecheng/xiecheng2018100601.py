#可迭代和迭代器的识别判断
import collections
from collections import Iterable
from collections import Iterator
l='I love zhangya';
print(isinstance(l,Iterable));
print(isinstance(l,Iterator));

print("*"*45);
#将可迭代对象转换成迭代器；
s=iter(l);
print(isinstance(s,Iterable));
print(isinstance(s,Iterator));

print("*"*45);
#简易生成器的制作处理；

def fun1():
    print("Step 1");
    yield "kavin";
    print("Step 2");
    yield  "tina";
    print("Step 3");
    yield "bill";

print(type(fun1));
a=next(fun1());
print(a);

print("*"*45);
#生成器的循坏获取
for x in fun1():
    print(x);