if __name__ == '__main__':
    s = input()
    flag = 'False'
    for i in s:
        if i.isalnum():
            flag = 'True'
    print(flag)       
    
    flag = 'False'
    for i in s:
        if i.isalpha():
            flag = 'True'
    print(flag)
    
    flag = 'False'
    for i in s:
        if i.isdigit():
            flag = 'True'
    print(flag)
    
    flag = 'False'
    for i in s:
        if i.islower():
            flag = 'True'
    print(flag)
    
    flag = 'False'
    for i in s:
        if i.isupper():
            flag = 'True'
    print(flag)
