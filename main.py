# ------------------- Programa Principal de UniNote -------------------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 11/08/2024 10:59:03
# Última Actualización: 21/08/2024 22:51:02
#
# El código no está privatizado por ninguna declaración oficial, pero se pide una referencia en el uso exterior
#
# Resumen: Se inicializan todos los modulos de utilidades y se presenta la pantalla de inicio.


# ------------------- Imports -----------------------------------------
import tkinter as tk
import os

from tkinter import ttk
from tkinter import filedialog

from source.app_conf import *
from source.file_manager import FileManager
from source.app_setup import dirSetUp
from source.home_window import HomeWindow


# ------------------- Función Principal -------------------------------
def main():
    dirSetUp()

    homw_window = HomeWindow()

# ------------------- Inicio de la Función Principal ------------------
if __name__ == '__main__':
    main()