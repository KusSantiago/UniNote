# ------------------- Código de ventana Inicial de UniNote -----------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 16/08/2024 23:12:43
# Última Actualización: 20/08/2024 21:58:25
#
# El código no está privatizado por ninguna declaración oficial, pero se pide una referencia en el uso exterior
#
# Resumen:

# ------------------- Imports -----------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from file_manager import FileManager
from edition_window import EditionWindow
from app_conf import *


# ------------------- Definición de la Clase De Ventana de Lectura ----
class ReadWindow:
    def __init__(self, notename:str):
        #Se guarda el nombre de la nota cargada con la ventana
        self.notename = notename

        # ------------------- Definición de la Ventana ---------------------
        self.window = tk.Tk()
        self.window.geometry('700x500+100+110')
        self.window.title(notename + ' - Solo Lectura - UniNote')
        self.window.resizable(False, False)
        self.window.grid_propagate(False)

        #Se crea un gestor de archivos para la ventana
        self.fmanager = FileManager()

        # ------------------- Definición del Menu para la Ventana ----------
        #Se desactiva la opción visual de Tearoff para evitar las lineas de separación de lineas en el menu
        self.window.option_add('*tearOff', False)

        #Se crea el menú y se añade a la ventana
        self.menubar = tk.Menu(self.window, ReadWindow_menubar_confDitc)
        self.window['menu'] = self.menubar

        #Se crea un sub nivel de menú y se los agrega al menu de la ventana
        self.archive_menu = tk.Menu(self.menubar, ReadWindow_edition_menu_confDitc)
        self.menubar.add_cascade(menu=self.archive_menu, label='Archivo')

        self.archive_menu.add_command(label='Editar\t\t\t\t', command=self.editMenuOption_event)                    #Se agrega una opción al sub-menu
        self.archive_menu.add_command(label='Abrir\t\t\t\t', command=self.openMenuOption_event)
        self.archive_menu.add_command(label='Salir\t\t\t\t', command=self.closeMenuOption_event)

        # ------------------- Definición del Cuadro de Texto ---------------
        #Se crea el area de escritura como cuerpo principal
        self.body = tk.Text(self.window, ReadWindow_body_confDitc)
        self.body.configure(width=600, wrap='word', state='normal')
        self.body.grid(column=0, row=0, padx=3, sticky='nwes')

        #Se asocia un evento de doble click al texto completo para poder presionar y abrir el modo de edición
        self.body.bind('<Double-Button-1>', self.dobleClickBody_event)

        #Se crea una barra de desplazamiento vertical para el cuerpo de texto
        self.body_yscroolbar = ttk.Scrollbar(self.window, orient='vertical', command=self.body.yview)
        self.body_yscroolbar.grid(column=1, row=0, padx=2, sticky='ns')

        self.body['yscrollcommand'] = self.body_yscroolbar.set          #Se configura el par de funciones de actulización de la barra de desplazamiento

        #Se ajustan las relaciones de tamaño para que se coloque bien los componentes
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        #Se configuran las etiquetas de texto a usar
        self.body.tag_configure('Common', ReadWindow_Common_tag)
        self.body.tag_configure('Title', ReadWindow_Title_tag)
        self.body.tag_configure('Subtitle', ReadWindow_Subtitle_tag)
        self.body.tag_configure('Bold', ReadWindow_Bold_tag)
        self.body.tag_configure('Italic', ReadWindow_Italic_tag)
        self.body.tag_configure('Reference', ReadWindow_Reference_tag)

        #Se asigna un evento propio al clickear una palabra con la etiqueta de referencia
        self.body.tag_bind('Reference', '<Double-Button-1>', self.dobleClickReference_event)

        #Se carga el texto de la nota abierta a el cuerpo de la ventana
        text = self.fmanager.readFile(notename)
        self.formatText(text)

        #Se bloque la edición en el cuerpo
        self.body['state'] = 'disabled'

        # ------------------- Definición del Footer ------------------------
        #Se crea el marco del footer y se coloca despues del cuadro de texto en el pie de la ventana
        self.footer = tk.Frame(self.window, ReadWindow_footer_confDitc)
        self.footer.configure(width=700, height=30)

        self.footer.grid(column=0, columnspan=2, row=1, sticky='we')
        self.footer.pack_propagate(False)           #Se configura las opciones de .pack() para evitar que despues al agregar la Label se cambie el tamaño


        #Se agrega una label con el texto al final del Footer
        self.footer_lb = tk.Label(self.footer, Readwindow_footer_lb_confDitc)
        self.footer_lb.configure(text='Doble Click En El Texto Para Editar')
        self.footer_lb.pack(side='right')

        # ------------------- Se ejecuta la ventana ------------------------
        self.window.mainloop()


    def dobleClickReference_event(self, event:tk.Event):
        #Se obtiene los indices en el texto de la nota referenciada
        reference_start_index = self.body.index('current' + ' wordstart')
        reference_end_index = self.body.index('current' + ' wordend')

        #Se extrae el nombre del texto
        referenced_note = self.body.get(reference_start_index, reference_end_index)

        #Se consigue la lista de notas en el directorio raiz
        notes_list = self.fmanager.listFiles()

        #Se comprueba que el nombre corresponda a una nota
        if referenced_note in notes_list:
            #Se crea una nueva instancia de ventana de lectura y se destuye esta instancia pasando la referencia a la ventana de inicio
            self.window.destroy()
            new_read_window = ReadWindow(referenced_note)
        else:
            #Se informa un error de que la nota no corresponde a ninguna guardada
            print('No se encontró la nota')
        

    def dobleClickBody_event(self, event:tk.Event):
        #Se cierra la ventana y se abre una instancia de ventana de edición
        self.window.destroy()

        new_edition_window = EditionWindow(self.notename)

    def editMenuOption_event(self):
        #Se cierra la ventana y se abre una instancia de ventana de edición
        self.window.destroy()

        new_edition_window = EditionWindow(self.notename)

    def openMenuOption_event(self):
        #Se abre una ventana de gestor de archivos pidiendo abrir el nuevo archivo dentro del directorio raiz
        notefile = filedialog.askopenfile(defaultextension='.txt', initialdir=self.fmanager.DocDirPath)
        notefile.close()
        
        #Se extrae el nombre del archivo
        notename = notefile.name.partition(self.fmanager.DocDirPath)[2]             #Se separa haciendo una particicón con el nombre del directorio raiz y tomando la última parte de la lista
        notename = notename.removesuffix('.txt')

        #Se crea una nueva ventana de lectura abriendo el archivo especificado
        self.window.destroy()
        new_read_window = ReadWindow(self.home_window, notename)

    def closeMenuOption_event(self):
        #Se cierra esta ventana de ejecución y se abre la ventana de inicio
        self.window.destroy()

    def formatText(self, text:str) -> None:
        #Se separa el texto de la nota en partes por lineas individuales
        splited_text = text.split('\n')
        #Se analiza el formato de cada linea
        for line in splited_text:
            #Se obtiene con que etiqueta se corresponde la linea
            line_tag = self.tagRecognize(line)

            if type(line_tag) == type(()):
                self.body.insert('end', line_tag[0] +'\n', [line_tag[1]])

            if type(line_tag) == type([]):
                for line in line_tag:
                    self.body.insert('end', line[0], [line[1]])
                
                self.body.insert('end', '\n')

    def tagRecognize(self, line:str) -> list[tuple[str, str]] | tuple[str, str] | None:

        #Se comprueba para etiquetas de título
        if line.startswith('##') and line.endswith('##'):
            #Se elimina los caracteres de edición y se pasa la nueva linea
            formated_line = line.removeprefix('##').removesuffix('##')
            return (formated_line, 'Title')
        
        #Se comprueba para etiquetas de subtítulo
        if line.startswith('#') and line.endswith('#'):
            #Se elimina los caracteres de edición y se pasa la nueva linea
            formated_line = line.removeprefix('#').removesuffix('#')
            return (formated_line, 'Subtitle')
        
        #Para comprobar si existen alteraciones en negrita o italica o refrencias a otras notas dentro del texto se analiza letra a letra
        #Se guarda en una pila el caracter de reconocimiento y el indice donde se encuentra
        symbols_stack: list[tuple[str, int]] = [('&', 0)]

        index = 0
        for char in line:
            if char == '*' or char == '~' or char == '_':
                symbols_stack.append((char, index))
            index += 1
        symbols_stack.append(('&', len(line)))          #Se estakea el último caracter para formar

        #Se toma el último elemento y se desapila elementos hasta encontrar un par del tomado, se genera un 
        #nuevo string a partir de los indeces y se le da la etiqueta correspondiente al simbolo y
        #se toma el siguiente simbolo en la pila para el mismo procedimiento, hasta que no queden simbolos
        #Se acumulan en una lista para despues devolver
        tag_list:list[tuple[str, str]] = []

        iterator = len(symbols_stack)

        selec_sym, selec_i = symbols_stack.pop(0)
        iterator -= 1
        while(iterator != 0):
            sym, i = symbols_stack.pop(0)

            if selec_sym == '_' and selec_sym == sym:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('_', '')
                tag_list.append((tag_line, 'Reference'))

                selec_sym = sym
                selec_i = i

            if selec_sym == '_' and sym in ['*', '~']:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('*', '').replace('~', '').replace('_', '')
                tag_list.append((tag_line, 'Common'))

                selec_sym = sym
                selec_i = i

            if selec_sym == '~' and selec_sym == sym:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('~', '')
                tag_list.append((tag_line, 'Italic'))

                selec_sym = sym
                selec_i = i

            if selec_sym == '~' and sym in ['*', '_']:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('*', '').replace('~', '').replace('_', '')
                tag_list.append((tag_line, 'Common'))

                selec_sym = sym
                selec_i = i

            if selec_sym == '*' and selec_sym == sym:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('*', '')
                tag_list.append((tag_line, 'Bold'))

                selec_sym = sym
                selec_i = i

            if selec_sym == '*' and sym in ['_', '~']:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('*', '').replace('~', '').replace('_', '')
                tag_list.append((tag_line, 'Common'))

                selec_sym = sym
                selec_i = i

            if selec_sym == '&' and selec_sym == sym:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('*', '').replace('~', '').replace('_', '')
                tag_list.append((tag_line, 'Common'))

                selec_sym = sym
                selec_i = i

            if selec_sym == '&' and sym in ['~', '*', '_']:
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('*', '').replace('~', '').replace('_', '')
                tag_list.append((tag_line, 'Common'))

                selec_sym = sym
                selec_i = i

            if selec_sym in ['~', '*', '_'] and sym == '&':
                tag_line = line[selec_i:i]
                tag_line = tag_line.replace('*', '').replace('~', '').replace('_', '')
                tag_list.append((tag_line, 'Common'))

                break

            iterator -= 1

        return tag_list
        


test = ReadWindow('prueba')