#Map Two Lists into a Dictionary

k = []
v = []

n = int(input("Enter number of elements in the dictionary : "))

print("Adding Keys in Dictionary:")
for i in range(1,n+1):
    ele = input("Enter Key " + str(i) + " for Dictionary:- ")
    k.append(ele)

print("Adding Values in Dictionary:")
for i in range(1,n+1):
    ele = input("Enter Value " + str(i) + " for Dictionary:- ")
    v.append(ele)

d = dict(zip(k,v))

print("Dictionary which we have is: ",d)