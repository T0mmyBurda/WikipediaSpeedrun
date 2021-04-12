from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

frame2 = Frame(frame)
frame2.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="green", fg="green")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

redbutton2 = Button(frame, text="Red", fg="red")
redbutton2.pack( side = LEFT)

greenbutton2 = Button(frame, text="green", fg="green")
greenbutton2.pack( side = LEFT )

bluebutton2 = Button(frame, text="Blue", fg="blue")
bluebutton2.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()