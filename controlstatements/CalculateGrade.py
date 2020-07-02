m,p,c = [int(x) for x in input("Enter the marks un three subjects ").split()]

if(m<35):
    print("Fail in Maths with %d marks " %m)
elif(p<35):
    print("Fail in Physics with %d marks " %p)
elif(c<35):
    print("Fail in Chemistry with %d marks " %c)

if(m<35 or p<35 or c<35):
    print("Grade can't be calculated")
else:
    average = int((m+p+c)/3)

    if(average<=59):
        print("You got C grade")
    elif(average<=69):
        print("You got B grade")
    else:print("You got A Grade")
