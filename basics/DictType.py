dict1 ={1:"ravi",2:"Monu",3:"Anki"}
print(type(dict1))
print(dict1)


print(dict1.items())

k =dict1.keys()

for i in k:print(i)

v = dict1.values()
for i in v:print(i)


del dict1[1]
print(dict1)