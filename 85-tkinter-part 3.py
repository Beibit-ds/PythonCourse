import tkinter


window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=700, width=700, bg="blue")
canvas.create_line((0,700), (700,0), fill='red')
canvas.create_rectangle(
    (50,50),
    (400, 500),
    fill='green'
)
canvas.create_oval((500, 500),(600, 600), fill='black')
canvas.pack()
window.mainloop()
