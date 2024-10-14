integer_list = [1, 2, 3]
integer_tuple = (4, 5, 6)

combined = integer_list + list(integer_tuple)
string_list = list(map(str, combined))

print(string_list)
