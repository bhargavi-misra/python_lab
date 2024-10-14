list1 = [1, 2, 3]
list2 = [4, 5, 6]

added = list(map(lambda x, y: x + y, list1, list2))
difference = list(map(lambda x, y: x - y, list1, list2))

print("Added:", added)
print("Difference:", difference)
