#Count the Number of Vowels Present in a String using Sets

s = input("Enter String:- ")

vowels = set("aeiou")

count = 0

for letters in s:
    if letters in vowels:
        count = count + 1
print("Count of vowels is : ", count)