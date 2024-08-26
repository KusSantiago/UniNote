# ------------------- Código de Configuración de UniNote --------------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 25/08/2024 12:33:41
# Última Actualización: 25/08/2024 22:18
#
# El código no está privatizado por ninguna declaración oficial, pero se pide una referencia en el uso exterior
#
# Resumen: Este archivo provee una fuente de configuración estetica de los widgets usados en la aplicación
# en forma de diccionarios de configuración de tkinter, no se podrán aplicar cambios al tamaño, posición
# o comportamiento, ya que estos están seteados en el momento de inicilización.
# Este archivo existe para todos aquellos conocedores de los estilos de tkinter dispuestos a mejorar
# la calidad visual de esta aplicación.


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

