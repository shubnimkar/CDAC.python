# 3) Create program that takes age of the user as input and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)
class my_exception(Exception):
     pass

try:
    inp = int(input("Please enter your age:"))*365
    if ( inp > 100001):
        raise my_exception
    else:
        print(f"You have lived for {inp} days ")
except my_exception:
    print(f"you lived for so long {inp} days , may be you will die soon)")