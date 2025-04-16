a = int(input("Enter a value: "))
b = int(input("Enter the second value: "))
c = int(input("enter the third value: "))

avg = (a + b + c) / 3
print("The average is : ",avg)

if avg > a and avg > b and avg > c:
    print("%d is greater than %d and %d and %d" %(avg,a,b,c))
elif avg > a and avg > b:
    print("%d is greater than %d and %d" %(avg,a,b))
elif avg > a and avg > c:
    print("%d is greater than %d and %d" %(avg,a,c))
elif avg > b and avg > c:
    print("%d is greater than %d and %d" %(avg,b,c))
elif   avg > a:
    print("%d is just greater than %d " %(avg,a))
elif   avg > b:
    print("%d is just greater than %d " %(avg,b))
elif   avg > c:
    print("%d is just greater than %d " %(avg,c))
else:
    print("invalid output")


    
     
