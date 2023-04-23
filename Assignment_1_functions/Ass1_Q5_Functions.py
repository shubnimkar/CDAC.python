#Get the no of the dollars from the user apply the conversion of 1 dollar = 82 rupees and print the amount to the console in rupees using fucntions



def convert(dollars):
    in_rupees = dollars*82
    print (f'Conversion in Rupees {in_rupees} ₹')
    
dollars = int(input("Enter Number of Dollars: "))
print(f"In Dollars = {dollars} $")
convert(dollars)

