import tkinter

def move_rectangle(event):
    if event.keysym == 'Up':
        canvas.move(square, 0, -50)
    elif event.keysym == 'Down':
        canvas.move(square, 0, 50)
    elif event.keysym == 'Left':
        canvas.move(square, -50, 0)
    elif event.keysym == 'Right':
        canvas.move(square, 50, 0)

window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=700, width=700, bg="blue")
square = canvas.create_rectangle((50,50),(150,150),fill='green')
canvas.pack()
window.bind("<KeyPress>", move_rectangle)
window.mainloop()
