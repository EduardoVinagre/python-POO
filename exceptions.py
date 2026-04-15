class BibliotecaError(Exception):
    pass


class LibroNotFoundError(BibliotecaError):
    pass

class LibroNoDisponibleError(Exception):
    pass

class UsuarioNoEncontradoError(Exception):
    pass