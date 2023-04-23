def fizz_buzz():
    number = int(input("Enter a number to start with: "))
    while True:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
        play_again = input("Do you want to continue? (y/n)").lower()
        if play_again != 'y':
            break
        number += 1

fizz_buzz()
