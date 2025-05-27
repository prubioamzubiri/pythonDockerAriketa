import os
import time

nombre = os.environ.get('NOMBRE', 'Estudiante')
curso = os.environ.get('CURSO', 'Docker')

print(f"Hola {nombre}!")
print(f"Bienvenido al curso de {curso}")
