#Se ejecuta intento de trabajar ventanas en HD, solo disponible en Windows (por eso el "try-except")
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import Label, ttk
from tkinter.constants import LEFT, TOP, X, Y
import tkinter.font as font

from otro_frame import Frame_2

from data import SECTIONS, OPTIONS
from general_styles import COLORS

def on_enter(e):
    e.widget['bg'] = COLORS["dark_blue"]
    e.widget['fg'] = COLORS["yellow"]

def on_leave(e):
    e.widget['bg'] = COLORS["blue"]
    e.widget['fg'] = COLORS["light_gray"]


class Root(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("1000x500")
        self.config(bg=COLORS["light_gray"])
        self.minsize(500, 700)
        #self.maxsize(500, 500)
        font.nametofont("TkDefaultFont")
        self.title("Una aplicación con TkInter")
        self.columnconfigure( 0, weight=1)
        self.columnconfigure( 1, weight=30)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=100)

        #Header
        header = tk.Frame(self, bg=COLORS["blue"])
        header.grid(column=0, row=0, columnspan=2, rowspan=1, sticky="NSWE")
        header.columnconfigure( 0, weight=1)
        header.columnconfigure( 1, weight=10)
        

        # Logo
        logo = tk.Label(header, text="Nombre", fg=COLORS["yellow"], bg=COLORS["blue"], font=("Roboto", 18, "bold"))
        logo.grid(column=0, row=0, sticky="EW")

        #Menu Nav
        menu_nav = tk.Frame(header, bg=COLORS["yellow"])
        menu_nav.grid(column=1, row=0, columnspan=1, sticky="E")
        

        def create_menu_sections():
            number_column = 0
            for element in SECTIONS:
                header.columnconfigure(number_column, weight=1)
                menu_buttons = tk.Button(menu_nav, text=element)
                menu_buttons.config(bg=COLORS["blue"], highlightbackground=COLORS["blue"], fg=COLORS["light_gray"], font=("Roboto", 12), relief="flat", cursor="hand2", activeforeground=COLORS["yellow"])
                menu_buttons.grid(column=number_column, row=0, columnspan=1, sticky="NSWE")
                menu_buttons.bind("<Enter>", on_enter)
                menu_buttons.bind("<Leave>", on_leave)
                number_column = number_column + 1
        
        create_menu_sections()

        #Aside
        aside = tk.Frame(self, bg=COLORS["yellow"])
        aside.grid(column=0, row=1, columnspan=1, rowspan=1, sticky="NSWE")
        aside.columnconfigure( 0, weight=1)

        def create_menu_options():
            number_row = 0
            for element in OPTIONS:
                aside.rowconfigure(number_row, weight=1)
                aside_buttons = tk.Button(aside, text=element)
                aside_buttons.config(bg=COLORS["blue"], highlightbackground=COLORS["blue"], fg=COLORS["light_gray"], font=("Roboto", 12), relief="flat", cursor="hand2", activeforeground=COLORS["yellow"])
                aside_buttons.grid(column=0, row=number_row, columnspan=1, rowspan=1, sticky="NSWE")
                aside_buttons.bind("<Enter>", on_enter)
                aside_buttons.bind("<Leave>", on_leave)
                number_row = number_row + 1
        
        create_menu_options()


if __name__ == "__main__":
    root = Root()
    root.mainloop()