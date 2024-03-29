import datetime
from tkinter import *
import tkinter as tk
from fahp import fahp_project

# Call Submit Data function for start Calculations and get result
def submitData():
    pci_info = pci.get()
    deflection_info = deflection.get()
    iri_info = iri.get()
    cvpd_info = cvpd.get()
    result = fahp_project([pci_info, deflection_info, iri_info, cvpd_info])
    label = Label(screen, text="Result is : " + str(result), fg="green", font = ('Helvetica', 18, 'bold'))
    label.pack()
    # screen1.quit



# Load Main Screen Window
def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("600x450")
    screen.title("PCA using FL V1.0")
    Label(text="PCA using FL", bg="grey", width="300", height="2", font=("calibri", 13))
    global pci
    global deflection
    global iri
    global cvpd

    pci = tk.StringVar()
    deflection = tk.StringVar()
    iri = tk.StringVar()
    cvpd = tk.StringVar()
    remarks = "Demo user"

    Label(screen, text="Please enter details Below").pack()
    Label(screen, text="").pack()
    Label(screen, text="PCI").pack()
    pci_entry = Entry(screen, textvariable=pci).pack()
    Label(screen, text="Deflection").pack()
    deflection_entry = Entry(screen, textvariable=deflection).pack()
    Label(screen, text="IRI :").pack()
    iri_entry = Entry(screen, textvariable=iri).pack()
    Label(screen, text="CVPD").pack()
    cvpd_entry = Entry(screen, textvariable=cvpd).pack()
    Label(screen, text="").pack()


    Button(screen, text="Submit", bg="grey", width="10", height="1", command=submitData).pack()

    Button(screen, text="Cancel", bg="grey", width="10", height="1", command=screen.destroy).pack()


    screen.mainloop()


main_screen()
