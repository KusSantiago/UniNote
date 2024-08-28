# ------------------- Programa Principal de UniNote -------------------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 11/08/2024 10:59:03
# Última Actualización: 21/08/2024 22:51:02
#
# El código está cubrido por la licencia GPL, quisiera ser nombrado por Sanyus a la hora de shoutouts,
# espero llegue a personas que si saben tkinter para que le den un retoque de pintura a los widgets
#
# Resumen: Se compila todo el código y se integra en un solo producto que se ejecuta como un scrypt de python

# ------------------- Imports -----------------------------------------
import tkinter as tk
import os

from tkinter import ttk
from tkinter import filedialog

# ------------------- / ------------------- / ------------------- / ---
#       app_conf.py
# ------------------- / ------------------- / ------------------- / ---

# ------------------- Componentes de Ventana de Inicio ------------------------

# ------------------- HomeWindow::header ------------------------------
HomeWindow_header_confDict = {
    'bg': '#e5eaca'
}

# ------------------- HomeWindow::newNote_bt --------------------------
HomeWindow_newNote_bt_confDict = {
    'bg': '#c7cbb1',
    'relief': 'groove'
}

# ------------------- HomeWindow::delNote_bt --------------------------
HomeWindow_delNote_bt_confDict = {
    'bg': '#c7cbb1',
    'relief': 'groove'
}

# ------------------- HomeWindow::accept_bt ---------------------------
HomeWindow_accept_bt_confDict = {
    'bg': 'green',
    'relief': 'groove'
}

# ------------------- HomeWindow::deny_bt -----------------------------
HomeWindow_deny_bt_confDict = {
    'bg': 'red',
    'relief': 'groove'
}

# ------------------- HomeWindow::body --------------------------------
HomeWindow_body_confDict = {
    'font': ('Ebrima', 16, 'italic'),
    'background': '#b9bcbc',
    'selectborderwidth': 2,
    'selectforeground': 'black',
    'activestyle': 'none'
}

# ------------------- Componentes de Ventana de Lectura -----------------------

# ------------------- ReadWindow::Menubar -----------------------------
ReadWindow_menubar_confDitc = {
    'bg': '#c7cbb1'
}

# ------------------- ReadWindow::edition_menu ------------------------
ReadWindow_edition_menu_confDitc = {

}

# ------------------- ReadWindow::body --------------------------------
ReadWindow_body_confDitc = {
    'borderwidth': 2,
    'font': ('Console', 12),
    'relief': 'groove'
}

# Common Tag Configuration
ReadWindow_Common_tag = {
    'font': ('Console', 12),
    'justify': 'left',
    'wrap': 'word'
}
# Title Tag Configuration
ReadWindow_Title_tag = {
    'font': ('Console', 22, 'bold', 'underline'),
    'justify': 'left',
    'spacing1': 10,
    'spacing3': 25,
    'wrap': 'word'
}
# Subtitle Tag Configuration
ReadWindow_Subtitle_tag = {
    'font': ('Console', 18, 'bold'),
    'justify': 'left',
    'spacing1': 10,
    'spacing3': 15,
    'wrap': 'word'
}
# Bold Tag Configuration
ReadWindow_Bold_tag = {
    'font': ('Console', 12, 'bold'),
    'justify': 'left',
    'wrap': 'word'
}
# Italic Tag Configuration
ReadWindow_Italic_tag = {
    'font': ('Console', 12, 'italic'),
    'justify': 'left',
    'wrap': 'word'
}
# Reference Tag Configuration
ReadWindow_Reference_tag = {
    'font': ('Console', 12),
    'justify': 'left',
    'wrap': 'word',
    'foreground': 'blue',
    'underline': True,
    'underlinefg': 'blue'
}

# ------------------- ReadWindow::footer ------------------------------
ReadWindow_footer_confDitc = {
    'bg': '#c7cbb1'
}

# ------------------- ReadWindow::footer_lb ---------------------------
Readwindow_footer_lb_confDitc = {
    'font': ('Ebrima', 12),
    'justify': 'right',
    'bg': '#c7cbb1'
}


# ------------------- Componentes de Ventana de Edición ------------------------

# ------------------- EditionWindow::menubar --------------------------
EditionWindow_menubar_confDitc = {

}

