## STEAM_GAMES (output_steam_games.json)
Contiene información sobre varios juegos de Steam. A continuación, se describen los campos:
1)	id (string): Identificador único del juego en Steam.
2)	app_name (string): Nombre de la aplicación tal como aparece en la tienda de Steam.
3)	title (string): Título principal del juego, usualmente igual al nombre de la aplicación.
4)	publisher (string): Nombre del editor del juego.
5)	developer (string): Nombre del desarrollador del juego.
6)	genres (list of strings): Lista de géneros a los que pertenece el juego
7)	tags (list of strings): Lista de etiquetas asignadas al juego por los usuarios de Steam (puede incluir géneros y otras caracteristicas).
8)	url (string): URL de la página del juego en la tienda de Steam.
9)	reviews_url (string): URL de la página de reseñas del juego en Steam Community.
10)	release_date (string): Fecha de lanzamiento del juego en formato YYYY-MM-DD.
11)	price (string o float): Precio del juego. Puede ser un valor numérico (ej.: 4.99) o "Free To Play" si es gratuito.
12)	early_access (boolean): Indica si el juego se encuentra en acceso anticipado (True) o no (False).
13)	specs (list of strings): Lista de características técnicas del juego, como modo de juego (un jugador, multijugador, etc.)

## USER_REVIEWS (australian_user_reviews.json)
Contiene información sobre reseñas de videojuegos, además de datos adicionales como si recomiendan o no ese juego entre otros. A continuación, se describen los campos:
1)	user_id (str): Identificador único del usuario que escribió la reseña.
2)	user_url (str): URL del perfil del usuario en Steam Community.
3)	reviews (lista de objetos): Es una lista que contiene objetos, cada objeto representa una reseña individual.
Campos anidados dentro del objeto "reviews":
> 1.	funny (str): Almacena la cantidad de votos que la reseña recibió como "divertida".
> 2.	posted (str): Fecha en la que se publicó la reseña.
> 3.	last_edited (str): Fecha de la última edición de la reseña.
> 4.	item_id (str): Identificador único del videojuego reseñado.
> 5.	helpful (str): Indica cuántas personas consideraron la reseña útil.
> 6.	recommend (booleano): Indica si el usuario recomienda el videojuego (True - lo recomienda, False - no lo recomienda).
> 7.	review (str): El texto de la reseña escrita por el usuario.


## USERS_ITEMS (australian_users_items.json)
Contiene información sobre los juegos de los usuarios de Steam como la cantidad de horas acumuladas jugadas. Los campos son:
1)	user_id (str): Identificador único del usuario de la cuenta de Steam.
2)	items_count (int): Cantidad total de juegos en la biblioteca del usuario.
3)	steam_id (str): ID de la cuenta de Steam del usuario (puede ser el mismo que user_id).
4)	user_url (str): URL del perfil del usuario en Steam Community.
5)	items (lista de objetos): Es una lista que contiene objetos, cada objeto representa un juego de la biblioteca del usuario.
Campos anidados dentro del objeto "items":
> 1.	item_id (str): Identificador único del juego en Steam.
> 2.	item_name (str): Nombre del juego.
> 3.	playtime_forever (int): Tiempo total de juego registrado en horas (desde que el usuario tiene el juego).
> 4.	playtime_2weeks (int): Tiempo de juego en las últimas dos semanas registrado en horas.



# Lista de "géneros" utilizado en el dataset de steam_games.parquet
Se obtienen 22 tipos de géneros clasificados en total del dataset en steam_games, los cuales se intenta dar una breve descripción (probablemente algunas contengan errores).

### Géneros principales de videojuegos:
* Action (Acción): Juegos que se centran en los desafíos físicos, los reflejos y la superación de obstáculos, a menudo relacionados con el combate (por ejemplo, juegos de disparos, juegos de lucha, plataformas).
* Adventure (Aventura): Juegos que enfatizan la exploración, la resolución de rompecabezas y el progreso de la historia (por ejemplo, aventuras point-and-click, juegos de exploración de mundo abierto).
* Racing (Carreras): Juegos donde los jugadores compiten en carreras con vehículos o personajes (por ejemplo, juegos de carreras de autos, juegos de carreras de motocicletas).
* Strategy (Estrategia): Juegos que requieren que los jugadores piensen con anticipación, planifiquen sus acciones y administren recursos para superar a sus oponentes (por ejemplo, juegos de estrategia en tiempo real, juegos de estrategia por turnos).
* RPG (Juego de rol): Juegos donde los jugadores toman el papel de un personaje y desarrollan sus habilidades y destrezas dentro de un mundo ficticio (por ejemplo, juegos de rol por turnos, juegos de rol de acción).
* Simulation (Simulación): Juegos que intentan replicar experiencias o sistemas del mundo real, a menudo con un enfoque en la estrategia o la gestión de recursos (por ejemplo, simuladores de construcción de ciudades, simuladores de vuelo, simuladores de granjas).
* Sports (Deportes)

### Otras categorías:
* Indie (Indie): Juegos desarrollados por estudios independientes en lugar de grandes editoriales.
* Free to Play - Gratuito para jugar (F2P):  Un modelo de negocio donde el juego base es gratuito, pero los jugadores pueden comprar contenido o funciones adicionales.
* Casual (Casual): Juegos diseñados para ser fáciles de aprender y jugar, a menudo con sesiones de juego más cortas.
* Massively Multiplayer (Multijugador masivo - MMO): Juegos en línea donde una gran cantidad de jugadores pueden interactuar y participar en un mundo persistente.

### Categorías de software:
* Animation & Modeling (Animación y modelado): Software utilizado para crear animaciones y modelos 3D.
* Utilities (Utilidades): Herramientas de software de uso general para tareas como la administración de archivos, la optimización del sistema o la productividad.
* Education (Educación): Software diseñado con fines educativos, como aprender idiomas, ciencias o historia.
* Design & Illustration (Diseño e ilustración): Software utilizado para diseño gráfico, ilustración y creación de arte digital.
* Audio Production (Producción de audio): Software para grabar, editar y mezclar audio.
* Video Production (Producción de video): Software para editar y crear contenido de video.
* Software Training (Capacitación en software): Software o recursos utilizados para enseñar a los usuarios cómo utilizar otros programas de software.
* Accounting (Contabilidad): Software para administrar registros financieros y transacciones.
* Web Publishing (Publicación web): Software para crear y administrar sitios web.
* Photo Editing (Edición de fotos): Software para editar y manipular fotografías digitales.
* Early Access (Acceso anticipado): Juegos que aún están en desarrollo, pero están disponibles para su compra y juego por parte del público.