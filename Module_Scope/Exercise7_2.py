# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 

#my_list=input("Enter the comma seperated values to enter: ").split(",")
try:
    my_list=1,2,3,4,5
    index=int(input("enter the index you want: "))
    print(my_list[index])
    
except IndexError:
        print ("Index not present")
finally :
        print ("This is last block ")


# ERROR:
# enter the index you want: 9
# Index not present  
# This is last block 
# PS E:\Python>      
