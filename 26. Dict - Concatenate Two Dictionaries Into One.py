#Concatenate Two Dictionaries Into One
n1 = int(input("Enter number of Element you want in Dictionary1:- "))
n2 = int(input("Enter number of Element you want in Dictionary2:- "))

d1 = {}
d2 = {}

print("Values for Dictionary1:-")
for i in range(1,n1+1):
    Key = input("Enter Key " + str(i) + " :" )
    Value = int(input("Enter value " + str(i) + " :" ))
    d1.update({Key:Value})
#print("Dictionary1 is: ",d1)

print("Values for Dictionary2:-")
for i in range(1,n2+1):
    Key = input("Enter Key " + str(i) + " :"  )
    Value = int(input("Enter value " + str(i) + " :" ))
    d2.update({Key:Value})
#print("Dictionary2 is: ",d2)

print("Dictionary1 is: ",d1)
print("Dictionary2 is: ",d2)

d1.update(d2)
print("Concatinated Dictionary is: ",d1)


