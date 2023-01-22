import tkinter

def move_rectangle(event):
    x0, y0, x1, y1 = canvas.coords(square)
    if event.keysym == 'Up':
        canvas.move(square, 0, -50)
        if y0 < 0:
            canvas.move(square, 0, 750)
    elif event.keysym == 'Down':
        canvas.move(square, 0, 50)
        if y1 > 700:
            canvas.move(square, 0, -750)
    elif event.keysym == 'Left':
        canvas.move(square, -50, 0)
        if x0 < 0:
            canvas.move(square, 750, 0)
    elif event.keysym == 'Right':
        canvas.move(square, 50, 0)
        if x1 > 700:
            canvas.move(square, -750, 0)


window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=700, width=700, bg="blue")
square = canvas.create_rectangle((50,50),(150,150),fill='green')
canvas.pack()
window.bind("<KeyPress>", move_rectangle)
window.mainloop()
