num_rows=5
end=' '
for i in range(num_rows):
    print(' '*(num_rows-i-1*2,end))
    for j in range(i+1):
        print(i+j+1,end=' ')
    for j in range (i-1,-1,-1):
        print(i+j+1,end=' ')
    print()
        