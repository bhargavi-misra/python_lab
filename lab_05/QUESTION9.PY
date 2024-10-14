integer_tuple = (10, 20, 30, 40, 50)
specific_indices = [0, 2, 4]
string_value = "100"

new_list = [integer_tuple[i] for i in specific_indices]
integer_value = int(string_value)

new_list.append(integer_value)

print(new_list)
