c, k= 50, 3
c_list= [1, 3, 5, 7, 9]
c_list= list(map(int, '''390225 426456 688267 800389 990107 439248 240638 15991 874479 568754 729927 980985 132244 488186 5037 721765 251885 28458 23710 281490 30935 897665 768945 337228 533277 959855 927447 941485 24242 684459 312855 716170 512600 608266 779912 950103 211756 665028 642996 262173 789020 932421 390745 433434 350262 463568 668809 305781 815771 550800'''.split(' ')))

price_list = []
if(c==k):
    price_list= c_list
else:
    rotation= 0
    flower_bought= 0
    c_list.reverse()
    for i in range(c):
        if(flower_bought>0 and flower_bought%k==0):
            rotation+=1
        for j in c_list:
            if(i<k):
                flower_bought+= 1
                price_list.append(j)
                c_list.remove(j)
                break
            else:
                flower_bought+=1
                price_list.append(j*(rotation+1))
                c_list.remove(j)
                break
    print(rotation)
    print(flower_bought)


print(sum(price_list))