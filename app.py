#Se ejecuta intento de trabajar ventanas en HD, solo disponible en Windows (por eso el "try-except")
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from otro_frame import Frame_2

from general_styles import COLORS

class APP(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("1000x500")
        self.config(bg=COLORS["light_gray"])
        #Cambiar "font" por defecto a todo (ojo con forma de importar libreria arriba)
        font.nametofont("TkDefaultFont").configure(size = 14, underline = True)
        self.title("Una aplicación con TkInter")
        #Se busca que Ventana se mantenga central y correcta independiente del tamanno y expansiones realizadas:
        self.columnconfigure( 0, weight=1)
        self.rowconfigure(0, weight=1)

        #Se crea el "CONTENEDOR PRINCIPAL", el cual es un Frame en donde se llamaran a otros Frames de las otras clases...
        #...esto nos permitira tener el efecto de multiples ventanas segun la que se necesita (osea el frame respectivo)
        main_container = tk.Frame( self ,bg=COLORS["yellow"])
        main_container.grid( padx=40,pady=50, sticky="nsew")

        #IMPORTANTE (CREACION DE DICCIONARIO CON FRAMES A UTILIZAR EN APP --> TODAS LAS FRAMES QUE SE TENGAN):
        self.all_frames = dict()

        for F in (Frame_1, Frame_2):
            frame = F( main_container , self)
            self.all_frames[F] = frame
            #NOTA: FUNDAMENTAL crear frames con sticky = "nsew", para que no aparezcan cosas de otros frames indeseadas
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        #luego se debe llamar al metodo "show_frame", creado por nosotros, para mostrar un frame deseado...
        #...en esencia, permite traer al primer plano, un frame del vector "self.todos+los_frames"
        self.show_frame( Frame_1 )

    #METODO PARA MOSTRAR UNICAMENTE FRAME DESEADO (controller = Clase que queremos obtener de diccionario de frames)
    def show_frame(self,contenedor_llamado):
        frame = self.all_frames[contenedor_llamado]
        #Se agrega funcionalidad al presionar "ENTER" y "ENTER NUMERICO"
        #Estos "bind" SOLAMENTE se pueden agregar aqui, y debe generalizarse su funcion, pues no hay otra forma de...
        #... diferenciar en que ventana hace efecto el enter
        self.bind( "<Return>", frame.saludarme )
        self.bind( "<KP_Enter>", frame.saludarme )

        #Se elimina lo escrito en el label del frame respectivo (asociado al saludo)
        frame.L_3.configure( text = "" )
        frame.entrada_usuario.set( "" )
        frame.E_1.focus()
        
        #Ahora se llama a funcion de tkinter heredada desde clase APP, la cual permite traer frame indicada a primer plano
        frame.tkraise()

#( CREACION DE FRAMES)
#Se crean como clases con herencia de tk.Frame (para acceder inmediatamente a las clases Frames respectivas)
class Frame_1(tk.Frame):
    def __init__(self, container, controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = "yellow")

        #Agregamos Widgets
        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label( self, text = "MI PRIMER FRAME CON POO Y TKINTER", font = ("Times New Roman",14,"bold"),bg = "yellow",fg = "blue" )
        L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
        L_2 = tk.Label( self, text = "Ingrese Nombre: ", font = ("Times New Roman",12),bg = "yellow" )
        L_2.grid(row = 1, column = 0, sticky = "w")

        #Notar que entry debe tener como variable, la definida como "self.entrada_usuario". Se crea con "self", para acceder a ella en metodos
        self.E_1 = ttk.Entry( self, textvariable = self.entrada_usuario )
        self.E_1.focus()
        self.E_1.grid(row = 1, column = 1, columnspan = 2, padx = (0,10))

        #esto nos permitira acceder a metodos en clases, al interactuar con widgets. Es mas organizado segun clase (Frame)
        B_1 = ttk.Button( self, text = "SALUDARME" , command = self.saludarme )
        B_1.grid(row = 1, column = 3, sticky = "e")

        #OJO: este label es variable, por lo que lo creamos con "self.", para poder acceder a el con metodos de la clase
        self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman",12,"bold"),bg = "yellow" )
        self.L_3.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")

        #Crear boton para cambio de paginas entre Frames:
        #NOTA: como se debe acceder a metodo "show_frame" desde otra clase, por eso se debe pasar "controller"
        B_2 = ttk.Button( self, text = "ingles", command = lambda:controller.show_frame( Frame_2 ) )
        B_2.grid(row = 3, column = 0)

    #Se debe agregar "*args", porque esta funcion ademas puede ser llamada a traves de darle "enter" al teclado...
    #...para lograr esto, se requiere pasar funcion con parametros a traves de "bind" (ver self.bind() en clase principal)
    def saludarme(self, *args):
        self.L_3.configure( text = "Buenos Dias : {}.".format( self.entrada_usuario.get() ) )

    
#Se crea Frame_2 (similar a primera, pero con idioma ingles)
# class Frame_2(tk.Frame):
#     def __init__(self, container,controller,*args, **kwargs):
#         super().__init__(container, *args, **kwargs)
#         self.configure(bg = "yellow")
#         self.entrada_usuario = tk.StringVar()

#         L_1 = tk.Label( self, text = "MI FIRST FRAME WITH OOP AND TKINTER", font = ("Times New Roman",14,"bold"),bg = "yellow",fg = "blue" )
#         L_1.grid(row = 0, column = 0, columnspan = 4, sticky = "n")
#         L_2 = tk.Label( self, text = "Entry name: ", font = ("Times New Roman",12),bg = "yellow" )
#         L_2.grid(row = 1, column = 0, sticky = "w")

#         self.E_1 = ttk.Entry( self, textvariable = self.entrada_usuario )
#         self.E_1.focus()
#         self.E_1.grid(row = 1, column = 1, columnspan = 2, padx = (0,10))

#         B_1 = ttk.Button( self, text = "SAY HI" , command = self.saludarme )
#         B_1.grid(row = 1, column = 3, sticky = "e")

#         self.L_3 = tk.Label( self, textvariable = "", font = ("Times New Roman",12,"bold"),bg = "yellow" )
#         self.L_3.grid(row = 2, column = 0, columnspan = 4, sticky = "nsew")

#         B_2 = ttk.Button( self, text = "espannol", command = lambda:controller.show_frame( Frame_1 ) )
#         B_2.grid(row = 3, column = 0)
    
#     def saludarme(self, *args):
#         self.L_3.configure( text = "Good Morning, {}.".format( self.entrada_usuario.get() ) )


if __name__ == "__main__":
    #Se crea APP como tal (aprovechandonos de la clase creada)
    root = APP()

    #Se ejecuta la ventana principal, creada a traves de POO con las clases respectivas
    root.mainloop()