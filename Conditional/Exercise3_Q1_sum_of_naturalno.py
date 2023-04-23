# # Solve the following using either while/do while loops
# 1) Take a number from the user and print sum from 1 to that number
summ = 0
num = int(input("Enter the number: "))

while (num > 0):
    summ += num
    num -= 1

print('the sum', summ)
