import random
import string

x=int(random.randrange(1,30))
y=chr(random.randint(ord('A'), ord('F')))
#y=(random. choice(string.ascii_letters))
print(f"{x}{y}")