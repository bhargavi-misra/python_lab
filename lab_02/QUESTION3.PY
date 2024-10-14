elements = []
for i in range(20):
    num = float(input(f"Enter element {i + 1}: "))
    elements.append(num)

mean = sum(elements) / len(elements)

sorted_elements = sorted(elements)
mid = len(sorted_elements) // 2
if len(sorted_elements) % 2 == 0:
    median = (sorted_elements[mid - 1] + sorted_elements[mid]) / 2
else:
    median = sorted_elements[mid]

mode = max(set(elements), key=elements.count)

slices = [elements[i:i + 4] for i in range(0, len(elements), 4)]

even_list = []
odd_list = []

for i in range(len(slices)):
    if i % 2 == 0:
        even_list.extend(slices[i])
    else:
        odd_list.extend(slices[i])

merged_list = even_list + odd_list

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Sliced lists: {slices}")
print(f"Merged even and odd lists: {merged_list}")
