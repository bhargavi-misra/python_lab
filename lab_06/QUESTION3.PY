def cube_of_elements(*args):
    return [x**3 for x in args]

result = cube_of_elements(1, 2, 3, 4, 5)
print(result)
