#Create a Dictionary with Key as First Character and Value as Words Starting with that Character

My_String = input("Enter String:- ")
l = My_String.split()
d = {}

for i in l:
    if(i[0] not in d.keys()):
        d[i[0]] = []
        d[i[0]].append(i)

    else:
        if (i not in d[i[0]]):
            d[i[0]].append(i)
for k, v in d.items():
        print(k, ":", v)


