arr= list(range(1,int(input())+1))
tiang= [arr, [], []]
tiang_name= ['A', 'B', 'C']

iter= 0
prev_move= None
while True:
    print(tiang)

    iter+= 1
    # if iter==10:
    #     break

    if not tiang[0] and not tiang[1]:
        print('SELESAI')
        break

    for i in range(len(tiang)):
        if all(tiang):
            # print('A', i)
            if bool(tiang[i]) and tiang[i][0]==min([j[0] for j in tiang if len(j)>0]):
                if tiang[i][0] == prev_move:
                    i = i-2 if tiang[i-2][0]<tiang[i-1][0] else i-1
                    print('KESINI',i)

                # print('AA')
                for k in range(len(tiang)-1, -1, -1):
                    if k!=i and tiang[k][0]>tiang[i][0]:
                        print(tiang[i][0], tiang_name[i], tiang_name[k])
                        prev_move= tiang[i][0]
                        tiang[k].insert(0, tiang[i].pop(0))

                        break

                break
        else:
            # print('B', i)
            # print(bool(tiang[i]))
            if bool(tiang[i]) and tiang[i][0]==max([j[0] for j in tiang if len(j)>0]):
                # print('BB')
                if tiang[i][0] == prev_move:
                    i= i-2 if bool(tiang[i-2]) else i-1
                    print('KESINI', i)

                for k in range(len(tiang) - 1, -1, -1):
                    if (k!=i and tiang[k] and tiang[k][0]>tiang[i][0]) or (k != i and not tiang[k]):
                        print(tiang[i][0])

                        print(tiang[i][0], tiang_name[i], tiang_name[k])
                        prev_move= tiang[i][0]
                        tiang[k].insert(0, tiang[i].pop(0))

                        break

                break

# a= tiang[0].pop(0)

# print(min([i[0] for i in a if len(i)>0]))
# print(all(tiang))

# for i in range(3-1,-1,-1):
#     print(i)