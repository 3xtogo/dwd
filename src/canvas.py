import tkinter as tk

master = tk.Tk()

w = tk.Canvas(master, width=800, height=480)
w.pack()

gif1 = tk.PhotoImage(file='HSRM.gif')
gif
w.create_image(50, 10, image=gif1)
'''
Draws an image on the canvas.

position
    Image position, given as two coordinates.
**options
    Image options.
activeimage=
anchor=
    Where to place the image relative to the given position. Default is CENTER.
disabledimage=
image=
    The image object. This should be a PhotoImage or BitmapImage, or a compatible object (such as the PIL PhotoImage). The application must keep a reference to the image object. 
state=
    Item state. One of NORMAL, DISABLED, or HIDDEN.
tags=
    A tag to attach to this item, or a tuple containing multiple tags.
Returns:
    The item id.
'''


tk.mainloop()
