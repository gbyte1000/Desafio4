# Se modeló una aplicación de música con manejo de canciones, artistas, y usuarios. La
# tarea a realizar consiste en completar los métodos faltantes con la información que 
# tenemos disponible.

# Nota: No olvide eliminar la palabra pass luego de implementar cada método solicitado

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
        self.cancion=cancion
        self.canciones.append(self.cancion)



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

        self.artista=artista
        self.artistas_seguidos.append(artista)


    def agregar_cancion_playlist(self, cancion):
        """
        Agrega una canción a la lista de reproducción del usuario.
        """
        self.cancion=cancion
        self.playlist.append(cancion)


    def eliminar_cancion_playlist(self, cancion):
        """
        Elimina una canción de la lista de reproducción del usuario.
        """
        self.playlist.remove(cancion)


    def reproducir_cancion(self, cancion):
        """
        Simula la reproducción de una canción por parte del usuario.
        Ejemplo: Maxi está reproduciendo Bones de Imagine Dragons.
        """
        self.cancion=cancion
        print(f"{self.nombre} está reproduciendo {cancion.nombre}")

    def escuchar_artista(self, artista):
        """
        Reproduce todas las canciones del artista si el usuario sigue al artista.
        Ejemplo: Maxi está escuchando todas las canciones de Imagine Dragons.
        Se reproduce cada una de las canciones luego de ese mensaje.
        Debe considerar el caso en el que el usuario no siga al artista y
        manejar ese caso individualmente.
        """
        # Completar para escuchar todas las canciones de un artista seguido

        if artista in self.artista_seguidos:
          print(f"{self.nombre} esta reporduciendo todas las canciones de  {artista.nombre}")
          for cancion in artista.canciones:
              print(f"Ahora estas escuchando la {cancion} de {artista.nombre}")
        else:
          print("Usted no sigue individualmente al artista")


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
        self.usuarios.append(usuario)

    def agregar_artista(self, artista):
        """
        Agrega un artista a la lista de artistas de la aplicación.
        """
        # Completar para agregar un artista a la aplicación
        self.artistas.append(artista)

    def agregar_cancion(self, cancion):
        """
        Agrega una canción a la lista de canciones de la aplicación.
        """
        # Completar para agregar una canción a la aplicación
        self.canciones.append(cancion)

    def mostrar_usuarios(self):
        """
        Muestra todos los usuarios de la aplicación.
        """
        # Completar para mostrar todos los usuarios
        for usuario in self.usuarios:
          print(f"Usuario: {usuario.nombre}")

    def mostrar_artistas(self):
        """
        Muestra todos los artistas de la aplicación.
        """
        # Completar para mostrar todos los artistas
        for artista in self.artista:
          print(f"Usuario: {artista.nombre}")

    def mostrar_canciones(self):
        """
        Muestra todas las canciones de la aplicación.
        """
        # Completar para mostrar todas las canciones
        for cancion in self.canciones:
          print(f"Usuario: {cancion.nombre}")

artista1=Artista("Image code")
artista2=Artista("Lucas L.")

cancion1=Cancion("bones",120,artista1)
cancion2=Cancion("huesos",160,artista1)
artista1.lanzar_cancion(cancion1)
artista1.lanzar_cancion(cancion2)


cancion3=Cancion("te amo",120,artista2)
cancion4=Cancion("ya no",150,artista2)

usuario1=Usuario("CARLOS")
usuario2=Usuario("OSCAR")

usuario1.seguir_artista(artista1)
usuario1.agregar_cancion_playlist(cancion1)
cancnion_reproducida=usuario1.reproducir_cancion(cancion1)
print(cancion_reproducida)

usuario1.eliminar_cancion_playlist(cancion1)

usuario1.escuchar_artista(artista1)


"""print("")
print("")
print(usaurio1.playlist[0].nombre)"""

app_musica=AppMusica("Spotify")

app_musica.agregar_usuario(usuario1)
app_musica.agregar_usuario(usuario2)

app_musica.nostrar_usuarios()


app_musica.agregar_artista(artista1)
app_musica.agregar_artista(artista2)


app_musica.mostrar_artista()

app_musica.agregar_cancion(cancion1)
app_musica.agregar_cancion(cancion2)
app_musica.agregar_cancion(cancion3)
app_musica.agregar_cancion(cancion4)



# Tarea 0: Instanciación de las clases. Debe instanciar la aplicación de música, dos artistas, dos usuarios, y al menos dos canciones para cada artista
# Debe escribir el código que trabaja con los objetos luego de cada comentario con cada tarea.

# Tarea 1: Agregar los artistas, usuarios y canciones a la aplicación

# Tarea 2: Hacer que uno de los usuarios siga a un artista

# Tarea 3: Hacer que un usuario agregue una canción a su lista de reproducción

# Tarea 4: Hacer que un usuario reproduzca una canción

# Tarea 5: Hacer que un usuario elimine una canción de su lista de reproducción

# Tarea 6: Hacer que un usuario escuche todas las canciones de un artista que sigue
