list_a = ['Orange', 'Yellow', 'Green', 'Brown']
list_b = [1, 2, 3, 4]

# print(list_a[1])
# print(list_b[1:3])

# for value in list_a[1:3]:
#     print(value)

for value_1, value_2 in zip(list_a, list_b):
    print(value_1, "\t", value_2)