new_list = [1, 2, 3, 4, 5, 6, 7, 8]

another_one_list = []
for elem in new_list:
    another_one_list.append(elem * 3)

print(another_one_list)


generated_list = [x * 3 for x in new_list if x%2 == 0]
print(type(generated_list))
print(generated_list)