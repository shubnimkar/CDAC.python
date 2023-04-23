# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation

def my_addition(num_1,num_2):
    sum=num_1+num_2
    return sum
       
def my_square(num_1):
    square=num_1*num_1
    return square

def my_exponent(num_1,num_2):
    expo=num_1**num_2
    return expo

while True:
    print('1. Addition')
    print('2. Square')
    print('3. Exponent')
    print('4. Exit')
    
    choice=int(input('Enter your desired choice: '))

    if choice==1:
        num_1=int(input('Enter first number: '))
        num_2=int(input('Enter the second number: '))       
        print(f'The sum= {my_addition(num_1,num_2)}')
        
        
    
    elif choice==2:
        num_1=int(input('Enter the number: '))
        my_square(num_1)
        print(f'The square= {my_square(num_1)}')
  
    elif choice==3:
        num_1=int(input('Enter first number: '))
        num_2=int(input('Enter the second number: ')) 
        print(f'The exponent= {my_exponent(num_1,num_2)}')
        
    elif choice==4:
        break
    else:
        print('Enter Correct Option')