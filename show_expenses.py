import mysql
import mysql.connector
from tkinter import *
from tkinter import ttk

con = mysql.connector.connect(host='localhost', user='root', password='12345', \
                              database='expenses')
cur = con.cursor()


class show_expense:
    def __init__(self, rt):
        self.root = rt
        self.root.title("Show Expenses")
        self.root.geometry('480x300')
        self.root.configure(bg='dodgerblue4')

        sql = "Select * from expenses_table"
        cur.execute(sql)

        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        frame1 = Frame(my_canvas, bd=1, bg='light grey', relief=SUNKEN)
        """frame1.place(x=10, y=20, width=400, height=200)"""

        my_canvas.create_window((0, 0), window=frame1, anchor='nw')

        date_label = Label(frame1, text="Expenditure Date", bg='light grey', font=('times roman', 15, 'bold', 'italic'))
        date_label.grid(row=0, column=0, padx=5, pady=4)

        expenditure_label = Label(frame1, text="Expenditure Amount", bg='light grey',
                                  font=('times roman', 15, 'bold', 'italic'))
        expenditure_label.grid(row=0, column=1, padx=5, pady=4)

        records = cur.fetchall()
        r = 1
        total = 0

        for record in records:
            total += record[1]
            if r % 2 == 1:
                bg_color = 'black'
                fg_color = 'blue'
            else:
                bg_color = 'blue'
                fg_color = 'black'
            Label(frame1, text=record[0], bg='light grey', font=('times roman', 15, 'bold', 'italic'),
                  fg=fg_color).grid(
                row=r, column=0)
            Label(frame1, text=record[1], bg='light grey', font=('times roman', 15, 'bold', 'italic'),
                  fg=fg_color).grid(
                row=r, column=1)
            r += 1

        con.commit()
        total_label = Label(main_frame, text="Total : ", font=('times roman', 15, 'bold', 'italic'), bg='dodgerblue4',
                            fg='white')
        total_label.place(x=200, y=230)

        total_label2 = Label(main_frame, text=total, font=('times roman', 15, 'bold', 'italic'), bg='dodgerblue4',
                             fg='white')
        total_label2.place(x=300, y=230)

        self.root.mainloop()
