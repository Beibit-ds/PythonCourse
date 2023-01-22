import tkinter


window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=700, width=700, bg="blue")
canvas.create_line((0,700), (700,0), fill='red')
for x in range(50, 650, 60):
    canvas.create_rectangle(
        (x,10),
        (x+50, 60),
        fill='white'
    )
canvas.create_oval((500, 500),(600, 600), fill='black')
canvas.pack()
window.mainloop()
