# keys_list = ['Name', 'Age', 'Gender', 'Country']
# values_list = ['Adam', 48, 'Male', 'United States']
# print(f"Dictionary: {dict(zip(keys_list, values_list))}")


# def lucky_student(final_student_list,lucky_student_list):
#     is_append = 'N'
#     while(is_append == 'N'):
#         lucky_student_rollno = final_student_list[ random.randint(1,39)]
#         if lucky_student_rollno not in lucky_student_list:
#             lucky_student_list.append(lucky_student_rollno)
#             print(f"Congratulations {lucky_student_rollno} , Show is all yours !!! ")
#           is_append = 'Y'
        
# import random
# lucky_student_list = []
# final_student_list = random.randrange(1,16) + random.randrange(31,57)
# print(final_student_list)

# while(True):
#     lucky_student(final_student_list,lucky_student_list)
#     choice = input("Press Y to exit ").upper()
#     if choice == 'Y':
#         break


    # sample_dict = {
    #     'Physics': 82,
    #     'Math': 65,
    #     'history': 75
    # }
    # print(min(sample_dict, sample_dict.keys()))

# def append_middle(s1, s2):
#     print("Original Strings are", s1, s2)
#     mi = int(len(s1) / 2)
#     x = s1[:mi:]
#     x = x + s2
#     x = x + s1[mi:]
#     print("After appending new string in middle:", x)
# append_middle("Ault", "Kelly")

# str1="Ault"
# str2="Kelly"
# print(f'{str1[0:2]}{str2}{str1[2:4]}')

