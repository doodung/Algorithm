a, b = map(int, input().strip().split(' '))

star='*'
for i in range(int(b)) :
    for j in range(int(a)):
        print('*',end='')
    print('')