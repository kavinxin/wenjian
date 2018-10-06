import time
import pickle
with open(r"test.txt",'a') as f:
    f.writelines("生活不只眼前的苟且！");
    f.writelines("\n");
    f.writelines("还有远方的枸杞！");


print("*"*45);

with open(r"test.txt",'r')as f:
    con=f.read();
    print(con);

print("*"*45);

with open(r"test.txt",'a')as f:
    f.write("精灵岂是池中物！");

print("*"*45);

with open(r"test.txt",'r')as f:
    con=f.read(5);
    point=f.tell();

    while con:
        print(con);
        print(point);
        time.sleep(0);
        con=f.read(5);
        point=f.tell();

print("*"*45);

with open(r"test2.txt",'wb')as f:
    age=19;
    pickle.dump(age,f);

print("*"*45);

with open(r"test2.txt",'rb')as f:
    con=pickle.load(f);
    print(con);


print("*"*45);

a=["kavin","love","zhangya",["xin","hai"]];
with open(r"test2.txt",'wb')as f:
    pickle.dump(a,f);

print("*"*45);
with open(r"test2.txt",'rb')as f:
    con=pickle.load(f);
    print(con);


