n, m= map(int, input().strip().split(' '))

total_path= 0
def find_path(n_pos, m_pos):
    if n_pos<n-1:
        find_path(n_pos+1, m_pos)
    if m_pos<m-1:
        find_path(n_pos, m_pos+1)

    if n_pos==n-1 and m_pos==m-1:
        global total_path
        total_path+= 1

find_path(0,0)
print(total_path)