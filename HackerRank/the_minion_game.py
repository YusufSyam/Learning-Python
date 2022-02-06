# Failed due to runtime error

import re

def get_score(s, regex):
    s_len = len(s)

    alphabets= re.finditer(regex, s)
    words_set= set()

    for i in alphabets:
        temp_index= i.start()
        temp_len= s_len-temp_index

        for j in range(temp_len):
            words_set.add(s[temp_index:s_len-j])

    score= 0
    for word in words_set:
        temp_score= len(re.findall(r'(?=('+word+'))', s))
        score+=temp_score

    return score

def minion_game(string):
    s= string
    
    stuart_score= get_score(s, r'[^aiueoAIUEO]')
    kevin_score= get_score(s, r'[aiueoAIUEO]')

    if stuart_score>kevin_score:
        print('Stuart '+str(stuart_score))
    elif kevin_score>stuart_score:
        print('Kevin '+str(kevin_score))
    else:
        print('Draw')
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
