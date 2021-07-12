from tkinter import *
from tkmacosx import Button
from general_styles import COLORS
from data import SECTIONS, OPTIONS


class Root(Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.wind = window
        self.wind.geometry("1000x500")
        self.wind.config(bg=COLORS["light_gray"])
        self.wind.minsize(500, 700)
        #self.wind.maxsize(500, 500)
        self.wind.title("Una aplicación con TkInter")
        self.wind.grid_columnconfigure(1, weight=4)
        self.wind.grid_rowconfigure(1, weight=5)
        self.create_widgets()
        
    def create_widgets(self):
        #Header
        self.header = Frame(self.wind, bg=COLORS["blue"])
        self.header.place(x=0, y=0, relwidth=1)
        self.header.grid_columnconfigure(1, weight=4)

        # self.logo_container = Frame(self.header, bg=COLORS["blue"])
        # self.logo_container.grid(column=0, row=0, rowspan=1)

        self.logo = Label(self.header, text="Nombre de la App", bg=COLORS["blue"], fg=COLORS["yellow"], font=("Roboto", 18))
        self.logo.grid(column=0, row=0, padx=5, pady=5)

        self.menu_nav = Frame(self.header, bg=COLORS["yellow"])
        self.menu_nav.grid(column=1, row=0, columnspan=1, sticky='WE')

        self.create_multiple_elements(SECTIONS, self.menu_nav)

        #Aside
        self.aside = Frame(self.wind, bg=COLORS["blue"])
        self.aside.grid(column=0, row=2, rowspan=1, sticky='NS')
        self.create_multiple_elements(OPTIONS, self.aside)

    def create_multiple_elements(self, iterable, where):
        num_column = len(iterable)
        print(num_column)
        def on_enter(e):
            e.widget['bg'] = COLORS["dark_blue"]
            e.widget['fg'] = COLORS["yellow"]

        def on_leave(e):
            e.widget['bg'] = COLORS["blue"]
            e.widget['fg'] = COLORS["light_gray"]

        for element in iterable:
            self.button_section = Button(where, text=element)
            self.button_section.config(bg=COLORS["blue"], highlightbackground=COLORS["blue"], fg=COLORS["light_gray"], font=("Roboto", 14), relief="flat", cursor="hand2", activeforeground=COLORS["yellow"], focuscolor=COLORS["yellow"])
            #self.button_section.grid(column=num_column, row=0, padx=5, pady=5, sticky="E")
            self.button_section.place(height=20, relwidth=0.2, anchor=CENTER)
            self.button_section.bind("<Enter>", on_enter)
            self.button_section.bind("<Leave>", on_leave)
            num_column = num_column - 1




if __name__ == "__main__":
    window=Tk()
    aplication = Root(window)
    window.mainloop()