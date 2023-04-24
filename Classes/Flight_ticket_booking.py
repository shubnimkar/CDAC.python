# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 
import random
import string

Cities=["New Delhi","Mumbai",'Chennai','Bangalore','Vasco da Gama','Kolkata','Hyderabad','Kochi','Thiruvananthapuram','Ahmedabad','Jaipur','Pune','Bangalore','Amritsar','Vadodara','Mangalore','Varanasi','Bhubaneswar','Guwahati','Visakhapatnam','Calicut','Hyderabad','Chandigarh','Coimbatore','Jodhpur','Madurai','Indore','Lucknow','Patna','Leh','Nagpur','Port Blair','Siliguri','Udaipur','Srinagar']
dep=random.choice(Cities)
arr=random.choice(Cities)
fno=random.randrange(1,500)
x=int(random.randrange(1,30))
y=chr(random.randint(ord('A'), ord('F')))
seat=(f"{x}{y}")

class ticket_booking():
    
    #Name_of_airlines="Jet Blue"
    
    def __init__(self,my_name,dp_city,ar_city,flightno,seat):

        self.name=my_name
        self.Dep_city=dp_city
        self.Arr_city=ar_city
        self.flight_number=flightno
        self.seat_assignment=seat

    def display_object_details(self):
        print("Name of Passenger: ",self.name)
        print("Departure City: ",self.Dep_city)
        print("Arrival City: ",self.Arr_city)
        print("flight Number: JB",self.flight_number)
        print("Seat Number: ",self.seat_assignment)
       
        
def main():

    booking=ticket_booking(name,dep,arr,fno,seat)
    print(type(booking))
    print(f"    Welcome to JET BLUE   ")
    #print(f"    Welcome to {booking.Name_of_airlines}   ")
    
    booking.display_object_details()
    

name=input("Enter Name: ")
#dep=input("Enter Departure City: ")
#arr=input("Enter Arrival City: ")
#fno=input("Enter Flight No: ")
#seat=input("Enter Seat No: ")
main()