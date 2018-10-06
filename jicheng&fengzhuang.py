# -*- coding: UTF-8 -*-#!
class person():
    def __init__(self,name):
        print(name);
class student(person):
    def __init__(self,name):
        super(student,self).__init__(name);
        print("这是增加的构造！");
s=student("kavin");
print("*"*20);
print(type(student.__mro__));
class teacherMxin(person):
    def work(self):
        print("working......");
print("*"*20);
print(issubclass(student,person));
print("*"*20);
print(issubclass(teacherMxin,student));
print("*"*20);
print(issubclass(person,object));
print("*"*20);
print(isinstance(s,student));
print("*"*20);
print(hasattr(s,"name"));
print("*"*20);
print(dir(person),end="\n");
print("*"*20);
print(dir(s),end=" ");

