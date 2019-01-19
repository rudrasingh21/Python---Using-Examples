n = int(input("Enter number of element: "))

a=[]

for i in range(0,n):
    b = int(input("Enter "+str( i+1 )+" element: "))
    a.append(b)
a.sort()
print("Second Largest Element is: ",a[n-2])
print("Smallest Number is : ",a[0])
