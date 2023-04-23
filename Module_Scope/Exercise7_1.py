# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

try:    
    user_input=int(input("Enter the key: "))

    my_dict= {1:"red",2:"Blue",3:"orange"}
    key=my_dict[user_input]
    print(key)
    
except KeyError:
        print ("color not present")
finally :
        print ("This is finally block ")


# ERROR:
# Enter the key: 4
# color not present     
# This is finally block 
# PS E:\Python>

