#Check Common Letters in Two Input Strings

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

a = list(set(s1) & set(s2))

print("Common Letter in two string: ",a)