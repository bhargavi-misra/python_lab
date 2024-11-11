def process_list(input_list):
    input_list.append(100)
    input_list.sort()
    return input_list

my_list = [5, 3, 8, 1]
result = process_list(my_list)
print(result)
