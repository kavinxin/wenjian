import xuexi
l=[1,2,3,4,5];
print(len(l));
for x in l:
    print(x,end="\n");
tina=1
try:
    while tina==1:

         num=int(input("please input your number"));
         p=(100/num);
         print("The result is {0}".format(p));

except ZeroDivisionError as e:
    print(e);
    print("please input the right number!");
    exit();

except NameError as e:
    print("the name is error");
    print(e);
    exit();

except AttributeError as e:
    print("the attribue is erro!");
    print(e);
    exit();

except ValueError as e:
    print(" pleae input the number!");
    print(e);
    exit();

except InterruptedError as e:
    print("please input the number!");
    print(e);
    exit();

except Exception as e:
    print("I don't know is error!");
    print(e);
    exit();

else:
    print("No exception!")

finally:
    print("This conculate is over!");


print("*"*30);






