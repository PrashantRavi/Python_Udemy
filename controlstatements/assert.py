# x = int(input("Enter a number greater than 10 "))
#
# assert x>10 , "Wrong number entered"
#
# print("U entered ",x)


x = int(input("Enter a number "))

primeflag =True

for i in range(2,x-1):
    if(x%i==0):
        primeflag=False
        break

if(primeflag):
    print("Number is Prime")
else:print("Not a prime number")