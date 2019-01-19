#Find the Smallest Divisor of an Integer
'''
n=int(input("Enter an Integer: "))

a=[]

for i in range(2,n+1):
    if(n%i==0):
        a.append(i)

a.sort()
print("Smallest Diviser is: ",a[0])
'''
#Find the Smallest Divisor of an Integer

n=int(input("Enter an Integer: "))

#a=[]

for i in range(2,n+1):
    if(n%i==0):
        break
print(i)
#a.sort()
#print("Smallest Diviser is: ",a[0])
