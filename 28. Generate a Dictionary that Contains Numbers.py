#Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input("Enter Length of Dictionary:- "))

d = {i: i*i for i in range(1,n+1)}
print(d)


