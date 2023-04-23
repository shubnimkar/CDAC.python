# 2) Take a number from the user and print all prime numbers from 1 to that number

start = 1
n = int(input("Enter the number:"))
for num in range(start, n+1):
    if (num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
