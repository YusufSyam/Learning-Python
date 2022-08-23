n, k= map(int, input().strip().split(' '))
arr= map(int, input().strip().split(' ')) if k>0 else []

print(' '.join([str(j) for j in sorted(list({i for i in range(1,n+1)}-set(arr)))]))
