len_s, q= map(int, input().strip().split(' '))
s= list(input())

for i in range(q):
    query, a, b= map(int, input().strip().split(' '))

    if query==1:
        a2, b2= s[a-1], s[b-1]

        s[a-1]= b2
        s[b-1]= a2
    else:
        s[a-1:b]= reversed(s[a-1:b])

print(''.join(s))