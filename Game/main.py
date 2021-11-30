from tkinter import *

window = Tk()
window.title("Pokémon Python")
window.configure(background = "black")


photo1 = PhotoImage(file="rayq.gif")
Label(window, image=photo1, bg="black") .grid(row=0, column=0, sticky=N)

# Create a label
Label(window, text="Welcome to the world of Pokémon!",
      bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)


window.mainloop()

