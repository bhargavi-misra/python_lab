num_rows=5
for i in range(num_rows):
    current_char=chr(65+i)
    for j in range(i+1):
        print(current_char,end='')
    print()    