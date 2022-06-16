import datetime
from tkinter import *
import tkinter as tk


# Load Main Screen Window
def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("600x450")
    screen.title("PCA using FL V1.0")
    Label(text="PCA using FL", bg="grey", width="300", height="2", font=("calibri", 13))


    pci = tk.StringVar()
    fname = tk.StringVar()
    department = tk.StringVar()
    mobile = tk.StringVar()
    remarks = "Demo user"

    Label(screen, text="Please enter details Below").pack()
    Label(screen, text="").pack()
    Label(screen, text="User ID").pack()
    uid_entry = Entry(screen, textvariable=uid).pack()
    Label(screen, text="User Name").pack()
    fname_entry = Entry(screen, textvariable=fname).pack()
    Label(screen, text="Mobile No:").pack()
    mobile_entry = Entry(screen, textvariable=mobile).pack()
    Label(screen, text="Department").pack()
    department_entry = Entry(screen, textvariable=department).pack()
    Label(screen, text="").pack()

    Button(screen, text="Register", bg="grey", width="10", height="1", command="").pack()
    Button(screen, text="Cancel", bg="grey", width="10", height="1", command=screen.destroy).pack()


    screen.mainloop()


main_screen()
