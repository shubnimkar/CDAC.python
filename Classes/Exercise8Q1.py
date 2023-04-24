class Employee():
    # class variable 
    department_name="HPCSA"
    # class method 
    @classmethod
    def departmentt_name(cls,my_department_name):
         cls.dept_name=my_department_name

    # instance variables 
    def __init__(self,my_empid,my_empsalary,my_mgrid):
        self.emp_id = my_empid
        self.emp_salary = my_empsalary
        self.mgr_id = my_mgrid

    def display_object_details(self):
         print(f'Employee ID :{self.emp_id} \nSalary :{self.emp_salary} \nManager ID :{self.mgr_id} ')

    # static method
    @staticmethod
    def field_expertise():
        print( "just displays some expertise for all my employees")

def main():
    employee=Employee(100,1000,1)
    print(type(employee))
    employee.display_object_details()
    print("----------------Class variable printed--------------------- ")
    print(f"Before Department_name: {employee.department_name}")
    Employee.departmentt_name("PG-DAC")
    print(f"After Department_name: {employee.dept_name}")
  

main()

# 1) create an object employee(100,1000,1) 
# 2) display the employee object