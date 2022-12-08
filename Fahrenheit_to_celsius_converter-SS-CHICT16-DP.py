import tkinter as tk


class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, master):
        super().__init__(master)
        self.title = tk.Label(master, text='Temperature Converter\n')
        self.converter_label = tk.Label(master, text='Enter number')
        self.fahrenhuit_converter_box = tk.Entry(master, bg='white')
        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.title.grid(row=0, column=0)
        self.converter_label.grid(row=1,column=0)
        self.fahrenhuit_converter_box.grid(row=2,column=0)

    def fahrenheit_to_celsius(self, f):
        f = f - 32
        f = f / 1.8

        return round(f, 2)

    def celsius_to_fahrenheit(self, c):
        c = c * 1.8
        c += 32
        return round(c, 2)


if __name__ == '__main__':
    root = tk.Tk()

    main_frame = TestGUI(root)

    root.mainloop()