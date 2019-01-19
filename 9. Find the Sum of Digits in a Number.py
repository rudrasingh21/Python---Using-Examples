# Find the Sum of Digits in a Number

n = int(input("Enter a number: "))

total = 0

while(n>0):
    num=n%10
    total=total+num
    n=n//10

print("Total Sum of digits: ",total)