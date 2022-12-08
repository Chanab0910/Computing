import tkinter as tk
from tkinter import ttk

class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""
    def __init__(self, master):
        super().__init__(master)
          
        self.Title = tk.Label(self, text='Registration Form')
        self.name = tk.Label(self, text='Full name')
        self.name_box = tk.Entry(self)
        self.email = tk.Label(self, text='Email')
        self.email_box = tk.Entry(self)
        self.gender = tk.Label(self, text='Gender')
        
        self.gender_options = ttk.Radiobutton(self, text='Male', value=1) 
         
        
        self.place_widgets()
        
        
    def place_widgets(self):
        # This code creates the widgets and grids them 
        self.Title.grid(row=0,column=0)
        self.name.grid(row=1,column=0)
        self.name_box.grid(row=1,column=1)
        self.email.grid(row=2,column=0)
        self.email_box.grid(row=2, column=1)
        self.gender.grid(row=3, column=0)
        self.gender_options(row=3, column=1)
        








if __name__ == '__main__':    
    root = tk.Tk()
    main_frame = TestGUI(root)
    main_frame.pack()
    root.mainloop()