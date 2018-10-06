def hello(name):
    print("hi,{0},wellome to you!".format(name));

if __name__=="__main__":
   print("***"*10);
   name=input("please input your name:");
   hello(name=name);
   print("thanks ,{0}!".format(name));