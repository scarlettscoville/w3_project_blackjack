# Let's go, Dream Team!


from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text = "Dream Team Blackjack")
myLabel2 = Label(root, text = "built by Scarlett, Dak, and Grady")

# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()

class Dealer():
    def __init__(self):
        pass

    # Look into Fisher-Yates shuffle for shuffling algorithm? [https://www.youtube.com/watch?v=4zx5bM2OcvA]

class Player():
    def __init__(self):
        pass

class Player_UI():
    def __init__(self):
        pass