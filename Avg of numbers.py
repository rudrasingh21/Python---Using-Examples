n = int(input("Enter number of Element you want to enter: "))
a = []

for i in range(0,n):
    elem = int(input("Enter element: "))
    a.append(elem)

avg = sum(a)/n

print("Avg of entered numbers: ",avg)