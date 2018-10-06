#协程的使用案例

def fun(a):
    print("-----1");
    b=yield a;
    print("------2",a,b);
    c=yield a+b;
    print("------3",a,b,c);

def main():
    f=fun(3);
    aa=next(f);
    print(aa);
    print("*"*10);
    bb=f.send(4);
    print(bb);
    print("*"*10);
    cc=f.send(5);
    print(cc);



if __name__=='__main__':
    main();


