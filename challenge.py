# importing the Tkinter module
from tkinter import *
from tkinter import messagebox

# Below is the frame configuration
box = Tk()
box.geometry("500x350")
box.title("Sick Class Calculator")
frame = Frame(box)
box.config(bg="Yellow")

# Below is the layout of all the labels and entries

MSickID = Label(box, text="Sickness Code", bg="Yellow")
MSickID.place(x=20, y=20)

sick_entry = Entry(box, bd=1)
sick_entry.place(x=300, y=20)

MDurationOfTreatment = Label(box, text="Duration Of Treatment", bg="Yellow")
MDurationOfTreatment.pack(side=LEFT)
MDurationOfTreatment.place(x=20, y=80)

weeks_monthly = Label(box, text="Weekly/Months", bg="Yellow")
weeks_monthly.place(x=300, y=100)

due_entry = Entry(box, bd=1, width=8)
due_entry.place(x=300, y=80)

MDoctorsID = Label(box, text="Doctor's Practice Number", bg="Yellow")
MDoctorsID.place(x=20, y=150)

doc_entry = Entry(box, bd=1)
doc_entry.place(x=300, y=150)

scan_fee = Label(box, text="Scan or Consultation Fee", bg="Yellow")
scan_fee.place(x=20, y=190)

scan_entry = Entry(box, bd=1)
scan_entry.place(x=301, y=190)

amount_paid = Label(box)
amount_paid.place(x=20, y=260)

var = StringVar()


# The Calculations necessary for my window
class Sick:
    def sickness(self):
        self.MSickID = MSickID
        self.MDurationOfTreatment = MDurationOfTreatment
        self.MDoctorsID = MDoctorsID
        self.medcancer = 400
        self.medinflu = 350.50


# The calculation for cancer and influenza
def sickness():
    if var.get() == "Cancer":
        if int(scan_entry.get()) > 600:
            messagebox.showinfo("Message", "Sorry we cannot treat you")  # Error message will display
        elif int(scan_entry.get()) < 600:
            cancer_answer = int(scan_entry.get()) + 400
            amount_paid.config(text="AmountPaidForTreatment: " + str(cancer_answer))

    if var.get() == "Influenza":
        if int(scan_entry.get()) >= 600:
            influ_answer = 350.50 + int(scan_entry.get())
            amount_paid.config(text="AmountPaidForTreatment: " + str(influ_answer))
        elif int(scan_entry.get()) < 600:
            influ_answer = 350.50 + int(scan_entry.get())
            discount = (influ_answer * (2 / 100)) + influ_answer  # The calculation for the discount parameter
            messagebox.showinfo("Message", "2% discount")
            amount_paid.config(
                text="Amount Paid For Treatment: " + str(discount))


# Below are all the buttons needed for the window
radbtn1 = Radiobutton(box, text="   Cancer", variable=var, value="Cancer", bg="Yellow")
radbtn1.place(x=20, y=220)

radbtn2 = Radiobutton(box, text="Influenza", variable=var, value="Influenza", bg="Yellow")
radbtn2.place(x=20, y=240)

cal_btn = Button(box, text="Calculate", command=sickness, fg="Green")
cal_btn.place(x=20, y=300)


# below is for the clear button so that it works
def clear_all():
    sick_entry.delete(0, END)
    due_entry.delete(0, END)
    doc_entry.delete(0, END)
    scan_entry.delete(0, END)


clear_btn = Button(box, text="Clear", command=clear_all, fg="Red")  # Clears everything when the button is pushed
clear_btn.place(x=300, y=300)

box.mainloop()
