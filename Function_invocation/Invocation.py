#Accept two numbers from the user and print using functions
# Accept two numbers from the user and print 
  #   a) addition 
  #   b) first number squared 2 
  #   c) first number raised to number second number
    
from Calling_function import addition,square,raised
a=int(input('Enter the value of number 1: '))
b=int(input('Enter the value of number 2: '))
print ('The Sum is',addition(a,b))
print ('the Square is',square(a))
print ('A raised to B is',raised(a,b))


#############################################################################################################################################################################
#Accept String from user and output upper case of the input string using functions


from Calling_function import my_upper
str = input('Enter the sentence to convert into uppercase: ')
print(my_upper(str))


#############################################################################################################################################################################
'''Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console using function'''


from Calling_function import salary

raise_salary_percentage = float(input("Enter the raise percentage = "))
print("Revised salary = ",salary(raise_salary_percentage))



#############################################################################################################################################################################
'''Get the height from the user in cms and display the user height back to console
in foot/feet and inches using functions'''


from Calling_function import height
height_cms = float(input ('Enter the height in cms= '))
height(height_cms)


#############################################################################################################################################################################   
#Get the no of the dollars from the user apply the conversion of 1 dollar = 82 rupees and print the amount to the console in rupees using fucntions
    
from Calling_function import convert
    
dollars = int(input("Enter Number of Dollars: "))
print(f"In Dollars = {dollars} $")
convert(dollars)

#############################################################################################################################################################################
#Take the source, destination, fare in INR, discount_rate percentage from the user and display the string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%" using functions


from Calling_function import conj


sr=input("Enter the name of Source: ")
dest=input("Enter the name of Destination: ")
fr=float(input("Enter the fare: "))
disc=float(input("Enter the Discount percentage: "))
conj(sr,dest,fr,disc)


#############################################################################################################################################################################