# ------------------- EditionWindow::archive_menu ---------------------
EditionWindow_archive_menu_confDitc = {

}

# ------------------- EditionWindow::edition_menu ---------------------
EditionWindow_edition_menu_confDitc = {
    
}

# ------------------- EditionWindow::help_menu ---------------------
EditionWindow_help_menu_confDitc = {
    
}

# ------------------- EditionWindow::body -----------------------------
EditionWindow_body_confDitc = {
    'borderwidth': 2,
    'font': ('Console', 12),
    'wrap': 'word',
    'relief': 'groove',
    'undo': True
}

# Highlight Tag Configuration
EditionWindow_Highlight_tag = {
    'background': 'light blue',
    'foreground': 'black',
    'selectbackground': 'blue',
    'selectforeground': 'white'
}

# ------------------- EditionWindow::footer ---------------------------
EditionWindow_footer_confDict = {
    'bg': '#c7cbb1'
}

#font=('Open-sans 12'), bg='#c7cbb1'
# ------------------- EditionWindow::saveWarning_lb -------------------
EditionWindow_saveWarning_lb_confDitc = {
    'font': ('Open-sans 12'),
    'bg': '#c7cbb1'
}

# ------------------- EditionWindow::line_lb -------------------
EditionWindow_line_lb_confDitc = {
    'font': ('Open-sans 12'),
    'bg': '#c7cbb1'
}

# ------------------- EditionWindow::column_lb -------------------
EditionWindow_column_lb_confDitc = {
    'font': ('Open-sans 12'),
    'bg': '#c7cbb1'
}

# ------------------- Componentes del Dialogo de Busqueda ---------------------

# ------------------- SearchDialog::window ---------------------------
SearchDialog_window_confDitc = {

}

# ------------------- SearchDialog::entry_lb --------------------------
SearchDialog_entry_lb_confDitc = {
    'justify': 'left'
}

# ------------------- SearchDialog::word_entry ------------------------
SearchDialog_word_entry_confDitc = {
    'relief': 'groove'
}

# ------------------- SearchDialog::action_bt -------------------------
SearchDialog_action_bt_confDitc = {

}

# ------------------- SearchDialog::info_lb ---------------------------
SearchDialog_info_lb_confDitc = {
    'justify': 'left',
    'foreground': 'red'
}


# ------------------- Componentes del Dialogo de Reemplazar ---------------------------

# ------------------- GoToDialog::window ---------------------------
ReplaceDialog_window_confDitc = {

}

# ------------------- GotoDialog::word_lb --------------------------
ReplaceDialog_word_lb_confDitc = {
    'justify': 'left'
}

# ------------------- GotoDialog::word_entry ------------------------
ReplaceDialog_word_entry_confDitc = {
    'relief': 'groove'
}

# ------------------- GotoDialog::replace_lb --------------------------
ReplaceDialog_replace_lb_confDitc = {
    'justify': 'left'
}

# ------------------- GotoDialog::replace_entry ------------------------
ReplaceDialog_replace_entry_confDitc = {
    'relief': 'groove'
}

# ------------------- GoToDialog::action_bt -------------------------
ReplaceDialog_action_bt_confDitc = {

}

# ------------------- GoToDialog::info_lb ---------------------------
ReplaceDialog_info_lb_confDitc = {
    'justify': 'left',
    'foreground': 'red'
}



# ------------------- Componentes del Dialogo de Ir ---------------------------

# ------------------- GoToDialog::window ---------------------------
GoToDialog_window_confDitc = {

}

# ------------------- GotoDialog::entry_lb --------------------------
GoToDialog_entry_lb_confDitc = {
    'justify': 'left'
}

# ------------------- GotoDialog::word_entry ------------------------
GoToDialog_word_entry_confDitc = {
    'relief': 'groove'
}

# ------------------- GoToDialog::action_bt -------------------------
GoToDialog_action_bt_confDitc = {

}

# ------------------- GoToDialog::info_lb ---------------------------
GoToDialog_info_lb_confDitc = {
    'justify': 'left',
    'foreground': 'red'
}

# ------------------- / ------------------- / ------------------- / ---
#       app_setup.py
# ------------------- / ------------------- / ------------------- / ---

# ------------------- Declaración de Funciones ------------------------
dirpath = ''

