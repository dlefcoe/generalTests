'''

example by: dlefcoe

darren@redhedge.uk
twitter: @dlefcoe

the cuser cannot use pack and grid together.
ie. pack & grid are mutually exclusive.

frame lets both exist together.

'''

import tkinter as tk
from PIL import Image, ImageTk

import os


root = tk.Tk()
root.title('RedHedge - radio button example')
root.iconbitmap('RH_icon.ico')

r = tk.IntVar()
r.set('2')


toppings = [
    ('peperoni','peperoni'),
    ('cheese','cheese'),
    ('mushroom','mushroom'),
    ('onion','onion')
]

pizza = tk.StringVar()
pizza.set('peperoni')

for text, topping in toppings:
    tk.Radiobutton(root, text=text, variable=pizza, value=topping).pack()


def clicked(value):
    ''' writes label with give value '''
    my_label = tk.Label(root, text=value)
    my_label.pack()


# radio buttons
# r1 = tk.Radiobutton(root, text='option 1', variable=r, value=1, command=lambda: clicked(r.get() ))
# r2 = tk.Radiobutton(root, text='option 2', variable=r, value=2, command=lambda: clicked(r.get() ))
# r1.pack()
# r2.pack()


my_button = tk.Button(root, text='some button', command=lambda: clicked(pizza.get() )).pack()


root.mainloop()



