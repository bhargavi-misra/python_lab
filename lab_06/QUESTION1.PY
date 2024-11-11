my_list = [3, 7, 2, 9, 5, 7, 10]

print("Length of the list:", len(my_list))

my_list.append(15)
print("List after append(15):", my_list)

my_list.extend([20, 25, 30])
print("List after extend([20, 25, 30]):", my_list)

my_list.insert(3, 100)
print("List after insert(3, 100):", my_list)

my_list.remove(7)
print("List after remove(7):", my_list)

popped_item = my_list.pop(2)
print(f"Item popped from index 2: {popped_item}")
print("List after pop():", my_list)

index_of_9 = my_list.index(9)
print("Index of 9:", index_of_9)

count_of_7 = my_list.count(7)
print("Count of 7 in the list:", count_of_7)

my_list.sort()
print("List after sort():", my_list)

my_list.reverse()
print("List after reverse():", my_list)

my_list_copy = my_list.copy()
print("Shallow copy of the list:", my_list_copy)

my_list.clear()
print("List after clear():", my_list)

my_list = [3, 7, 2, 9, 5]
total_sum = sum(my_list)
print("Sum of elements in the list:", total_sum)

min_value = min(my_list)
print("Minimum value in the list:", min_value)

max_value = max(my_list)
print("Maximum value in the list:", max_value)

squared_values = [x**2 for x in my_list if x % 2 == 0]
print("Squared values of even numbers:", squared_values)
