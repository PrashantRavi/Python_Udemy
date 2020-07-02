list =[3,5,224]
print(type(list))

b =bytes(list)
print((type(b)))

b1 = bytearray(list)
print(type(b1))

b1[2]=33
print(b1)