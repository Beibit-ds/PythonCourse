import tkinter

def draw_circle(event):
    if event.char == 'b':
        canvas.create_oval((500, 500),
                           (600,600),
                           fill='black')
    elif event.char == 'r':
        canvas.create_oval((500, 500),
                           (600,600),
                           fill='red')
    elif event.char == 'g':
        canvas.create_oval((500, 500),
                           (600, 600),
                           fill='green')


window = tkinter.Tk()
canvas = tkinter.Canvas(window, height=700, width=700, bg="blue")
canvas.create_line((0,700), (700,0), fill='red')
title = tkinter.Label(window, text="First drawing")
for x in range(50, 650, 60):
    canvas.create_rectangle(
        (x,10),
        (x+50, 60),
        fill='white'
    )
canvas.pack()
title.pack()
window.bind("<KeyPress>", draw_circle)
window.mainloop()
