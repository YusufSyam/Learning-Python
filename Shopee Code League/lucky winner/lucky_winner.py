import numpy as np
from collections import Counter

tokens= 3
total_rows= 5
total_cols= 3

# tokens, total_rows= map(int, input().split())

if(tokens>np.floor((total_rows*total_cols)/2)):
    print('Finding n tokens combination is not possible')

arr= np.array([[100, -9, -1], [-1, 3, 2], [-9, 2, 3], [2, 5, 1], [3, 3, 4]])

summed_dict= {}

for row_idx, row in enumerate(arr):
    for col_idx, col in enumerate(row):
        if(col_idx==total_cols-1):
            break
        # print(col+row[col_idx+1], end=' ')
        summed_dict[f'r{row_idx}c{col_idx}|r{row_idx}c{col_idx+1}']= col+row[col_idx+1]

    if(row_idx==total_rows-1):
        break

    for col_idx, col in enumerate(row):
        # print(col+arr[row_idx+1][col_idx], end=' ')
        summed_dict[f'r{row_idx}c{col_idx}|r{row_idx+1}c{col_idx}']= col+arr[row_idx+1][col_idx]


    # print()

# print()
# print()

print(summed_dict)
print()
# print(max(summed_dict))
# print('-----------------')


counter= Counter(summed_dict)
print(counter.most_common(len(summed_dict)-8))