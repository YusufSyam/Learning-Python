from tkinter import *

root= Tk()

# def p():
#
b1= []

# for i in range(6):
#     temp_list= []
#     for i in range(2):
#         temp_list.append()

b1= [Button(root, text='a') for i in range(5)]
r= 0
for i in b1:
    i.grid(row=r, column= 0)
    r+= 1
print(b1[1].grid_info()['row'])
print(b1[0])

def onClick():
    print('au')

b1[0].configure(command=onClick)

root.mainloop()

