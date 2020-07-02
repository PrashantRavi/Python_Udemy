a =[2,4,6,8]
b=[1,2,3,4]

res =[]
# for i in a:
#     if i in b:
#         res.append(i)

res = [i for i in a if i in b]

print(res)