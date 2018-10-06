from ren import ren1
class studen(ren1):
    def setName(self,name):
        self.name=name.upper();

    def getName(self,name):
        return  name;

    def setAge(self,age):
        self.age=int(age);

    def getAge(self,age):
        return age;

    def setDate(self,date):
        self.date=date;

    def getDate(self):
        return date;
