# Python Program to implement Astrologer's Stars logic in GUI.


# Imports
import os
import sys
from PIL import Image
from tkinter.tix import Tk, Balloon
from tkinter import END, RIDGE, Button, Entry, Frame, Label, Text, Toplevel, messagebox

# creating a path for the icon of the window.
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

path = resource_path("./Icon//Icon.ico")


def show(a):
    """Function to show the stars."""

    type(a)                                                                     # Garbage calculation to make use of the unused argument.

    try:                                                                        # Try block to check if the input of n.
        int(en1.get())
    except Exception:                                                           # If the input is invalid, show an error message.
        if len(en1.get()) == 0:
            messagebox.showerror("Error", "Please enter a number.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    try:                                                                        # Try block to check if the input of b.
        int(en2.get())
    except Exception:                                                           # If the input is invalid, show an error message.
        if len(en2.get()) == 0:
            messagebox.showerror("Error", "Please enter a number.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    if int(en1.get()) <= 0 or int(en2.get()) < 0:                               # If the input is invalid, show an error message.
        messagebox.showerror("Error", "Please enter a positive number.")

    else:                                                                       # If the input is valid, show the stars.

        try:                                                                    # Try block.
            n = int(en1.get())                                                  # Taking the input of n.
            b = int(en2.get())                                                  # Taking the input of b.
            b = bool(b)                                                         # Converting the integer b to bool.

        except Exception as e:                                                  # If the input is invalid, show an error message.
            n = b = 0
            messagebox.showerror("Error", str(e))

        top1 = Toplevel(root1)                                                  # Creating a new window.

        # Setting the title of the window.
        top1.title("Stars Output")

        # Setting the icon of the window.
        try:                                                                    # Try block to set the icon of the window.
            top1.iconbitmap(path)
        except Exception:                                                       # If the icon is not found, show an error message.
            messagebox.showerror("Error", "icon.ico not found.")
        
        # Setting the size of the window.
        top1.geometry("500x500")
        top1.minsize(200, 200)
        top1.maxsize(850, 700)

        # Creating a Text.
        txt1 = Text(top1, relief=RIDGE, borderwidth=5, width=100, height=100)
        txt1.pack(padx=20, pady=10)

        # Creating a list containing numbers from 1 to n.
        v = list(range(1, n + 1))

        if not b:                                                            # If the bool value turns False, the list is reversed.
            v.reverse()

        for i in v:                                                          # A loop to print the required pattern.
            txt1.insert(END, "*" * i + "\n")                                 # Inserting the stars in the Text.


if __name__ == '__main__':
    """The Main Function Begins."""

    root1 = Tk()  # Creating main window root1.

    root1.title("Astrologer's Stars")  # Setting the title of root1.

    # Trying to Add Icon to window.
    try:
        root1.iconbitmap(path)

    except Exception:
        messagebox.showerror("Error", "Icon not found.")

    # Geometry of root1.

    root1.geometry('500x300')
    root1.minsize(400, 260)
    root1.maxsize(600, 450)

    # Background Color of root 1.

    root1['bg'] = 'grey'

    # Heading

    Heading = Label(root1, text="Astrologer's Stars", bd=5, font='Aerial 22 underline', bg='black', fg='white')
    Heading.pack(pady=10, ipadx=10)

    # Creating a frame.

    f1 = Frame(root1, bd=20)
    f1.pack()

    # Content.

    lb1 = Label(f1, text="Enter the value of n :", font="Arial 12")             # Creating a Label.
    lb1.grid(row=0, column=0, pady=10, ipadx=3)

    tip1 = Balloon()                                                            # Creating a Balloon.
    tip1['bg'] = 'white'

    en1 = Entry(f1, font="Areal 12")                                            # Creating an Entry.
    en1.grid(row=0, column=1, pady=10)

    tip1.bind_widget(en1, balloonmsg="Enter the value of n(Integer)")           # Binding the Balloon to the Entry.

    # Repeat the same for the other Entry.
    lb2 = Label(f1, text="Enter the bool (0 or 1) :", font="Areal 12")
    lb2.grid(row=1, column=0, pady=10)

    tip2 = Balloon()
    tip2['bg'] = 'white'

    en2 = Entry(f1, font="Areal 12")
    en2.grid(row=1, column=1, pady=10)
    en2.bind("<Return>", show)                                                      # Binding the Entry to the show function.

    tip2.bind_widget(en2, balloonmsg=" Enter the value of bool(1 or 0)")

    tip3 = Balloon()
    tip3['bg'] = 'white'

    bt1 = Button(f1, text="Show", cursor='hand2', font="Arial 12")                  # Creating a Button.
    bt1.grid(row=2, columnspan=2, pady=10, ipadx=7)

    bt1.bind("<Button-1>", show)                                                    # Binding the Button to the show function.

    tip3.bind_widget(bt1, balloonmsg="Click to view the Pattern.")                  # Binding the Balloon to the Button.

    root1.mainloop()                                                                # Mainloop of root1.
