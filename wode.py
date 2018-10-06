
# -*- coding: UTF-8 -*-#!汉诺塔的实现
def hano(n,a,b,c):
    if(n==1):
        print(a,"---->",c);
        return None;
    if(n==2):
        print(a,"---->",b);
        print(a,"---->",c);
        print(b,"---->",c);
        return None;
    hano(n-1,a,b,c);
    print(a,"---->",c);
    hano(n-1,b,a,c);
a="A";
b="B";
c="C";























































