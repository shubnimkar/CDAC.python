def my_list_store():
    print("\nWelcome to Our List Store !!! ")
    print("Please enter a list Comma seperated that you would want to perform Operation Upon")
    members = input('Enter the list:  \n').split(",")

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display number of elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7:  Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            list_display_members=len(members)
            print("Number of elements in list: ",list_display_members)
        elif choice ==2:
            list_add_element=input("Element to add in list: ")
            members.append(list_add_element)
            print("Updated list: ",members)
        elif choice ==3:
            new = input('Enter the new members to add:  \n').split(",")  
            members.extend(new)  
            print("Updated list: ",members)     
        elif choice ==4:
            list_remove_element=input("Enter the element to remove: ")
            members.remove(list_remove_element)
            print("Updated list: ",members) 
        elif choice ==5:
            members.pop()
            print("Updated list: ",members) 
        elif choice ==6:
            print("Third, fourth, fifth elements in list are: ",members[2:5])
        elif choice ==7:
             break
        else:
             print("Invalid Input , Please Try Again !!!!  ")
my_list_store()