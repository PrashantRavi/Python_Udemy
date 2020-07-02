class Patient:

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setssn(self, ssn):
        self.ssn = ssn

    def getssn(self):
        return self.ssn

p = Patient()
p.setId(2)
p.setname("Rohit")
p.setssn(2312312)

print(p.getId())
print(p.getname())
print(p.getssn())