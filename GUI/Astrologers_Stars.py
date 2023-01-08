# Python Program to implement Astrologer's Stars logic in GUI.


# Imports
import os
import sys
import customtkinter
from customtkinter import CTk, CTkTextbox, END, CTkLabel, CTkFrame, CTkButton, CTkEntry, CTkScrollbar
from tkinter import messagebox, CENTER, BOTH, RIGHT


def switch_event():
    global theme
    theme = switch_var.get()
    customtkinter.set_appearance_mode(theme)


theme = "dark"
# Setting the appearance mode of the window.
customtkinter.set_default_color_theme("green")

# creating a path for the icon of the window.


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path = resource_path("./Icon//Icon.ico")


def segmented_button_callback(value):
    pass


def show(a):
    """Function to show the stars."""

    # Garbage calculation to make use of the unused argument.
    type(a)

    # Try block to check if the input of n.
    try:
        int(en1.get())
    # If the input is invalid, show an error message.
    except Exception:
        if len(en1.get()) == 0:
            messagebox.showerror("Error", "Please enter a number.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    # If the input is invalid, show an error message.
    if int(en1.get()) <= 0 < 0:
        messagebox.showerror("Error", "Please enter a positive number.")

    # If the input is valid, show the stars.
    else:

        # Try block.
        try:
            # Taking the input of n.
            n = int(en1.get())
            # Taking the input of b.
            b = segemented_button.get()
            # Converting the integer b to bool.
            if b == "True":
                b = True
            else:
                b = False

        # If the input is invalid, show an error message.
        except Exception as e:
            n = b = 0
            messagebox.showerror("Error", str(e))

        # Creating a new window.
        top1 = customtkinter.CTkToplevel(root1)

        # Setting the title of the window.
        top1.title("Stars Output")

        # Setting the icon of the window.
        # Try block to set the icon of the window.
        try:
            top1.iconbitmap(path)
        # If the icon is not found, show an error message.
        except Exception:
            messagebox.showerror("Error", "icon.ico not found.")

        # Setting the size of the window.
        top1.geometry("500x500")
        top1.minsize(200, 200)
        top1.maxsize(850, 700)

        # Creating a Text.
        txt1 = CTkTextbox(top1, width=100, height=100, wrap="none")
        txt1.pack(pady=10, padx=10, fill=BOTH, expand=True)

        # Creating a list containing numbers from 1 to n.
        v = list(range(1, n + 1))

        # If the bool value turns False, the list is reversed.
        if not b:
            v.reverse()

        # A loop to print the required pattern.
        for i in v:
            # Inserting the stars in the Text.
            txt1.insert(END, "*" * i + "\n")


if __name__ == '__main__':
    """The Main Function Begins."""

    root1 = CTk()  # Creating main window root1.

    # Creating font to use.
    headingFont = customtkinter.CTkFont(
        family="Aerial", size=22, underline=True)
    normalFont = customtkinter.CTkFont(family="Aerial", size=12)

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

    # Heading

    Heading = CTkLabel(root1, text="Astrologer's Stars", font=headingFont)
    Heading.pack(pady=10, ipadx=10)

    # Creating a frame.

    f1 = CTkFrame(root1)
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)

    switch_var = customtkinter.StringVar(value="dark")

    CTkLabel(root1, text="🌙").place(relx=0.77, rely=0.09, anchor=CENTER)

    switch_1 = customtkinter.CTkSwitch(root1, text="☀️", command=switch_event,
                                       variable=switch_var, onvalue="light", offvalue="dark", )
    switch_1.place(relx=0.9, rely=0.1, anchor=CENTER)

    # Content.

    # Creating a Label.
    lb1 = CTkLabel(f1, text="Enter the value of n :", font=normalFont)
    lb1.grid(row=0, column=0, pady=10, ipadx=4, padx=5)

    # Creating an Entry.
    en1 = CTkEntry(f1, font=normalFont)
    en1.grid(row=0, column=1, pady=10, padx=10)

    # Repeat the same for the other Entry.
    lb2 = CTkLabel(f1, text="Select bool b :", font=normalFont)
    lb2.grid(row=1, column=0, pady=10)

    segemented_button = customtkinter.CTkSegmentedButton(root1,
                                                         values=[
                                                             "True", "False"],
                                                         command=segmented_button_callback)
    segemented_button.place(relx=0.57, rely=0.5, anchor=CENTER)

    # Creating a Button.
    bt1 = CTkButton(f1, text="Show", cursor='hand2', font=normalFont)
    bt1.grid(row=2, columnspan=2, pady=10, ipadx=7)

    # Binding the Button to the show function.
    bt1.bind("<Button-1>", show)

    # Mainloop of root1.
    root1.mainloop()
