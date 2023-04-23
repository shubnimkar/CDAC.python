'''Get the height from the user in cms and display the user height back to console
in foot/feet and inches using functions'''

def height(height_cms):
    
    height_in_feet = int(height_cms//30.48)
    height_in_inches = float((height_cms%30.48)/2.54)
    print(f'Your Height is: {height_in_feet} Feet {height_in_inches:.2f} Inches')
   
 

height_cms = float(input ('Enter the height in cms= '))
height(height_cms)
    
    
    
    
    

