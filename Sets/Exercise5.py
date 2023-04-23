def my_set_store():
    print("\n Welcome to Our Set Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("	1: Union")
        print("	2: Intersection ")
        print("	3: A-B")
        print("	4: B-A")
        print("	5: Take a element from user and Display if that element is a member of set B ")
        print("	6: Display number of elements in the set A")
        print(" 7: Display number of elements in the set B")
        print("	8: Add an element taken from the user to the set A")
        print("	9: Add multiple elements taken from the user to the set A")
        print("	10: Remove an element taken from the user from set A")
        print(" 11: Exit")

        choice = int(input("Please enter your choice "))

        if choice   ==1:
            set_union=setA.union(setB)
            print(set_union) 
        elif choice ==2:
            set_intersection=setA.intersection(setB)
            print(set_intersection)
        elif choice ==3:
            set_minus=setA.difference(setB)
            print(set_minus)
        elif choice ==4:
            set_minus=setB.difference(setA)
            print(set_minus)
        elif choice ==5:
            is_member_of_set=input("Enter the element to find: ") 
            print(f"Element{is_member_of_set} is present(True/False): { is_member_of_set in setB }")
        elif choice ==6:
            print("No of elements in Set A:",len(setA))
        elif choice ==7:
            print("No of elements in Set B:",len(setB))
        elif choice ==8:
            element=input("Enter the element to add in setA: ")
            setA.add(element)
            print("Updated Set:",setA)
        elif choice ==9:
            elements=set(input("Please enter comma seperated elements for the set A: ").split(","))
            setA.update(elements)
            print("Updated Set:",setA)
        elif choice ==10:
            element=input("Insert the element to remove from setA: ")
            setA.discard(element)
            print(setA)
        elif choice ==11:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")  
                    
setA=set(input("Please enter comma seperated elements for the set A: ").split(","))
setB=set(input("Please enter comma seperated elements for the set B: ").split(","))			
my_set_store()			