class Course:

    def __init__(self,name,ratings):
        self.name = name
        self.ratings=ratings

    def average(self):
        noOfRatings = len(self.ratings)
        average =sum(self.ratings)/noOfRatings
        print("Average rating for ",self.name ," Is ",average)

c1 = Course("Java",[1,4,5,3])

print(c1.ratings)
print(c1.name)
c1.average()

c2 = Course("Java Web services",[8,8,8,8])

print(c2.name)
print(c2.ratings)

c2.average()