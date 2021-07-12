from tkinter import *
from tkmacosx import Button
from general_styles import COLORS, on_enter, on_leave



class Calculator:
    def __init__(self, window):
        calculator = window
        calculator.geometry("240x250")
        calculator.config(bg=COLORS["light_gray"])

        def suma():
            first_value = first_text.get()
            second_value = second_text.get()

            if first_value == "":
                first_text["highlightbackground"] = COLORS["warning"]
            elif second_value == "":
                second_text["highlightbackground"] = COLORS["warning"]
            else:
                result_sum = int(first_value) + int(second_value)
                third_text.delete(0, "end")
                third_text.insert(0, result_sum)
                first_text["highlightbackground"] = COLORS["blue"]
                second_text["highlightbackground"] = COLORS["blue"]
                third_text["highlightbackground"] = COLORS["success"]




        first_label = Label(calculator, text="Primer numero", bg=COLORS["blue"], fg=COLORS["light_gray"])
        first_label.place(x=10, y=10, width=100, height=30)

        second_label = Label(calculator, text="Segundo numero", bg=COLORS["blue"], fg=COLORS["light_gray"])
        second_label.place(x=10, y=50, width=100, height=30)

        result = Label(calculator, text="Resultado", bg=COLORS["blue"], fg=COLORS["light_gray"])
        result.place(x=10, y=90, width=100, height=30)


        first_text = Entry(calculator, bg=COLORS["light_gray"], fg=COLORS["dark_blue"], highlightthickness=1, highlightbackground=COLORS["blue"], highlightcolor=COLORS["yellow"], borderwidth=0)
        first_text.place(x=120, y=10, width=100, height=30)
        
        second_text = Entry(calculator, bg=COLORS["light_gray"], fg=COLORS["dark_blue"], highlightthickness=1, highlightbackground=COLORS["blue"], highlightcolor=COLORS["yellow"], borderwidth=0)
        second_text.place(x=120, y=50, width=100, height=30)
        
        third_text = Entry(calculator, bg=COLORS["light_gray"], fg=COLORS["dark_blue"], highlightthickness=1, highlightbackground=COLORS["blue"], highlightcolor=COLORS["yellow"], borderwidth=0)
        third_text.place(x=120, y=90, width=100, height=30)

        button_result = Button(calculator, text="Calcular", command=suma)
        button_result.config(bg=COLORS["dark_blue"],highlightbackground=COLORS["light_gray"], fg=COLORS["light_gray"], relief="flat", cursor="hand2", activeforeground=COLORS["dark_blue"], focuscolor=COLORS["dark_blue"])
        button_result.place(x=10, y=130, width=220, height=30)
        button_result.bind("<Enter>", on_enter)
        button_result.bind("<Leave>", on_leave)



if __name__ == "__main__":
    window=Tk()
    aplication = Calculator(window)
    window.mainloop()
