# ------------------- Código de Administrador de Archivos -------------
# Autor: Kus Santiago
# Dirección de Contacto: kussantiago29@gmail.com
# Fecha de Creación: 11/08/2024 11:12:05
# Última Actualización: 13/08/2024 17:54:01
#
# El código no está privatizado por ninguna declaración oficial, pero se pide una referencia en el uso exterior
#
# Resumen:


# ------------------- Imports -----------------------------------------
import os


# ------------------- Definición de Clase Administrador de Archivos ---
class FileManager:
    def __init__(self):
        self.DocDirPath: str = 'docs/'

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
