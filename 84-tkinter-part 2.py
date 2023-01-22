import tkinter


window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=700, width=700, bg="blue")
canvas.create_rectangle(
    (50,50),
    (400, 500),
    fill='green'
)
canvas.pack()
window.mainloop()
