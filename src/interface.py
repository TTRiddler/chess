# -*- coding: utf-8 -*-

from tkinter import *

DARK_SQUARE_COLOR = '#c66b4c'
LIGHT_SQUARE_COLOR = '#e6c49f'
OUTLINE_COLOR = '#880014'
SQUAD_SIZE = 70


root = Tk()
root.title(u'Шахматы')

canvas = Canvas(width=SQUAD_SIZE*8, height=SQUAD_SIZE*8)

for i in range(8):
    if i % 2 == 0:
        for j in range(1, 8, 2):
            canvas.create_rectangle((j * SQUAD_SIZE, i * SQUAD_SIZE, j * SQUAD_SIZE + 70, i * SQUAD_SIZE + 70),
                                    fill=DARK_SQUARE_COLOR, outline=OUTLINE_COLOR)
    else:
        for j in range(0, 8, 2):
            canvas.create_rectangle((j * SQUAD_SIZE, i * SQUAD_SIZE, j * SQUAD_SIZE + 70, i * SQUAD_SIZE + 70),
                                    fill=DARK_SQUARE_COLOR, outline=OUTLINE_COLOR)

for i in range(8):
    if i % 2 != 0:
        for j in range(1, 8, 2):
            canvas.create_rectangle((j * SQUAD_SIZE, i * SQUAD_SIZE, j * SQUAD_SIZE + 70, i * SQUAD_SIZE + 70),
                                    fill=LIGHT_SQUARE_COLOR, outline=OUTLINE_COLOR)
    else:
        for j in range(0, 8, 2):
            canvas.create_rectangle((j * SQUAD_SIZE, i * SQUAD_SIZE, j * SQUAD_SIZE + 70, i * SQUAD_SIZE + 70),
                                    fill=LIGHT_SQUARE_COLOR, outline=OUTLINE_COLOR)

# l = Label(bg='black', fg='white', width=20)


# def strToSortlist(event):
#     s = e.get()
#     s = s.split()
#     s.sort()
#     l['text'] = ' '.join(s)
#
#
# b.bind('<Button-1>', strToSortlist)
#
# e.pack()
# b.pack()
canvas.pack()
root.mainloop()
