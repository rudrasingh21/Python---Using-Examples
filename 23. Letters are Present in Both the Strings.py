# Letters are Present in Both the Strings

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

a = list(set(s1)|set(s2))

print("Letters are Present in Both the Strings: ",a)