#Take the source, destination, fare in INR, discount_rate percentage from the user and display the string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
source=input("Enter the name of Source: ")
destination=input("Enter the name of Destination: ")
fare=int(input("Enter the fare: "))
discount=int(input("Enter the Discount percentage: "))
my_str= print(f"fare from {source} to {destination} is {fare- (fare*discount/100)} INR with discount of {discount}%")