def dirSetUp():
    #Se obtiene un camino que expande de los documentos del usuario a la raiz
    global dirpath
    dirpath = os.path.expanduser('~/Documents/UniNote/')

    #Se comprueba si existe el directorio o no
    if  not os.path.exists(dirpath):
        #Si no existe, se asume nunca fue "Instalada" entonces se crea el directorio
        os.mkdir(dirpath)


# ------------------- / ------------------- / ------------------- / ---
#       file_manager.py
# ------------------- / ------------------- / ------------------- / ---


# ------------------- Definición de Clase Administrador de Archivos ---
class FileManager:
    def __init__(self):
        global dirpath
        self.DocDirPath: str = dirpath

    def listFiles(self) -> list[str]:
        try:
            #Extraer todos los documentos en el directorio de Notas
            files = os.listdir(self.DocDirPath)

            #Separar aquellos que si cumplan el formato .txt
            txt_files = []
            for file in files:
                if file.find('.txt') > 0:
                    file = file.removesuffix('.txt')
                    txt_files.append(file)

            return txt_files

        except IOError:
            print('No se pudo leer el directorio')

    def readFile(self, filename:str) -> str:
        #Se cargan los archivos .txt del directorio
        txt_files = self.listFiles()

        #Se encuentra el archivo especificado en los del directorio
        if filename not in txt_files:
            return 'No se ha Encontrado'
        
        #Se abre el archivo pedido en función del directorio raíz de los archivos y se lee su contenido total
        filepath = self.DocDirPath + filename + '.txt'
        with open(filepath) as f:
            text = f.read()
            f.close()

        return text

    def createFile(self, filename:str) -> None:
        #Se crea un archivo en función del directorio raíz
        filepath = self.DocDirPath + filename + '.txt'
        file = open(filepath, 'x')
        file.close()

    def writeFile(self, filename:str, text:str) -> None:
        #Se abre el archivo en función del directorio raíz
        filepath = self.DocDirPath + filename + '.txt'
        with open(filepath, 'w') as f:
            #Se excribe el contenido dado, sobreescribiendo todo el archivo
            f.write(text)
            f.close()

    def deleteFile(self, filename:str) -> None:
        #Se arma el path para el archivo y se comprueba que exista
        filepath = self.DocDirPath + filename + '.txt'
        if os.path.exists(filepath):
            #Se Elimina 
            os.remove(filepath)
        else:
            print('El Archivo No Existe')


# ------------------- / ------------------- / ------------------- / ---
#       edition_window.py
# ------------------- / ------------------- / ------------------- / ---


