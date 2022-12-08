""" Each tkinter widget is an object with its own attributes and methods. To make a clearer GUI structure
we should create subclasses of the tkinter widgets using OOP """

import tkinter as tk


class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""
    def __init__(self, master):
        super().__init__(master)

        # This creates the widgets
        
        self.config(bg='antique white')
        self.txt = tk.Label(self, text="My tkinter app", bg='red', fg='yellow')
        self.btn = tk.Button(self, text="Press me",bg='red', fg='yellow')
        self.edt = tk.Entry(self,bg='green', fg='pink')
        self.sld = tk.Scale(self,from_=0,to=10000,orient='vertical')
        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them 
        self.txt.grid(row=0,column=0)
        self.btn.grid(row=0,column=1)
        self.edt.grid(row=1,column=0)
        self.sld.grid(row=1,column=1)


if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('Tkinter Class Example')
    root.config(bg='antique white')
    main_frame = TestGUI(root)
    main_frame.pack()
    root.mainloop()
    