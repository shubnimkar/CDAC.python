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

# Accept String from user and output upper case of the input string using functions

def my_upper(my_str):
    my_str1 = my_str.upper()
    return my_str1




'''Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console using function'''


#New salary – Old Salary) / Old Salary * 100 = Hike percentage. 

def salary(raise_salary_percentage):
    Name='Gaurav'
    Existing_salary = 900
    raised_salary = (raise_salary_percentage*Existing_salary+ 100*Existing_salary)/100
    return raised_salary 



'''Get the height from the user in cms and display the user height back to console
in foot/feet and inches using functions'''

def height(height_cms):
    
    height_in_feet = int(height_cms//30.48)
    height_in_inches = float((height_cms%30.48)/2.54)
    print(f'Your Height is: {height_in_feet} Feet {height_in_inches:.2f} Inches')
    
    
    
#Get the no of the dollars from the user apply the conversion of 1 dollar = 82 rupees and print the amount to the console in rupees using fucntions



def convert(dollars):
    in_rupees = dollars*82
    print (f'Conversion in Rupees {in_rupees} ₹')
    


#Take the source, destination, fare in INR, discount_rate percentage from the user and display the string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%" using functions

def conj(source,destination,fare,discount):
 sr= source
 dest= destination
 fr= fare- (fare*discount/100)
 dis= discount
 print(f"fare from {source} to {destination} is {fare} INR with discount of {discount}%")
