from tkinter import *
from tkinter import ttk
import datetime
from playsound import playsound

class tkinter():
    #make tk callable
    root = Tk()

    user_minutes = "0"

    #initialize variable for use with tkinter
    variable = StringVar()

    def create_tk_top_label(self):
        self.your_label = Label(self.root, text="Custom Timer")
        self.your_label.grid(column=0, row=0)

    def create_tk_userinput(self):
        self.feet_entry = Entry(self.root, width=7, textvariable=self.user_minutes)
        self.feet_entry.grid(column=0, row=1)

    def create_tk_button(self):
        self.start_button = Button(self.root, text="start", command=self.tk_update_label)
        self.start_button.grid(column=0, row=2)

    def create_tk_output_label(self):

        self.your_label2 = Label(self.root, textvariable=self.variable)
        self.your_label2.grid(column=0, row=3)

    def tk_update_label(self):
        #grabs the variable from tkinter and sets it
        self.time_entry = self.feet_entry.get()

        #main for loop, also converts variable to integer and then makes it into minutes
        for i in reversed(range(int(self.feet_entry.get())*60)):


            self.variable.set(str(i))
            self.root.after(1000, self.root.update())

            #plays sound when timer is up.
            if i == 0:
                for i2 in range(10):
                    playsound('soundfiles/270405__littlerobotsoundfactory__pickup-gold-03.wav')


object1 = tkinter()

object1.create_tk_top_label()
object1.create_tk_userinput()
object1.create_tk_button()
object1.create_tk_output_label()
tkinter.root.mainloop()