# ------------------- Definición de Clase Ventana de Edición ----------
class EditionWindow:
    def __init__(self, notename:str):
        #Se guarda el nombre de la nota
        self.notename = notename

        #Se crea una gestor de archivos para la ventana
        self.fmanager = FileManager()

        #Se crea una variables para mantener constancia de cambios en el texto cargado
        self.TextEdited = False
        
        # ------------------- Definición de la Ventana ---------------------
        self.window = tk.Tk()
        self.window.geometry('700x500+100+110')
        self.window.title(notename + ' - Edición - UniNote')
        self.window.resizable(False, False)
        self.window.grid_propagate(False)
        self.window.option_add('*tearOff', False)

        self.window.protocol('WM_DELETE_WINDOW', self.closeMenuOption)

        # ------------------- Definición del Menu de la Ventana ------------
        self.menubar = tk.Menu(self.window, EditionWindow_menubar_confDitc)
        self.window['menu'] = self.menubar

        self.archive_menu = tk.Menu(self.menubar, EditionWindow_archive_menu_confDitc)
        self.archive_menu.add_command(label='Guardar', command=self.saveMenuOption)
        self.archive_menu.add_command(label='Salir', command=self.closeMenuOption)

        self.edition_menu = tk.Menu(self.menubar, EditionWindow_edition_menu_confDitc)
        self.edition_menu.add_command(label='Buscar', command=self.searchMenuOption)
        self.edition_menu.add_command(label='Reemplazar', command=self.replaceMenuOption)
        self.edition_menu.add_command(label='Ir a', command=self.gotoMenuOption)

        self.help_menu = tk.Menu(self.menubar, EditionWindow_help_menu_confDitc)
        self.help_menu.add_command(label='Guia')

        self.menubar.add_cascade(menu=self.archive_menu, label='Archivo')
        self.menubar.add_cascade(menu=self.edition_menu, label='Edición')
        self.menubar.add_cascade(menu=self.help_menu, label='Ayuda')

        #Se enlaza combinaciones de teclas a la ventana para acceder rapidamente a las funciones del menu
        self.quickCommand_bindings: dict[str, str] | dict[str, None] = {'saveMenuOption': None,
                                                                        'searchMenuOption': None,
                                                                        'replaceMenuOption': None,
                                                                        'gotoMenuOption': None}
        self.setBindings()
        
        # ------------------- Definición del Cuerpo de Texto ---------------
        self.body = tk.Text(self.window, EditionWindow_body_confDitc)
        self.body.configure(width=600, height=25)
        self.body.grid(column=0, row=0, padx=3, sticky='nwes')

        self.body_yscrollbar = ttk.Scrollbar(self.window, orient='vertical')
        self.body_yscrollbar.grid(column=1, row=0, padx=2, sticky='ns')

        self.window.grid_columnconfigure(index=0, weight=1)
        self.window.grid_rowconfigure(index=0, weight=1)

        #Se crea una etiqueta de destacado de palabras
        self.body.tag_config('Highlight', EditionWindow_Highlight_tag)

        self.setBodyInteraction()

        #Se carga el texto de la nota con la que se abrio la ventana, y se guarda para poder comparar el texto en caso de producir cambios
        self.original_text = self.fmanager.readFile(notename)
        self.body.insert('1.0', self.original_text)

        # ------------------- Definición del Footer ------------------------
        #Se define el un marco para el footer
        self.footer = tk.Frame(self.window, EditionWindow_footer_confDict)
        self.footer.configure(width=700, height=30)
        self.footer.grid(column=0, columnspan=2, row=1, sticky='we')

        #Se definen los textos(labels) dentro del footer para seguimiento de linea
        self.footer.grid_propagate(False)       #Se asegura que no se cambie el tamaño del marco del footer

        #Se obtiene el valor del cursor en el final del texto
        end_index = self.body.index('end').split('.')

        #Se crean variables de texto para usar en los labels y su correpondiente Stringvar para que puedan ser interpretados por tkinter
        self.saveWarning_str = ''
        self.line_str = 'Ln ' + end_index[0]
        self.column_str = 'Col ' + end_index[1]

        self.saveWarning_strVar = tk.StringVar(value=self.saveWarning_str)
        self.line_strVar = tk.StringVar(value=self.line_str)
        self.column_strVar = tk.StringVar(value=self.column_str)

        #Se crean labels para la alerta de guardado, numero de linea y numero de columna
        self.saveWarning_lb = tk.Label(self.footer, EditionWindow_saveWarning_lb_confDitc)
        self.saveWarning_lb['textvariable'] = self.saveWarning_strVar

        self.line_lb = tk.Label(self.footer, EditionWindow_line_lb_confDitc)
        self.line_lb['textvariable'] = self.line_strVar

        self.column_lb = tk.Label(self.footer, EditionWindow_column_lb_confDitc)
        self.column_lb['textvariable'] = self.column_strVar

        #Se crean unos separadores para los datos en el footer
        separator1 = ttk.Separator(self.footer, orient='vertical')
        separator2 = ttk.Separator(self.footer, orient='vertical')

        #Se colocan los labels y separadores en el footer
        self.saveWarning_lb.grid(column=1, row=0, padx=15, pady=2)
        separator1.grid(column=2, row=0)
        self.line_lb.grid(column=3, row=0, padx=5, pady=2)
        separator2.grid(column=4, row=0)
        self.column_lb.grid(column=5, row=0, padx=5, pady=2)

        self.footer.grid_columnconfigure(index=0, weight=1)
        

        # ------------------- Se Ejecuta la Ventana ------------------------
        self.window.mainloop()


    def updateText_event(self, event:tk.Event):
        #Se carga al footer el valor del cursor de inserción en el indice actual
        new_index = self.body.index('insert').split('.', 2)
        
        self.line_str = 'Ln ' + new_index[0]
        self.line_strVar.set(self.line_str)

        self.column_str = 'Col ' + new_index[1]
        self.column_strVar.set(self.column_str)


        if self.body.edit_modified():
            #Se actualiza el mensaje de cambios
            self.saveWarning_str = 'Hay Cambios No Guardados'
            self.saveWarning_strVar.set(self.saveWarning_str)


    def saveMenuOption(self):
        #Se extrae el texto completo en el cuerpo
        text = self.body.get('1.0', 'end')

        #Se guarda con el gestor de archivos
        self.fmanager.writeFile(self.notename, text)
        
        #Se escribe un mensaje de confirmación
        self.saveWarning_str = 'Se Ha Guardado Correctamente'
        self.saveWarning_strVar.set(self.saveWarning_str)

    def saveMenuOption_event(self, event:tk.Event):
        return self.saveMenuOption()

    def closeMenuOption(self):
        self.window.destroy()

        new_read_window = ReadWindow(self.notename)

    def searchMenuOption(self):
        #Se desactiva el uso de la tecla para abrir una nueva ventana mientras este activa
        self.clearMenuInteraction()
        #Se genera una ventana de dialogo
        new_search_dialog = SearchDialog(self)

    def searchMenuOption_event(self, event:tk.Event):
        return self.searchMenuOption()

    def replaceMenuOption(self):
        #Se desactiva el uso de la tecla para abrir una nueva ventana mientras este activa
        self.clearMenuInteraction()
        #Se genera una ventana de dialogo
        new_replace_dialog = ReplaceDialog(self)

    def replaceMenuOption_event(self, event:tk.Event):
        return self.replaceMenuOption()

    def gotoMenuOption(self):
        #Se desactiva el uso de la tecla para abrir una nueva ventana mientras este activa
        self.clearMenuInteraction()
        #Se genera una ventana de dialogo
        new_goto_dialog = GoToDialog(self)

    def gotoMenuOption_event(self, event:tk.Event):
        return self.gotoMenuOption()
    

    def setBindings(self) -> None:
        self.quickCommand_bindings['saveMenuOption'] = self.window.bind('<Control-s>', self.saveMenuOption_event)
        self.quickCommand_bindings['searchMenuOption'] = self.window.bind('<Control-j>', self.searchMenuOption_event)
        self.quickCommand_bindings['replaceMenuOption'] = self.window.bind('<Control-h>', self.replaceMenuOption_event)
        self.quickCommand_bindings['gotoMenuOption'] = self.window.bind('<Control-g>', self.gotoMenuOption_event)

    def clearBindings(self) -> None:
        self.quickCommand_bindings['saveMenuOption'] = self.window.unbind('<Control-s>', self.quickCommand_bindings['saveMenuOption'])
        self.quickCommand_bindings['searchMenuOption'] = self.window.unbind('<Control-j>', self.quickCommand_bindings['searchMenuOption'])
        self.quickCommand_bindings['replaceMenuOption'] = self.window.unbind('<Control-h>', self.quickCommand_bindings['replaceMenuOption'])
        self.quickCommand_bindings['gotoMenuOption'] = self.window.unbind('<Control-g>', self.quickCommand_bindings['gotoMenuOption'])

    def switchBinding(self, binding:str) -> None:
        if type(self.quickCommand_bindings[binding]) == type('str'):
            #Se desactiva la union
            self.quickCommand_bindings[binding] = self.window.unbind(self.quickCommand_bindings[binding]) #Se aprovecha simplemente porque la función devuelve None de por si
        elif type(self.quickCommand_bindings[binding]) == None:
            #Se une el comando
            match binding:
                case 'saveMenuOption':
                    self.quickCommand_bindings[binding] = self.window.bind('<Control-s>', self.saveMenuOption_event)
                case 'searchMenuOption':
                    self.quickCommand_bindings[binding] = self.window.bind('<Control-j>', self.searchMenuOption_event)
                case 'replaceMenuOption':
                    self.quickCommand_bindings[binding] = self.window.bind('<Control-h>', self.replaceMenuOption_event)
                case 'gotoMenuOption':
                    self.quickCommand_bindings[binding] = self.window.bind('<Control-g>', self.gotoMenuOption_event)
                
        else:
            print('No se encontró esa combinación o no existe')

    def setBodyInteraction(self) -> None:
        self.interaction_id = self.body.bind('<KeyPress>', self.updateText_event)

    def clearBodyInteraction(self) -> None:
        self.body.unbind('<KeyPress', self.interaction_id)

    def setMenuInteraction(self) -> None:
        self.archive_menu.entryconfigure(index=0, state='normal')
        self.archive_menu.entryconfigure(index=1, state='normal')

        self.edition_menu.entryconfigure(index=0, state='normal')
        self.edition_menu.entryconfigure(index=1, state='normal')
        self.edition_menu.entryconfigure(index=2, state='normal')

        self.help_menu.entryconfigure(index=0, state='normal')

    def clearMenuInteraction(self) -> None:
        self.archive_menu.entryconfigure(index=0, state='disabled')
        self.archive_menu.entryconfigure(index=1, state='disabled')

        self.edition_menu.entryconfigure(index=0, state='disabled')
        self.edition_menu.entryconfigure(index=1, state='disabled')
        self.edition_menu.entryconfigure(index=2, state='disabled')

        self.help_menu.entryconfigure(index=0, state='disabled')


