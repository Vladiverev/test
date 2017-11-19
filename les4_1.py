from time import time

new_list = [1, 2, 3, 4, 5, 6, 7, 8]
start_time = time()

print(start_time)
list_sum = 0
for elem in new_list:
    list_sum += elem

end_time = time()
print('Duration: {}'.format(end_time - start_time))
print('Sum: {}'.format(list_sum))

start_time = time()
new_sum = sum(new_list)
print(new_sum)