my_tuple = (1, 2, 3, (4, 5, 6, (7, 8, 9)))

# for value_1 in my_tuple:
#     if type(value_1) == int:
#         print(value_1)
#     else:
#         for value_2 in value_1:
#             if type(value_2) == int:
#                 print("\t", value_2)
#             else:
#                 for value_3 in value_2: 
#                     if type(value_3) == int:
#                         print("\t\t", value_3)

my_new_tuple = my_tuple.__add__((10, 11, 12, (13, 14, 15)))
print(my_new_tuple)
