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
raise_salary_percentage = float(input("Enter the raise percentage = "))
print("Revised salary = ", salary(raise_salary_percentage))

