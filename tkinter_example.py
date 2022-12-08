import tkinter_example as tk
if __name__ == '__main__':
    root = tk.Tk()
    txt = tk.Label(root, text = 'My Tinker app')
    btn = tk.Button(root, text = 'Press me', height = 100)
    edt = tk.Entry(root)
    
    txt.pack()
    btn.pack()
    edt.pack()
    root.mainloop()
    