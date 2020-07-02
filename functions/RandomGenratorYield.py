def cumtomgen(x,y):
    while x<y:
        yield x
        x+=1


result = cumtomgen(10,78)

for i in result:print(i)