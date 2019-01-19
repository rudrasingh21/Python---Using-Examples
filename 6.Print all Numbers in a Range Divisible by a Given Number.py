#Print all Numbers in a Range Divisible by a Given Number

Lower_Range = int(input("Enter Lower Range: "))
Upper_Range = int(input("Enter Upper Range: "))
Divser = int(input("Enter Divser: "))

for i in range(Lower_Range,Upper_Range+1):
    if(i%Divser==0):
        print("Number: " + str(i) + " is devisable.")
