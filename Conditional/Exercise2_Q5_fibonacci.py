# 5)Take a number from the user and print fibonacci sequence till that number

End_number = int(input("ENTER THE END VALUE: "))
# Initial Value:
num_1, num_2 = -1, 1
#count = 0

while True:
    num_3 = num_1+num_2
    if num_3>End_number:
        break
    print(num_3,end=" ")
    num_1 = num_2
    num_2 = num_3
    #count += 1
    