class Person():


    def __init__(self,Name,Gender):
        self.my_name=Name
        self.my_gender=Gender
        
    def display(self):
        print("Your Name: ",self.my_name)
        print("Your Gender: ",self.my_gender)
    
class Age(Person):
     
     def __init__(self, Name, Gender,age):
        super().__init__(Name, Gender)
        self.my_age=age
    
     def displays(self):
        print("Your age: ",self.my_age)
        

def main():
        Details=Age(name,gender,age)
        print(type(Details))
        Details.display()
        Details.displays()
name=input("Enter Your Name: ",)
gender=input("Enter Your gender: ")
age=input("Enter Your Age: ")

main()