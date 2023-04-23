#Python program to interchange first and last elements in a list
my_list=input("Enter the comma seperated list: ").split(",")
print("Your Entered List :",my_list)
# size=len(my_list)
# temp=my_list[0]
# my_list[0]=my_list[size-1]
#my_list[size-1]=temp
print("Swapped List :",my_list)

#Python program to swap two elements in a list

my_list[1],my_list[2]=my_list[2],my_list[1]
print(my_list)