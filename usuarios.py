class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"La solicitud de libro '{titulo}' realizada"


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return super().solicitar_libro(titulo)
        else:
            return "No puedes prestar más libros, limite alcanzado"
        


class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return super().solicitar_libro(titulo)
    

estudiante =Estudiante("Luis","1212121","Sistemas")
profesor = Profesor("Felipe","2122121")

print(profesor.solicitar_libro("Python básico"))
print(profesor.solicitar_libro("Python Intermedio"))
print(profesor.solicitar_libro("Python Avanzado"))
print(profesor.solicitar_libro("Python / django"))