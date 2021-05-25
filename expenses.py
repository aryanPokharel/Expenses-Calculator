from tkinter import *
from Expenses_calculator import add_expenses
from Expenses_calculator import show_expenses


class main:
    def __init__(self, rt):
        self.root = rt
        self.root.geometry("400x250")
        self.root.title("Expenses Calculator")
        self.root.configure(bg='salmon4')
        self.root.resizable(0, 0)

        welcome_label = Label(text="Welcome to Expenses Calculator! Choose your action :)", bg='lime green', fg='white',
                              font=('aeiral', 10, 'bold'), height=2)
        welcome_label.pack(side=TOP, fill='x')

        frame1 = Frame(self.root, bd=1, bg='dodgerblue4', relief=SUNKEN)
        frame1.place(x=10, y=50, width=380, height=180)

        add_expenses_btn = Button(frame1, text="Add Expenses", bg='chocolate3', fg='white', font=('aeiral', 10, 'bold'),
                                  height=5, command=self.add_expenses)
        add_expenses_btn.grid(row=0, column=0, padx=50, pady=50)

        show_expenses_btn = Button(frame1, text="Show Expenses", bg='chocolate3', fg='white',
                                   font=('aeiral', 10, 'bold'), height=5, command=self.show_expenses)
        show_expenses_btn.grid(row=0, column=1)

        self.root.mainloop()

    def add_expenses(self):
        add_expenses.add_expense(Tk())

    def show_expenses(self):
        show_expenses.show_expense(Tk())


run = Tk()
main(run)
