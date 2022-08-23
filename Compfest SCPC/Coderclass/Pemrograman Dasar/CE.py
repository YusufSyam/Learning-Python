n= int(input())
arr= [list(map(int, input().strip().split(' '))) for _ in range(n)]

print(sum([arr[i][i] for i in range(n)]))