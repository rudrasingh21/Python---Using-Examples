#Add a Key-Value Pair to the Dictionary

n = int(input("Enter number of Element you want in Dictionary:- "))

d = {}

for i in range(1,n+1):
    Key = input("Enter Key : ")
    Value = input("Enter Value : ")
    d.update({Key:Value})
print("Updated Dictonary is: ",d)