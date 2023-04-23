'''Get the height from the user in cms and display the user height back to console
in foot/feet and inches'''


height_cms = float(input ('Enter the height in cms= '))
print(f"Height in cms = {height_cms} cms")

height_in_feet = int(height_cms//30.48)
height_in_inches = int((height_cms%30.48)/2.54)

print(f"The height is {(height_in_feet)} feet {height_in_inches} inches")