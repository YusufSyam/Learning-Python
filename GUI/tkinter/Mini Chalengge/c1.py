# Kita akan membuat program berisi 2x6 button yang akan berubah warnanya jika diklik
# Warna dari button akan dipilih melalui input button

from tkinter import *

root= Tk()

label1= Label(root, text='Klik tombol cycle di bawah untuk mengganti warna, jika warna tidak valid maka akan direset menjadi white').grid(row=0, column=0)

entry= Entry(root, width=50)
entry.insert(0, 'red')
entry.configure(state='disabled')

entry.grid(row=1, column=0)

color_list= ['red', 'white', 'yellow', 'black', 'blue', 'green']
n_time_clicked= 1
def on_click(entry):
    global n_time_clicked
    global color_list

    entry.configure(state='normal')
    entry.delete(0, END)
    entry.insert(0, color_list[n_time_clicked%len(color_list)])
    entry.configure(state='disabled')

    n_time_clicked+= 1

button= Button(root, text='cycle', command= lambda : on_click(entry)).grid(row=1, column=1)

def change_color(color, index_row, index_col):
    global colored_label_list
    colored_label_list[index_row][index_col].configure(bg=color)

cll_rows= 2
cll_cols= 6
colored_label_list= [[Button(root, text='\t', bg=color_list[(i+j)%len(color_list)]) for j in range(cll_rows)] for i in range(cll_cols)]

# button_info= [[0 for i in range(cll_rows)] for j in range(cll_cols)]
# button_info= {}
for i in range(cll_cols):
    for j in range(cll_rows):
        colored_label_list[i][j].grid(row=j, column=i+2)

        # button_info[colored_label_list[i][j]]= colored_label_list[i][j].grid_info()
        # a, b= button_info['row'], button_info['column']
        # colored_label_list[i][j].configure(command = lambda: change_color(entry.get(), button_info[colored_label_list[i][j]]['row'], button_info[colored_label_list[i][j]]['column']))

# Hard coding =')
colored_label_list[0][0].configure(command= lambda : change_color(entry.get(), 0, 0))
colored_label_list[0][1].configure(command= lambda : change_color(entry.get(), 0, 1))
colored_label_list[1][0].configure(command= lambda : change_color(entry.get(), 1, 0))
colored_label_list[1][1].configure(command= lambda : change_color(entry.get(), 1, 1))
colored_label_list[2][0].configure(command= lambda : change_color(entry.get(), 2, 0))
colored_label_list[2][1].configure(command= lambda : change_color(entry.get(), 2, 1))
colored_label_list[3][0].configure(command= lambda : change_color(entry.get(), 3, 0))
colored_label_list[3][1].configure(command= lambda : change_color(entry.get(), 3, 1))
colored_label_list[4][0].configure(command= lambda : change_color(entry.get(), 4, 0))
colored_label_list[4][1].configure(command= lambda : change_color(entry.get(), 4, 1))
colored_label_list[5][0].configure(command= lambda : change_color(entry.get(), 5, 0))
colored_label_list[5][1].configure(command= lambda : change_color(entry.get(), 5, 1))

root.mainloop()