class SearchDialog:
    def __init__(self, owner:EditionWindow):
        #Se crea una variable bandera para saber si se inicio una secuencia de busqueda
        self.OnSearch = False

        #Se guarda la conexión al dueño de la ventana
        self.owner = owner

        #Se desactiva la union con comando para abrir otras funcionalidades y la interacción con la pantalla hasta que se termine la operación
        self.owner.clearBindings()
        self.owner.clearBodyInteraction()

        #Se crea un widget de toplevel para usar como un ventana de dialogo y se configura
        self.window = tk.Toplevel(owner.window, SearchDialog_window_confDitc)
        self.window.geometry('300x130')
        self.window.resizable(False, False)

        self.window.bind('<Destroy>', self.onDestroy_event)

        #Se crean elemento dentro del dialogo y se colocan en un patrón de grilla
        self.entry_lb = tk.Label(self.window, SearchDialog_entry_lb_confDitc)
        self.entry_lb['text'] = 'Palabra: '
        self.entry_lb.grid(column=0, row=0, padx=10, pady=10)

        self.entry_str:str = ''
        self.entry_strVar = tk.StringVar(value=self.entry_str)

        self.word_entry = tk.Entry(self.window, SearchDialog_word_entry_confDitc)
        self.word_entry['textvariable'] = self.entry_strVar

        self.word_entry.grid(column=1, row=0, padx=5, pady=10)

        self.action_bt = tk.Button(self.window, SearchDialog_action_bt_confDitc)
        self.action_bt.configure(text='Buscar', command=self.searchButton_event)
        self.action_bt.grid(column=1, row=1, padx=5, pady=5)

        self.info_str = ''
        self.info_strVar = tk.StringVar(value=self.info_str)

        self.info_lb = tk.Label(self.window, SearchDialog_info_lb_confDitc)
        self.info_lb['textvariable'] = self.info_strVar

        self.info_lb.grid(column=0, columnspan=3, row=2, padx=5, pady=10)

    def searchButton_event(self):
        #Se sube la abndera de sequencia de busqueda
        self.OnSearch = True

        #Se vacia el mensaje de la label de información
        self.info_str = ''
        self.info_strVar.set(self.info_str)

        #Chequea si se escribió una palabra en el entrada primero
        self.entry_str = self.entry_strVar.get()
        if self.entry_str == '':
            #Si si esta vacio se notifica y se termina la acción
            self.info_str = 'No se ingreso una palabra'
            self.info_strVar.set(self.info_str)
            
            #Se baja la bandera de secuencia de busqueda y se vuelve
            self.OnSearch = False
            return
        
        entry_len = '+ ' + str(len(self.entry_str)) + ' c'
        founded_index = '1.0'
        self.founded_indexes = []

        founded_index = self.owner.body.search(self.entry_str, founded_index, 'end', True)
        while founded_index != '':
            end_word_index = founded_index + entry_len
            self.founded_indexes.append(founded_index)

            founded_index = self.owner.body.search(self.entry_str, end_word_index, 'end', True)

        if len(self.founded_indexes) < 1:
            #Se informa que no se encontró ninguna instancia de la palabra buscada
            self.info_str = 'No se Encontró La Palabra'
            self.info_strVar.set(self.info_str)

            #Se baja la dandera de secuencia de busqueda
            self.OnSearch = False
            return
        
        #Se colocan todas las palabras en destacado todas la palabras encontradas
        for index in self.founded_indexes:
            self.owner.body.tag_add('Highlight', index, index + entry_len)
        

    def onDestroy_event(self, event:tk.Event):
        if self.OnSearch:
            #Se elimina toda las etiquetas destacadas
            entry_len = '+ ' + str(len(self.entry_str)) + ' c'
            for index in self.founded_indexes:
                self.owner.body.tag_remove('Highlight', index, index + entry_len)

        #Se recuperan los controles de la ventana de edición
        self.owner.edition_menu.entryconfig(index=0, state='normal')
        self.owner.setBindings()
        self.owner.setBodyInteraction()
        self.owner.setMenuInteraction()

        del self


