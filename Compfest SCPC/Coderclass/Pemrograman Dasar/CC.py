a, b, c= map(int, input().strip().split(' '))

karton= ''
for i in range(a):
    for j in range(b):
        karton+= ('*' if (i<c or j<c or i>=a-c) else '.')

    karton+= ('\n' if i!=(a-1) else '')

print(karton)