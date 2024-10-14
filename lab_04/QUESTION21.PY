num_rows=4
for i in range(num_rows):
    for j in range(num_rows):
        if(i+j)%2==0:
            print('1',end='')
        else:
            print('0',end='')
    print()