class ReplaceDialog:
    def __init__(self, owner:EditionWindow):
        #Se guarda la ventana padre
        self.owner = owner

    #Se desactiva la union con comando para abrir otras funcionalidades y la interacción con la pantalla hasta que se termine la operación
        self.owner.clearBindings()
        self.owner.clearBodyInteraction()

        #Se crea un widget de toplevel para usar como un ventana de dialogo y se configura
        self.window = tk.Toplevel(owner.window, ReplaceDialog_window_confDitc)
        self.window.geometry('300x130')
        self.window.resizable(False, False)

        self.window.bind('<Destroy>', self.onDestroy_event)

        #Se crean elemento dentro del dialogo y se colocan en un patrón de grilla
        self.word_lb = tk.Label(self.window, ReplaceDialog_word_lb_confDitc)
        self.word_lb['text'] = 'Palabra: '
        self.word_lb.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        self.word_str:str = ''
        self.word_strVar = tk.StringVar(value=self.word_str)

        self.word_entry = tk.Entry(self.window, ReplaceDialog_word_entry_confDitc)
        self.word_entry['textvariable'] = self.word_strVar

        self.word_entry.grid(column=1, row=0, padx=5, pady=10, sticky='w')

        self.replace_lb = tk.Label(self.window, ReplaceDialog_replace_lb_confDitc)
        self.replace_lb['text'] = 'Reemplazo: '
        self.replace_lb.grid(column=0, row=1, padx=10, pady=10, sticky='w')

        self.replace_str:str = ''
        self.replace_strVar = tk.StringVar(value=self.replace_str)

        self.replace_entry = tk.Entry(self.window, ReplaceDialog_replace_entry_confDitc)
        self.replace_entry['textvariable'] = self.replace_strVar

        self.replace_entry.grid(column=1, row=1, padx=5, pady=10, sticky='w')

        self.action_bt = tk.Button(self.window, ReplaceDialog_action_bt_confDitc)
        self.action_bt.configure(text='Reemplazar', command=self.replaceButton_event)
        self.action_bt.grid(column=2, row=1, padx=5, pady=5)

        self.info_str = ''
        self.info_strVar = tk.StringVar(value=self.info_str)

        self.info_lb = tk.Label(self.window, ReplaceDialog_info_lb_confDitc)
        self.info_lb['textvariable'] = self.info_strVar

        self.info_lb.grid(column=0, columnspan=3, row=2, padx=5, pady=10)

    def replaceButton_event(self):
        self.word_str = self.word_strVar.get()
        if self.word_str == '':
            #Si si esta vacio se notifica y se termina la acción
            self.info_str = 'No se ingreso una palabra de busqueda'
            self.info_strVar.set(self.info_str)

            return
        
        self.replace_str = self.replace_strVar.get()
        if self.replace_str == '':
            #Si si esta vacio se notifica y se termina la acción
            self.info_str = 'No se ingreso una palabra de reemplazo'
            self.info_strVar.set(self.info_str)

            return
        

        word_len = ' + ' + str(len(self.word_str)) + ' chars'
        founded_words = []

        founded_index = self.owner.body.search(self.word_str, '1.0', 'end', True)
        while founded_index != '':
            founded_words.append(founded_index)
            
            founded_index = self.owner.body.search(self.word_str, founded_index + word_len, 'end', True)


        if len(founded_words) < 1:
            #Si no se encontró ninguna instancia de la palabra de busqueda se notifica
            self.info_str = 'No se encontró ninguna palabra para reemplazar'
            self.info_strVar.set(self.info_str)


        for word_index in founded_words:
            self.owner.body.replace(word_index, word_index + word_len, self.replace_str)


    def onDestroy_event(self, event:tk.Event):
        #Se recuperan los controles de la ventana de edición
        self.owner.edition_menu.entryconfig(index=1, state='normal')
        self.owner.setBindings()
        self.owner.setBodyInteraction()
        self.owner.setMenuInteraction()

        del self


