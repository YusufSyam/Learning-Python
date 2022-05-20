from heap import heap

input_example= '''22
1 286789035
1 255653921
1 274310529
1 494521015
3
2 255653921
2 286789035
3
1 236295092
1 254828111
2 254828111
1 465995753
1 85886315
1 7959587
1 20842598
2 7959587
3
1 -51159108
3
2 -51159108
3
1 789534713'''.split('\n')

input_example= [[int(j) for j in i.split(' ')] for i in input_example]

q = input_example[0][0]

for i in range(q):
    queries = input_example[i+1]
    query = int(queries[0])

    if i == 0:
        my_heap = heap(int(queries[1]))
        continue

    if query == 1:
        my_heap.insert(int(queries[1]))
    elif query == 2:
        my_heap.remove(int(queries[1]))
    else:
        print(my_heap.node_dict[1].data)