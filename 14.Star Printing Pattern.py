
n = int(input("Enter Number of Rows: "))
for i in range(0,n+1):
    print('' + i* '*')

'''
Output:-
 *
 **
 ***
 ****
 '''

#Inverted Star Pattern

n = int(input("Enter Number:- "))

for i in range(0,n+1):
    print(' ' + (n-i)*'*')
    #OR
    #print(i* ' ' + (n-i)*'*')

'''
Output:-
***
**
*

&

***
 **
  *
'''