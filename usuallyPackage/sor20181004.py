a=[-12,-124,2,334,332,-123,338,4338];
al=sorted(a,key=abs,reverse=True);
print(al);
print("*"*45);
str2=["kavin","xin","tina","bill"];
print([sorted(str2,key=str.upper)]);
print("*"*45);
def fun1():
    def fun2():
        print("china");
        return "chinese!";
    return fun2();
p=fun1;
print(type(p));
print("*"*45);
print(p());
print("*"*45);
def funa(*args):
    def funb():
        rst=0;
        for x in args:
            rst+=x;
        return rst;
    return funb();
p3=funa(0,1,2,3);
print(p3);
p5=funa(100,200,300,400,500,600,700,800,999);
print(p5);





