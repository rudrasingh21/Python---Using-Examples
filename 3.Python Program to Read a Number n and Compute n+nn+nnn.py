#Python Program to Read a Number  n and Compute n+nn+nnn3

n = int(input("Enter number to compute: "))

t = str(n)

t1 = t+t

t2 = t+t+t

print(n+n)
print(str(n)+str(n))

t = n
t1=n+n
t2=n+n+n
print(t)
print(t1)
print(t2)



'''
Output:-
Enter number to compute: 1
Clubbing like n+nn+nnn is:  111111
Sum like n+nn+nnn is:  123
'''