# Modify the program above using a while loop so it prints out all of the factorial values that are 
# less than 2 billion.

f=n = 1
while f < 2000000000:
    a=print(f"{n} != {f}")
    n += 1
    f *= (n or 1)
   