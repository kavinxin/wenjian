stm= lambda x:x*100;
stm(100);
print(stm(100));
print("-"*50);
stm1= lambda x,y,z :x+y+z;
print(stm1(1,2,3));
print("-"*50);
def funa(n):
    return n*100;
def funb(n):
    return funa(n)*3;
print(funb(100));
print("-"*50);
def func(n,f):
    return f(n)*3;
print(func(3,funa));
l1=[1,2,3,4,5]

print("-"*50);
def func(n):
    return n*100;
fund=func;
print(fund(3));
print("-"*50);
def fune(n):
    return func(n)*200;
print(fune(2));
print("-"*50);
stm2=lambda x,y:x*y;
print(stm2(10,20));
print("-"*50);
def funf(n,f):
    return f(n)*3;
print(funf(2,func));




