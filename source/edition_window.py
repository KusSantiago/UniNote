# ------------------- Código de Pantalla de Edición De uniNote --------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 11/08/2024 11:09:03
# Última Actualización: 25/08/2024 22:19:13
#
# El código no está privatizado por ninguna declaración oficial, pero se pide una referencia en el uso exterior
#
# Resumen:


# ------------------- Imports -----------------------------------------
import tkinter as tk
from tkinter import ttk
from file_manager import FileManager
from app_conf import *

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

        from read_window import ReadWindow
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



test = EditionWindow('prueba')