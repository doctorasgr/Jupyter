number = int(input("Enter number: "))
flag = False
for j in range(2, number):
    if number%j == 0:
        flag = True
if flag == True:
    print("Number is not prime")
else:
    print("Number is prime")