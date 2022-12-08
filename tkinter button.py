import tkinter as tk


class ClickApp(tk.Tk):
    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()
     
        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.background_color_frame = BackgroundColorFrame(self)
        
        self.clicker_frame.pack(side=tk.LEFT)
        self.background_color_frame.pack(side=tk.LEFT)
        
class BackgroundColorFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.colors = [['red','#FF0000'],['green','#00FF00'],['yellow','#FFFF00'],['gold','#FFD700'],['Black pearl', '#1E272C'],['orange','#FFA500'],['vintage green','#065535']]
        
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])
        
        self.radio_options = [tk.Radiobutton(self,
                                             text=color[0],
                                             value=color[1],
                                             variable=self.selected_color,
                                             command=self.change_color,
                                            )
                              for color in self.colors]
        self.place_widgets()
    
    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w',padx=[5,10])
        
    def change_color(self):
        color=self.selected_color.get()
        self.config(bg=color)
        self.master.config(bg=color)
        self.master.clicker_frame.config(bg=color)

class ButtonClicker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.clicks = 0
        # This creates the widgets   
        self.title_txt = tk.Label(self, text="My clicker app")
        self.btn = tk.Button(self, text="Press me", height=10,width=10, command=self.add_click)
        self.response_txt = tk.Label(self, text="No clicks")

        self.place_widgets()
    
    def add_click(self):
        self.clicks +=1
        click_test = f'Number of clicks = {self.clicks}'
        self.response_txt.config(text=click_test)
        
    def place_widgets(self):
        # Use this for settings that will apply to all widgets
        settings = {'padx': 10, 'pady': 10}
        
        # The **settings 'unpacks' the dictionary into padx=10, pady=10
        self.title_txt.grid(row=0, column=0, **settings)
        self.btn.grid(row=1, column=0, **settings)
        self.response_txt.grid(row=2, column=0, **settings)
    


if __name__ == '__main__':
    app = ClickApp()
    app.mainloop()
    