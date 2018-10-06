import  time
with open(r"test.txt",'r') as f:
    strline=f.readline();
    while strline:
        print(strline);
        strline=f.readline();

print("*"*45);
with open(r"test.txt","r") as f:
    l=list(f);
    for line in l:
        print(line);

print("*"*45);

with open(r"test.txt", 'r')as f:
    re=f.read(36);
    print(len(re));
    print("@"*10);
    print(re);

print("*"*45);

with open(r"test.txt",'r')as f:
    f.seek(6,0);
    strp=f.read();
    print(strp);

print("*"*45);

with open(r"test.txt",'r')as f:
    str2=f.read(5);
    while str2:
        print(str2);
        time.sleep(5);
        str2=f.read(5);

print("*"*45);

with open(r"test.txt",'r')as f:
    con=f.read(5);
    point=f.tell();

    while con:
        print(con);
        print(point);

        con=f.read(5);
        point=f.tell();


