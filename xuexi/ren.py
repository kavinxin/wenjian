class ren1():
    def __init__(self,name,age,date):
        self.name=name.upper();
        self.age=age;
        self.date=date;

    def say(self):
        print("my nam is {0}".format(self.name));
        print("my age is {0}".format(self.age));
        print("my date is {0}".format(self.date));

if __name__=="__main__":
    print("请执行我！");