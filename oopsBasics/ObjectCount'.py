class ObjectCounter:
    NumberOfOnject =0

    def __init__(self):
        ObjectCounter.NumberOfOnject+=1

    @staticmethod
    def displayCount():
        print(ObjectCounter.NumberOfOnject)

O1 = ObjectCounter()
o2 = ObjectCounter()

print(ObjectCounter.displayCount())