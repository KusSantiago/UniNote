# ------------------- Programa Principal de UniNote -------------------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 27/08/2024 09:42
# Última Actualización: 
#
# El código no está privatizado por ninguna declaración oficial, pero se pide una referencia en el uso exterior
#
# Resumen: Se definen funciones usadas para estructurar un directorio propio en el sistema del usuario

# ------------------- Imports -----------------------------------------
import os

# ------------------- Declaración de Funciones ------------------------
def dirSetUp():
    #Se obtiene un camino que expande de los documentos del usuario a la raiz
    dirpath = os.path.expanduser('~/Documents/UniNote/')

    #Se comprueba si existe el directorio o no
    if  not os.path.exists(dirpath):
        #Si no existe, se asume nunca fue "Instalada" entonces se crea el directorio
        os.mkdir(dirpath)

