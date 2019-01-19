#Put Even and Odd elements in a List into Two Different Lists

n = int(input("Enter Number of Elements: "))

Even=[]
odd=[]

for i in range(0,n):
    Num = int(input("Enter number: "))
    if(Num%2==0):
        Even.append(Num)
    else:
        odd.append(Num)
print("Even numbers are: ",Even)
print("Odd numbers are: ",odd)

#Other Method:-

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)