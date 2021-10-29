start, end= map(int, input().split())

print("O JOGO DUROU {:d} HORA(S)".format(24 if start==end else (24-start+end)%24))