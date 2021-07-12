from tkinter import Entry, Tk, Label, Button
import sqlite3

blue = "#185ADB"
white = "#ffffff"
light_gray = "#EFEFEF"
dark_blue = "#0A1931"
yellow = "#FFC947"

def message():
    print("Hola Python con TkInter")



class Application:
    def __init__(self, window):
        self.wind = window
        self.wind.geometry("240x200")
        #self.wind.config(bg=yellow)
        self.wind.title("Una aplicación con TkInter")

        def suma():
            first_value = first_text.get()
            second_value = second_text.get()

            result_sum = int(first_value) + int(second_value)
            third_text.delete(0, "end")
            third_text.insert(0, result_sum)

        first_label = Label(self.wind, text="Primer numero", bg=blue, fg=light_gray)
        first_label.place(x=10, y=10, width=100, height=30)

        second_label = Label(self.wind, text="Segunda numero", bg=blue, fg=light_gray)
        second_label.place(x=10, y=50, width=100, height=30)

        result = Label(self.wind, text="Resultado", bg=blue, fg=light_gray)
        result.place(x=10, y=90, width=100, height=30)


        first_text = Entry(self.wind, bg=light_gray, fg=dark_blue, highlightthickness=1, highlightcolor=blue, highlightbackground=blue, borderwidth=0)
        first_text.place(x=120, y=10, width=100, height=30)
        
        second_text = Entry(self.wind, bg=light_gray, fg=dark_blue, highlightthickness=1, highlightcolor=blue, highlightbackground=blue, borderwidth=0)
        second_text.place(x=120, y=50, width=100, height=30)
        
        third_text = Entry(self.wind, bg=light_gray, fg=dark_blue, highlightthickness=1, highlightcolor=blue, highlightbackground=blue, borderwidth=0)
        third_text.place(x=120, y=90, width=100, height=30)

        button_result = Button(self.wind, text="Calcular", bg=dark_blue, fg=light_gray, relief="flat", cursor="hand2", command=suma)
        button_result.place(x=10, y=130, width=220, height=30,)

        # label = Label(self.wind, text="Esto es un Label")
        # #label.pack(side="top")
        # label.config(fg="red", bg="white")
        # label.place(x=10, y=10, width=100)

        # buttonMessage = Button(self.wind, text="Presiona este botón para ver el mensaje", command=message)
        # buttonMessage.config(fg="red", bg="white", borderwidth=0, cursor="hand2")
        # buttonMessage.pack(side="bottom" )


if __name__ == "__main__":
    window=Tk()
    aplication = Application(window)
    window.mainloop()
