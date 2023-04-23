def my_cal(a,b):
    while True:
        choice=int(input ("Please select your choice: "))
        if choice==1:
           print(f'The sum= {a+b}')
        elif choice==2:
            print(f'The Square= {a*a}')
        elif choice==3:
            print(f'The Eponent={a**b}')
        elif choice==4:
            break
        else:
            print("Enter Valid Choice")
     
print("****************** MENU ************************\n1: Addition\n2: Square\n3: Exponentation\n4: Exit\n")
a,b=int(input("Enter first number: ")),int(input("Enter second number: "))
my_cal(a,b)