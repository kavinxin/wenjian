import time
import collections
from collections import deque
from collections import defaultdict
from collections import Counter
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time",time.ctime());
        return f(*args,**kwargs);
    return wrapper();

@printTime
def hello():
    print("hello china!");
print("-"*45);
l1=["kavin","bill","tina"];
l2=[80,90,78];
z=zip(l1,l2);
for x in z :
    print(x,end="\n");
print("-"*45);
l2=[11,22,33,44,55];
p=enumerate(l2,start=1000);
l3=[x for x in p]
for i in l3:
    print(i);
print("-"*45);
print(l3);
print("-"*45);
Point=collections.namedtuple("point",["x","y"]);
p=Point(3,5);
print(p);
print(p.x);
print(p.y);
print(p[1]);
print(p[0]);
print("-"*45);
q=deque([1,2,3]);
print(q);
q.append(4)
print(q);
q.appendleft(-1);
print(q);
print("-"*45);
for x in q:
    print(x);
print("-"*45);
fun1=lambda :"kavin";
d1=defaultdict(fun1);
d1["one"]="tina";
d1["two"]="bill";
print(d1["one"]);
print(d1["three"]);
print("-"*45);
c=Counter("abcdefghabdxhgfabdchs");
print(c);




