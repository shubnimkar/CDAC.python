# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 

class Person():

    def __init__(self,name, place_of_residence):
        self.name=name
        self.place_of_residence=place_of_residence
    
    def disp_person(self):
        print("Your Name: ",self.name)
        print("Your Place of Residence: ",self.place_of_residence)

class Sister(Person):
    def __init__(self,name, place_of_residence,exam_subjects):
        super().__init__(name, place_of_residence)
        self.exam_subjects=exam_subjects

    def disp_sister(self):
        print("Your Exam Subjects: ",self.exam_subjects)

class Uncle(Sister):
    def __init__(self,name, place_of_residence, exam_subjects,business):
        super().__init__(name, place_of_residence, exam_subjects)
        self.business=business

    def disp_Uncle(self):    
        print("Your Business: ",self.business)

def main():

    Final=Uncle(name, place_of_residence, exam_subjects,business)
    print(type(Final))

    Final.disp_person()
    Final.disp_sister()
    Final.disp_Uncle()

name= input("Enter Your Name: ")
place_of_residence= input("Enter Your Place of residence: ")
exam_subjects=input("Enter Your Exam Subjects: ")
business=input("Enter Your Business: ")
main()