class Employee():
    #class variable 
    department_name=input("Enter name of Department: ")
    #class method 
    @classmethod
    def new_department(cls,my_department_name):
         cls.dept_name=my_department_name

    # instance variables 
    def __init__(self,my_name,my_empid,my_empsalary,my_mgrid):
        self.name=my_name
        self.emp_id = my_empid
        self.emp_salary = my_empsalary
        self.mgr_id = my_mgrid

    def display_object_details(self):
         print(f'Name:{self.name}\nEmployee ID :{self.emp_id} \nSalary :{self.emp_salary} \nManager ID :{self.mgr_id} ')

    # static method
    @staticmethod
    def field_expertise():
        print( "just displays some expertise for all my employees")

def main():
    employee=Employee(name1,eid,sal,mgid)
    print(type(employee))
    employee.display_object_details()
    print("\n----------------Class variable printed---------------------\n")
    Employee.new_department("aa")
    print(f"Before Department_name: {employee.department_name}")
    print(f"After Department_name: {Employee.new_department()}")

name1=input("Enter Employee name: ")
eid=input("Enter Employee ID: ")
sal=input("Enter Salary: ")
mgid=input("Enter manager id: ")
main()

# 1) create an object employee(100,1000,1) 
# 2) display the employee object