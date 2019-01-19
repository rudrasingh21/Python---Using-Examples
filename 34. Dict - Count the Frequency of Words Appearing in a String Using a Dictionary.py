#Count the Frequency of Words Appearing in a String Using a Dictionary

My_String = input("Enter your string: ")

l = []
l = My_String.split()

for i in l:
    WF=l.count(i)

print(WF)
#print(dict(zip(l,WF)))
'''

test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))
'''