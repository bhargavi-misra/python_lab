num_rows = 5
triangle = []

for row in range(num_rows):
    current_row = [1] * (row + 1)
    for col in range(1, row):
        current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    triangle.append(current_row)

for row in triangle:
    line = ""
    for num in row:
        line += str(num) + " "
    print(line.center(len(triangle[-1]) * 3))
