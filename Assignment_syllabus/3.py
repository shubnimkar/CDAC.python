# # Write a program that asks the user how many days are in a particular month, and what day of 
# # the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for 
# # that month. For example, here is the output for a 30-day month that begins on day 4 (Thursday):
# # S M T W T F S
# #  1 2 3
# # 4 5 6 7 8 9 10
# # 11 12 13 14 15 16 17 
# # 18 19 20 21 22 23 24 
# # 25 26 27 28 29 30 

# month = input("Enter the month('January', ...,'December'): ")
# day = input("Enter the start day ('Monday', ..., 'Sunday'): ")
# n = 1

# if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
#         x = 31
# elif month == "February":
#         x = 28
# else:
#         x = 30
# print(month)
# print("Mo Tu We Th Fr Sa Su")
# if (day == "Sunday"):
#         print("                  ", end='')
# for i in range (1, 7):
#         for j in range (1, 8):
#                 while n != x+1:
#                         print('%2s' % n, end=' ')
#                         n = n + 1
#                         break
#         print()

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))