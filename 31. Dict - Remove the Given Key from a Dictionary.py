#Remove the Given Key from a Dictionary

d = {'a':1,'b':2,'c':3,'d':4}

print("Enter Key from Dictionary Keys:- ",d.keys())

k = input("Enter key to delete:- ")

if k in d:
    del d[k]
    print("Updated Dictionary is:- ",d)

else:
    print("Key not found")

