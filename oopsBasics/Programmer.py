class Programmer:

    def setName(self,name):
        self.name =name

    def geName(self):
        return self.name

    def setSalary(self,salary):
        self.salary=salary

    def getSalary(self):
        return self.salary

    def setTech(self,tech):
        self.tech=tech

    def getTech(self):
        return self.tech


p1 = Programmer()

p1.setName("ravi")
p1.setSalary(1000)
p1.setTech(['java','python','ML'])

print(p1.geName())
print(p1.getSalary())
print(p1.getTech())