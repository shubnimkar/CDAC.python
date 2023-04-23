class negative_number_error(Exception):
    pass

class positive_number_error(Exception):
    pass

class homogenous_list_error(Exception):
    pass

"""These lines define three custom exception classes that 
will be raised later in the program if certain conditions are met."""


def create_positive_numbered_list(lst):
    while True:
        try:
            n = int(input("Enter number of elements in the list: "))
            if n < 0:
                raise negative_number_error
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    lst.clear()
    for i in range(n):
        while True:
            try:
                num = int(input(f"Enter element {i+1}: "))
                if num < 0:
                    raise positive_number_error
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        lst.append(num)

"""This function prompts the user to enter the number of elements they want in a list, and 
then populates the list with positive integers. It handles two custom exceptions negative_number_error and 
positive_number_error if the user enters a negative or positive number respectively. 
It also handles ValueError if the user enters an invalid input."""

def create_negative_numbered_list(lst):
    while True:
        try:
            n = int(input("Enter number of elements in the list: "))
            if n < 0:
                raise negative_number_error
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    lst.clear()
    for i in range(n):
        while True:
            try:
                num = int(input(f"Enter element {i+1}: "))
                if num >= 0:
                    raise negative_number_error
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a negative integer.")
        lst.append(num)

"""This function is similar to the previous one, but it populates the list with negative integers instead."""

def create_heterogenous_list(lst):
    lst.clear()
    while True:
        elem = input("Enter an element (type 'stop' to stop): ")
        if elem == 'stop':
            break
        lst.append(elem)

"""This function prompts the user to enter elements for a list until they enter the word "stop". 
It populates the list with heterogenous elements (i.e., elements of any data type)."""

def find_an_element(lst):
    elem = input("Enter an element to search for: ")
    if elem in lst:
        print(f"Element '{elem}' found in the list.")
    else:
        print(f"Element '{elem}' not found in the list.")

"""This function prompts the user to enter an element and checks if it is present in the list."""

def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Create a heterogenous list ")
            print("4) Check if the element is present in the list ")
            print("5) Refresh the program to start with blank lists")
            print("6) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_positive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                create_heterogenous_list(my_het_list3)
            elif choice ==4:
                print("Lists created are as below \n ----------------------")
                print(f"1 : {my_int_list1}")
                print(f"2 : {my_int_list2}")
                print(f"3 : {my_het_list3}")
                
                while True:
                    check =int(input("Which of the below list you would want to search from "))
                    
                    if  check == 1:
                        find_an_element(my_int_list1)
                        break
                    elif check == 2:
                        find_an_element(my_int_list2)
                        break
                    elif check ==3:
                        find_an_element(my_het_list3)    
                        break
                    else:
                        print("Please choose something from the above")
            elif choice ==5:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==6:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except homogenous_list_error:    
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
            
my_exception_store()  

