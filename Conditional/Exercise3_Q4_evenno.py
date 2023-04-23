# 4) Take a number from the user and print all Even numbers from 1 to that number
initial_value = 1
end_value = int(input("Enter the number: "))
for num in range(initial_value, end_value):
    if num % 2 == 0:
        print(num)
