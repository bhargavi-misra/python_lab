num_rows=4
for i in range(num_rows):
    for j in range(i+1):
        if(i+j)%2==0:
            print('A',end='')
        else:
            print('B',end='')
    print()