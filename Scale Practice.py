from tkinter import *

def stack():
    print("Nasus has " + str(scale.get()) + " stacks!")

window = Tk()

window.title("Ping Nasus stacks!")

nasuspic = PhotoImage(file = "nasus.png")
label = Label(window,
              image = nasuspic)
label.pack()

scale = Scale(window,
              font = ("Impact",20,"bold"),
              from_= 0,
              to = 1000,
              length = 700,
              tickinterval = 100,
              orient = HORIZONTAL,
              fg = "#00FF00",
              bg = "black",
              troughcolor = "#00FF00")
scale.pack(anchor = N)

button = Button(window,
                text = "Ping",
                command = stack,
                relief = SUNKEN,
                fg = "#00FF00",
                activeforeground = "#00FF00",
                bg = "black",
                activebackground = "black")
button.pack(anchor = S)



window.mainloop()