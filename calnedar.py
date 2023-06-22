import tkinter as tk
import tkcalendar
import datetime
from datetime import datetime
from tkcalendar import DateEntry


class MYcalendar():
    def __init__(self):
        try:
            self.formatData = "%m/%d/%y"
            self.root = tk.Tk()
            self.label1 = tk.Label(self.root, text="chose first date")
            self.label1.pack()
            self.date_entry = DateEntry(self.root, date_pattern="dd/mm/yy")
            self.date_entry.pack()
            self.label2 = tk.Label(self.root, text="chose last date")
            self.label2.pack()
            self.label3 = tk.Label(self.root, text="")
            self.date_entry1 = DateEntry(self.root, date_pattern="dd/mm/yy")
            self.date_entry1.pack()
            self.diffDate = tk.Button(self.root, text="select!",
                                      command=self.updateLabel3)
            self.diffDate.pack()
            # Create a DateEntry widget with a specific date format

            self.root.geometry('600x600')
            self.root.mainloop()
        except Exception:
            pass

    def updateLabel3(self):
        diff = self.date_entry1._date - self.date_entry._date
        diff = diff.days
        self.diffDate.config(text=f"diffrence between days is  :   {diff}"
                             )
