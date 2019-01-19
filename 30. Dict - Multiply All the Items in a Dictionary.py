#Multiply All the Items in a Dictionary
'''
d={'A':10,'B':10,'C':10}

k = 1

for i in d.values():        #d.values will take values from d
    k = k*i

print(k)
'''

#OR
d={'A':10,'B':10,'C':239}
tot=1
for i in d:     #d will take key from dict
    tot=tot*d[i]
print(tot)