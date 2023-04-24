
class ticket_booking():
    Name_of_airlines="Pulse Air"
    
    def __init__(self,dp_city,ar_city,flightno,seat):
        self.Dep_city=dp_city
        self.Arr_city=ar_city
        self.flight_number=flightno
        self.seat_assignment=seat

    def display_object_details(self):
         print(f'Departure City: {self.Dep_city} \nArrival City: {self.Arr_city} \nFlight Number: {self.flight_number} \nSeat Number: {self.seat_assignment} ')

def main():
    
    booking=ticket_booking(dep,arr,fno,seat)
    print(f"    Welcome to {booking.Name_of_airlines}   ")
    print(type(booking))
    booking.display_object_details()
    print(f"{booking.Name_of_airlines}")

dep=input("Enter Departure City: ")
arr=input("Enter Arrival City: ")
fno=input("Enter Flight No: ")
seat=input("Enter Seat No: ")
main()