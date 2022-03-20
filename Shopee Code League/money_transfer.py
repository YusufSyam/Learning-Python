n, t= list(map(int, input().split()))

person_bal= []
for i in range(n):
    person_bal.append(input())

person_bal= sorted(person_bal)

bal= {}
for i in person_bal:
    temp_person, temp_bal= i.split(' ')
    bal[temp_person]= int(temp_bal)


transaction= []
for i in range(t):
    transaction.append(input())

for i in transaction:
    transfer_er, transfer_ed, amount= i.split(' ')
    amount= int(amount)
    if(amount>bal[transfer_er]):
        continue
    else:
        bal[transfer_er]-= amount
        bal[transfer_ed]+= amount

bal= {k: v for k, v in sorted(list(bal.items()))}
for i in bal:
    print(i, bal[i])