'''this code will generate a text file with PRN list with student name
create a menu driven program
1. add student
2. remove student
3. show list of students
4. generate file 

'''
student_dict={}

def add_student():
    #creating an empty list
    
    #asking for prn details
    prn_list=int(input("Enter your PRN: "))
    std_name=input("Enter your name: ")
    #adding the prn_details to the dictionary
    student_dict[prn_list] = std_name
    return None

def remove_student():
    #this function will remove the student from the list
    del_prn=int(input("Enter the PRN no: "))
    del student_dict[del_prn]
    print(f"{del_prn} has been removed successfully.")

def show_students():
    print(student_dict)

def generate_list():
    try:
        write_file=open("students.txt","w")
        write_file.write(str(student_dict))
        write_file.close()

    except FileNotFoundError:
        print("File do not exist!!")


while(True):
    print("Welcome to student list generator!!")
    print("1. Add student")
    print("2. Remove student")
    print("3. Show student list")
    print("4. Generate student list")
    print("5. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        add_student()
    elif ch==2:
        remove_student()
    
    elif ch==3:
        show_students()
    
    elif ch==4:
        generate_list()
    
    elif ch==5:
        break
    
    else:
        print("Wrong option!!")
    