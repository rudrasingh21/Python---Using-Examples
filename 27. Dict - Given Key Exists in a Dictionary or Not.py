# Given Key Exist in a Dictionary or Not

d={'A':1,'B':2,'C':3}

k = input("Enter Key which you want to search:- ")

if k in d.keys():
    print("Value is present and value for the Key is:- ", d[k])
else:
    print("Key is not present")
