from biblioteca import Biblioteca
from exceptions import BibliotecaError, LibroNoDisponibleError
from libros import Libro, LibroDigital, LibroFisico
from usuarios import Estudiante, Profesor
from exceptions import UsuarioNoEncontradoError
from data import data_libros, data_estudiantes

biblioteca = Biblioteca("Platzi Biblioteca")
profesor = Profesor("Felipe","2122121")
biblioteca.usuarios = [profesor] + data_estudiantes
biblioteca.libros = data_libros

print("Bienvenido a Platzi Biblioteca")

for libro in biblioteca.libros_disponibles():
    print(f" {libro.titulo} {libro.veces_prestado}")

cedula = input("Digite el numero de cedula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.cedula, usuario.nombre)
except UsuarioNoEncontradoError:
    print("El usuario no fue encontrado")

try: 
    titulo = input("digita el titulo del libro: ")
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que seleccionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)

resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n{resultado}")

try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e)