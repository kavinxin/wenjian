#协程的简易案例

def cao():
    print("start----->");
    x=yield ;
    print("over------>",x);

def main():
    c=cao();
    next(c);
    c.send('结束！');

if __name__=='__main__':
    main();