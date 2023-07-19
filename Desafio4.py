class Cancion:
    def __init__(self, nombre, duracion, artista):
        """
        Inicializa una nueva canción con un nombre, duración y artista.
        """
        self.nombre = nombre
        self.duracion = duracion
        self.artista = artista

class Artista:
    def __init__(self, nombre):
        """
        Inicializa un nuevo artista con un nombre.
        """
        self.nombre = nombre
        self.canciones = []

    def lanzar_cancion(self, cancion):
        """
        Agrega una canción a la lista de canciones del artista.
        """
        pass


class Usuario:
    def __init__(self, nombre):
        """
        Inicializa un nuevo usuario con un nombre.
        """
        self.nombre = nombre
        self.playlist = []
        self.artistas_seguidos = []

    def seguir_artista(self, artista):
        """
        Agrega un artista a la lista de artistas seguidos por el usuario.
        """
        pass


    def agregar_cancion_playlist(self, cancion):
        """
        Agrega una canción a la lista de reproducción del usuario.
        """
        pass


    def eliminar_cancion_playlist(self, cancion):
        """
        Elimina una canción de la lista de reproducción del usuario.
        """
        pass


    def reproducir_cancion(self, cancion):
        """
        Simula la reproducción de una canción por parte del usuario.
        Ejemplo: Maxi está reproduciendo Bones de Imagine Dragons.
        """
        pass

    def escuchar_artista(self, artista):
        """
        Reproduce todas las canciones del artista si el usuario sigue al artista.
        Ejemplo: Maxi está escuchando todas las canciones de Imagine Dragons.
        Se reproduce cada una de las canciones luego de ese mensaje.
        Debe considerar el caso en el que el usuario no siga al artista y
        manejar ese caso individualmente.
        """
        # Completar para escuchar todas las canciones de un artista seguido

    pass


class AppMusica:
    def __init__(self, nombre):
        """
        Inicializa una nueva aplicación de música con un nombre.
        """
        self.nombre = nombre
        self.usuarios = []
        self.artistas = []
        self.canciones = []

    def agregar_usuario(self, usuario):
        """
        Agrega un usuario a la lista de usuarios de la aplicación.
        """
        # Completar para agregar un usuario a la aplicación
        pass

    def agregar_artista(self, artista):
        """
        Agrega un artista a la lista de artistas de la aplicación.
        """
        # Completar para agregar un artista a la aplicación
        pass

    def agregar_cancion(self, cancion):
        """
        Agrega una canción a la lista de canciones de la aplicación.
        """
        # Completar para agregar una canción a la aplicación
        pass

    def mostrar_usuarios(self):
        """
        Muestra todos los usuarios de la aplicación.
        """
        # Completar para mostrar todos los usuarios
        pass

    def mostrar_artistas(self):
        """
        Muestra todos los artistas de la aplicación.
        """
        # Completar para mostrar todos los artistas
        pass

    def mostrar_canciones(self):
        """
        Muestra todas las canciones de la aplicación.
        """
        # Completar para mostrar todas las canciones
        pass
        

# Tarea 0: Instanciación de las clases. Debe instanciar la aplicación de música, dos artistas, dos usuarios, y al menos dos canciones para cada artista
# Debe escribir el código que trabaja con los objetos luego de cada comentario con cada tarea.

# Tarea 1: Agregar los artistas, usuarios y canciones a la aplicación

# Tarea 2: Hacer que uno de los usuarios siga a un artista

# Tarea 3: Hacer que un usuario agregue una canción a su lista de reproducción

# Tarea 4: Hacer que un usuario reproduzca una canción

# Tarea 5: Hacer que un usuario elimine una canción de su lista de reproducción

# Tarea 6: Hacer que un usuario escuche todas las canciones de un artista que sigue
