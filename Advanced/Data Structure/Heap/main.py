from heap import heap

'''22
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
1 789534713'''

my_heap= heap(1)
my_heap.insert(2)
my_heap.insert(3)
my_heap.insert(-100)
my_heap.insert(4)
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(8)
my_heap.insert(9)
my_heap.insert(10)
my_heap.insert(11)
my_heap.insert(12)
my_heap.insert(13)

my_heap.show_dict()

my_heap.remove(-100)
print()
my_heap.show_dict()