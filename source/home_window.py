# ------------------- Código de Pantalla Inicial de UniNote -----------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 11/08/2024 11:08:40
# Última Actualización: 25/08/2024 12:26:34
#
# El código no está privatizado por ninguna declaración oficial, pero se pide una referencia en el uso exterior
#
# Resumen:


# ------------------- Imports -----------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from file_manager import FileManager
from read_window import ReadWindow
from app_conf import *


# ------------------- Definición de Clase Ventana Pricipal ------------
class HomeWindow:
    def __init__(self):
        #Se instancia un gestor de archivos exclusivo de la ventana principal
        self.fmanager = FileManager()

        #--------------- Definición de la Ventana --------------------------
        self.window = tk.Tk()
        self.window.geometry('400x550+100+100')
        self.window.resizable(False, False)
        self.window.title('UniNote')
        self.window.grid_propagate(False)
        
        #--------------- Definición del Encabezado de la Ventana -----------
        #Crear Marco de Encabezado
        self.header = tk.Frame(self.window, HomeWindow_header_confDict)
        self.header.configure(height=60, width=400)
        self.header.grid(column=0, columnspan=2 ,row=0)

        self.header.grid_propagate(False)

        #Crear Botón de Agregar Nota
        self.newNote_bt = tk.Button(self.header, HomeWindow_newNote_bt_confDict)
        self.newNote_bt.configure(height=3, width=7, text='Nueva\nNota', command=self.clickNewNote_event)
        self.newNote_bt.grid(column=0, row=0, padx=5, pady=5)

        #Crear Botón de Eliminar Nota
        self.delNote_bt = tk.Button(self.header, HomeWindow_delNote_bt_confDict)
        self.delNote_bt.configure(height=3, width=7, text='Eliminar\nNota', command=self.clickDeleteNote_event)
        self.delNote_bt.grid(column=1, row=0, padx=5, pady=5)

        #Crear Botón Aceptar y dejarlo ocultado
        self.accept_bt = tk.Button(self.header, HomeWindow_accept_bt_confDict)
        self.accept_bt.configure(height=3, width=7, text='Aceptar', state='disabled', command=self.clickAccept_event)
        self.accept_bt.grid(column=3, row=0, padx=5, pady=5)

        #Crear Botón Cancelar y dejarlo ocultado
        self.deny_bt = tk.Button(self.header, HomeWindow_deny_bt_confDict)
        self.deny_bt.configure(height=3, width=7, text='Denegar', state='disabled', command=self.clickDeny_event)
        self.deny_bt.grid(column=4, row=0, padx=5, pady=5)

        self.header.grid_columnconfigure(index=2, weight=1)

        #Se define una variable para mantener un seguimiento de secuencias de eliminación de notas
        self.delete_sequence:bool = False

        #--------------- Definición del Cuerpo de la Ventana ---------------
        #Cargar Notas Guardadas
        self.notes = self.fmanager.listFiles()
        self.lt_notes = tk.StringVar(value=self.notes)

        #Crear cuerpo de Ventana en Listbox
        self.body = tk.Listbox(self.window, HomeWindow_body_confDict)
        self.body.configure(listvariable=self.lt_notes, height=500, width=380)
        self.body.grid(column=0, row=1)

        #Crear una barra de Desplazamiento vertical
        self.scroolbar_body = ttk.Scrollbar(master=self.window, orient=tk.VERTICAL, command=self.body.yview)
        self.body.configure(yscrollcommand=self.scroolbar_body.set)
        self.scroolbar_body.grid(column=1, row=1)

        self.window.grid_columnconfigure(index=0, weight=1)
        self.window.rowconfigure(index=1, weight=1)

        #Asociar Doble Click en un elemento de Listbox para abrir Nota
        self.body.bind('<Double-Button-1>', self.clickNote_event)

        # ------------------- Se Ejecuta la Ventana ------------------------
        self.window.mainloop()

    def clickNote_event(self, listbox):
        #Buscar que nota fue seleecionada, encontrar su nombre en el directorio, abrir una instancia de Ventana de Edición
        #y cargar el texto de la nota en la misma
        if self.delete_sequence:
            return
        
        if len(self.body.curselection()) < 1:
            return
        
        #Se busca que nota fue seleccionada
        selected_index = self.body.curselection()

        #Se verifica que se ha elegido una sola nota
        if len(selected_index) != 1:
            raise ValueError()

        #Se obtiene el nombre del archivo en el indice
        notename = self.notes[selected_index[0]]        #Indice 0 debido a que la lista debería contener solo un indice que siempre será el primero
        
    #Se abre una ventana de lectura y se oculta del escritorio y el gestor de ventanas la ventana de inicio
        self.window.destroy()
        read_window = ReadWindow(notename)

    def clickNewNote_event(self):
        #Se abre una ventana del Gestor de Archivos del SO y se pide un nombre, creando el archivo directamente
        file = filedialog.asksaveasfile(mode='x', defaultextension='.txt', initialdir=self.fmanager.DocDirPath, parent=self.window, title='New Note - UniNote', filetypes={'Text .txt'})
        
        #Se verifica que el usuario ingreso un nombre
        if file == None:
            #Si no ingreso una cadena se acaba la ejecución
            return

        #Se cierra el archivo por seguridad
        file.close()

        #Se corta el nombre del archivo del nombre del camino que se deriva
        if file.name.find(self.fmanager.DocDirPath) > 0:
            filename = file.name.partition(self.fmanager.DocDirPath)[2]         
            filename = filename.removesuffix('.txt')

        #Se agrega a la lista de notas y se actualiza la listbox para representarla
        self.notes.append(filename)
        self.body.insert(len(self.notes) - 1, filename)

        #print(filename)

    def clickDeleteNote_event(self):
        #Se levante la bandera de sequencia de eliminación
        self.delete_sequence = True

        #Se Desactivan momentaniamente los botones de acciones normales, Nueva Nota y Eliminar Nota. Desactivados hasta que se termine el proceso de eliminar notas
        self.newNote_bt['state'] = 'disabled'
        self.delNote_bt['state'] = 'disabled'

        #Se activan los botones de aceptar y cancelar para completar la eliminación
        self.accept_bt['state'] = 'normal'
        self.deny_bt['state'] = 'normal'

        #Se Cambia la configuración de la Listbox a selección múltiple y a focus de selección con punto
        self.body.configure(activestyle='dotbox', selectmode='multiple')

        #...

    def clickAccept_event(self):
        #Se extrae una lista de todos las notas seleccionadas
        selected_notes = self.body.curselection()

        #Se comprueba que existan elementos en la lista de indices
        if len(selected_notes) > 0:
            #Se eliminan todas las notas seleccionadas
            index_adjusment = 0                             #Se toma un valor 0 y se incrementa en cada iteración, se usa para acomodar los indices que van decreciendo de la lista de notas para que coincidan con los dados por el método curselection() 
            for note in selected_notes:
                self.fmanager.deleteFile(self.notes[note - index_adjusment])
                self.notes.pop(note - index_adjusment)
                index_adjusment += 1
                
            #Una vez terminada la eliminación, se actualiza la lista dentro del listbox
            self.lt_notes.set(self.notes)
        else:
            #si no se encontró ninguna, se informa
            print('No se ha seleccionado ningun archivo')

        #Se baja la bandera de sequencia de eliminación
        self.delete_sequence = False

        #Se Desactivan los botones Aceptar y Cancelar
        self.accept_bt['state'] = 'disabled'
        self.deny_bt['state'] = 'disabled'

        #Se activan los botones de acciones normales
        self.newNote_bt['state'] = 'normal'
        self.delNote_bt['state'] = 'normal'

        #Se revierte la configuración de la listbox
        self.body.configure(activestyle='none', selectmode='browse')

        #Se deselecciona todos los elemntos en el listbox
        self.body.select_clear(0, self.body.size() - 1)

    def clickDeny_event(self):
        #Se baja la bandera de sequencia de eliminación
        self.delete_sequence = False

        #Se Desactivan los botones Aceptar y Cancelar
        self.accept_bt['state'] = 'disabled'
        self.deny_bt['state'] = 'disabled'

        #Se activan los botones de acciones normales
        self.newNote_bt['state'] = 'normal'
        self.delNote_bt['state'] = 'normal'

        #Se revierte la configuración de la listbox
        self.body.configure(activestyle='none', selectmode='browse')

        #Se deselecciona todos los elemntos en el listbox
        self.body.select_clear(0, self.body.size() - 1)
        
        





test = HomeWindow()
