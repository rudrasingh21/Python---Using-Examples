# Displays which Letters are in the First String but not in the Second

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

a = list(set(s1) - set(s2))

print("Letters which are in first string but not in second: ",a)