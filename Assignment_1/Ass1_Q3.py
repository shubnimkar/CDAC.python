'''Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console'''


#New salary – Old Salary) / Old Salary * 100 = Hike percentage. 


Name='Gaurav'
Existing_salary = 900
raise_salary_percentage = int(input("Enter the raise percentage = "))
raised_salary = (raise_salary_percentage*Existing_salary+ 100*Existing_salary)/100
print("Revised salary = ", raised_salary)