class GoToDialog:
    def __init__(self, owner:EditionWindow):
        #Se guarda la ventana padre
        self.owner = owner

    #Se desactiva la union con comando para abrir otras funcionalidades y la interacción con la pantalla hasta que se termine la operación
        self.owner.clearBindings()
        self.owner.clearBodyInteraction()

        #Se crea un widget de toplevel para usar como un ventana de dialogo y se configura
        self.window = tk.Toplevel(owner.window, GoToDialog_window_confDitc)
        self.window.geometry('300x130')
        self.window.resizable(False, False)

        self.window.bind('<Destroy>', self.onDestroy_event)

        #Se crean elemento dentro del dialogo y se colocan en un patrón de grilla
        self.entry_lb = tk.Label(self.window, GoToDialog_entry_lb_confDitc)
        self.entry_lb['text'] = 'Ir a Palabra: '
        self.entry_lb.grid(column=0, row=0, padx=10, pady=10)

        self.entry_str:str = ''
        self.entry_strVar = tk.StringVar(value=self.entry_str)

        self.word_entry = tk.Entry(self.window, GoToDialog_word_entry_confDitc)
        self.word_entry['textvariable'] = self.entry_strVar

        self.word_entry.grid(column=1, row=0, padx=5, pady=10)

        self.action_bt = tk.Button(self.window, GoToDialog_action_bt_confDitc)
        self.action_bt.configure(text='Ir a', command=self.gotoButton_event)
        self.action_bt.grid(column=1, row=1, padx=5, pady=5)

        self.info_str = ''
        self.info_strVar = tk.StringVar(value=self.info_str)

        self.info_lb = tk.Label(self.window, GoToDialog_info_lb_confDitc)
        self.info_lb['textvariable'] = self.info_strVar

        self.info_lb.grid(column=0, columnspan=3, row=2, padx=5, pady=10)

    def gotoButton_event(self):
        self.entry_str = self.entry_strVar.get()
        if self.entry_str == '':
            #Si si esta vacio se notifica y se termina la acción
            self.info_str = 'No se ingreso una palabra'
            self.info_strVar.set(self.info_str)

            return
        
        founded_word = self.owner.body.search(self.entry_str, '1.0', 'end', True)

        if founded_word == '':
            #Se informa que no se encontró ninguna instancia de la palabra buscada
            self.info_str = 'No se Encontró La Palabra'
            self.info_strVar.set(self.info_str)

            return
        
        self.owner.body.see(founded_word)

    def onDestroy_event(self, event:tk.Event):
        #Se recuperan los controles de la ventana de edición
        self.owner.edition_menu.entryconfig(index=2, state='normal')
        self.owner.setBindings()
        self.owner.setBodyInteraction()
        self.owner.setMenuInteraction()

        del self



# ------------------- / ------------------- / ------------------- / ---
#       read_window.py
# ------------------- / ------------------- / ------------------- / ---



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

        #Se asocia un evento para la salida de la ventana
        self.window.protocol('WM_DELETE_WINDOW', self.closeMenuOption_event)

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

        new_home_window = HomeWindow()

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
        

# ------------------- / ------------------- / ------------------- / ---
#       home_window.py
# ------------------- / ------------------- / ------------------- / ---


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

        #Se cierra el archivo por seguridad##
        file.close()

        #Se corta el nombre del archivo del nombre del camino que se deriva
        # filename = file.name.removeprefix(self.fmanager.DocDirPath)        
        # filename = filename.removesuffix('.txt')

        #Se agrega a la lista de notas y se actualiza la listbox para representarla
        self.notes = self.fmanager.listFiles()
        self.body.insert(len(self.notes) - 1,self.notes[len(self.notes) - 1])

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
        
        

# ------------------- / ------------------- / ------------------- / ---
#       main.py
# ------------------- / ------------------- / ------------------- / ---

# ------------------- Función Principal -------------------------------
def main():
    dirSetUp()

    homw_window = HomeWindow()

# ------------------- Inicio de la Función Principal ------------------
if __name__ == '__main__':
    main()
