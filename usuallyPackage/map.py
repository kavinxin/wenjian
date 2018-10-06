from functools import reduce
li=[i for i in range(10)];
print(li);
l1=[x*10 for x in li];
print(l1);
print("-"*40);
def zuhe(n):
    return n*100;
l2=map(zuhe,li);
for i in l2:
    print(i,end="\n");
print("-"*40);
lb=[i for i in range(100)];
def add(x,y):
    return x + y;
result=reduce(add,lb);
print(result);
print("-"*40);
def isEven(n):
    if n % 2==0:
       return n;
p1=filter(isEven,li);
print([x for x in p1]);
print("-"*40);


