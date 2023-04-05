from tkinter import *


score = 0


def points():
    global score
    score = score + 1
    lbl = Label(window, text=score, font=("Ariel", 75))
    lbl.place(x=15, y=30)


window = Tk()
window.title("Clicker Game")
window = Canvas(window, width=250, height=200)
window.pack()
bttn = Button(window, text="Click For Points", command=points, bg="black", fg="white")
bttn.place(x=80, y=150)
window.mainloop()
