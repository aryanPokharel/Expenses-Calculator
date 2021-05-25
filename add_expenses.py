import mysql
import mysql.connector

from tkinter import *

con = mysql.connector.connect(host='localhost', user='root', password='12345', \
                              database='expenses')
cur = con.cursor()


class add_expense:
    def __init__(self, rt):
        self.root = rt
        self.root.title("Add Expenses")
        self.root.geometry('400x350')
        self.root.configure(bg='lime green')

        label1 = Label(self.root, text="Please provide the necessary details!", bg='light grey', fg='black',
                       font=('times roman', 15, 'bold', 'italic'), height=2)
        label1.pack(side=TOP, fill='x')

        frame1 = Frame(self.root, bd=1, bg='dodgerblue4', relief=SUNKEN)
        frame1.place(x=10, y=60, width=380, height=280)

        date_label = Label(frame1, text="Date (YYYY-MM-DD):", fg='white', bg='dodgerblue4',
                           font=('times roman', 12, 'bold', 'italic'), width=15, height=2)
        date_label.grid(row=0, column=0)

        self.date_entry = Entry(frame1, width=15, font=('times roman', 15, 'bold', 'italic'))
        self.date_entry.grid(row=0, column=1, padx=5)

        amount_label = Label(frame1, text="Amount (In Rs) : ", fg='white', bg='dodgerblue4',
                             font=('times roman', 15, 'bold', 'italic'), width=15,
                             height=2)
        amount_label.grid(row=1, column=0)

        self.amount_entry = Entry(frame1, width=15, font=('times roman', 15, 'bold', 'italic'))
        self.amount_entry.grid(row=1, column=1, padx=5)

        submit_btn = Button(frame1, text="Submit", font=('times roman', 15, 'bold', 'italic'), width=10,
                            command=self.submit_btn)
        submit_btn.place(x=100, y=100)

        reset_btn = Button(frame1, text="Reset", font=('times roman', 15, 'bold', 'italic'), width=10,
                           command=self.reset_btn)
        reset_btn.place(x=240, y=100)

        self.root.mainloop()

    def reset_btn(self):
        self.date_entry.delete(0, END)
        self.date_entry.insert(0, '')

        self.amount_entry.delete(0, END)
        self.amount_entry.insert(0, '')

    def submit_btn(self):
        date = self.date_entry.get()
        amount = self.amount_entry.get()

        sql = "Insert into expenses_table (expense_date, expense_amount) values (%s, %s)"
        values = date, amount

        cur.execute(sql, values)
        con.commit()

        print("Info added!")
