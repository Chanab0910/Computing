import tkinter as tk


class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, master):
        super().__init__(master)
        self.temp_c = tk.StringVar()
        self.temp_c.set(0)
        self.temp_f = tk.StringVar()
        self.temp_f.set(0)


        self.title = tk.Label(master, text='Temperature Converter\n')
        self.converter_label = tk.Label(master, text='Enter Celsius')
        self.fahrenheit_converter_box = tk.Entry(master, textvariable=self.temp_c, bg='white')
        self.fahrenheit_entry_button = tk.Button(master, text='Click to convert', command=self.convert_to_fahrenheit)
        self.fahrenheit_converted_num = tk.Label(master)
        self.fahrenheit_converted_num_label = tk.Label(master,text='Converted number is: ')

        self.celsius_converter_box = tk.Entry(master, textvariable=self.temp_c, bg='white')
        self.celsius_entry_button = tk.Button(master, text='Click to convert', command=self.convert_to_celsius)
        self.celsius_converted_num = tk.Label(master)
        self.celsius_converted_num_label = tk.Label(master, text='Converted number is: ')

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.title.grid(row=0, column=0)
        self.converter_label.grid(row=1,column=0)
        self.fahrenheit_converter_box.grid(row=1, column=1)
        self.fahrenheit_entry_button.grid(row=2,column=0)
        self.fahrenheit_converted_num_label.grid(row=2,column=1)
        self.fahrenheit_converted_num.grid(row=2,column=2)
# change all to celsius next
        self.converter_label.grid(row=1, column=0)
        self.fahrenheit_converter_box.grid(row=1, column=1)
        self.fahrenheit_entry_button.grid(row=2, column=0)
        self.fahrenheit_converted_num_label.grid(row=2, column=1)
        self.fahrenheit_converted_num.grid(row=2, column=2)

    def convert_to_fahrenheit(self):
        c = self.temp_c.get()
        f = celsius_to_fahrenheit(c)

        self.fahrenheit_converted_num.config(text=f)

    def convert_to_celsius(self):
        f = self.temp_c.get()
        c = fahrenheit_to_celsius(f)

        self.celsius_converted_num.config(text=c)


def fahrenheit_to_celsius(f):
    c = (f - 32) / 1.8


    return c

def celsius_to_fahrenheit(c):
    f = int(c) * 1.8 + 32

    return f


if __name__ == '__main__':
    root = tk.Tk()

    main_frame = TestGUI(root)

    root.mainloop()