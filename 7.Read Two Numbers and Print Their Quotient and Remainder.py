#Read Two Numbers and Print Their Quotient and Remainder

first_num = int(input("Enter First Number : "))
second_num = int(input("Enter Second Number : "))

quotient = first_num//second_num
remainder = first_num%second_num

print("Quotient is : ",str(quotient) + " & Remainder is: ",str(remainder))