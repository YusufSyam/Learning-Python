a, b= map(int, input().strip().split(' '))
arr= [list(map(int, input().strip().split(' '))) for _ in range(a)]

print('\n'.join([' '.join([str(j) for j in i]) for i in [[arr[i][j] for i in range(a)] for j in range(b)]]))