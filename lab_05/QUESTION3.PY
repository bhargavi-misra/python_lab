strings = ["hello", "world", "python"]
listified = list(map(lambda s: list(s), strings))
print(listified)
