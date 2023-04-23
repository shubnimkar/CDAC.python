# 3) Take a number from the user and print all Odd numbers from 1 to that number
initial_value = 1
end_value = int(input("Enter the number: "))
for num in range(initial_value, end_value+1):
    if num % 2 != 0:
        print(num)
