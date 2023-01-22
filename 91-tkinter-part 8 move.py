import tkinter

def move_rectangle(event):
    canvas.move(square, 50,50)


window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=700, width=700, bg="blue")
square = canvas.create_rectangle((50,50),(150,150),fill='green')
canvas.pack()
window.bind("<KeyPress>", move_rectangle)
window.mainloop()
