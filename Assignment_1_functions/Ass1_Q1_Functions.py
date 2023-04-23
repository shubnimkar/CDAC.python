#Accept two numbers from the user and print using functions




  # Accept two numbers from the user and print 
    #a) addition 
    #b) first number squared 2 
    #c) first number raised to number second number


def addition(a,b):
    sum = a+b
    return sum

def square(a):
    square = a*a
    return square

def raised(a,b):
    raised = a**b
    return raised    
    

a=int(input('Enter the value of number 1: '))
b=int(input('Enter the value of number 2: '))
print ('The Sum is',addition(a,b))
print ('the Square is',square(a))
print ('A raised to B is',raised(a,b))


