sequence = "Hello World"

uppercase = list(map(lambda x: x.upper(), set(sequence)))
lowercase = list(map(lambda x: x.lower(), set(sequence)))

print("Uppercase:", ''.join(sorted(uppercase)))
print("Lowercase:", ''.join(sorted(lowercase)))
