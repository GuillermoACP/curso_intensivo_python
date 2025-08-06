'''
2-8. Extensiones de archivo Python tiene un método llamado removesuffix() que funciona igual que removeprefix(). Asigna 'python_notes.txt' a una variable llamada nombre_archivo, y luego usa removesuffix() para mostrar el nombre del archivo sin la extensión, como hacen algunos exploradores de archivos.
'''

nombre_archivo = 'python_notes.txt'
nombre_simple = nombre_archivo.removesuffix('.txt')

print(nombre_simple)
