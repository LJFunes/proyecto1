

# <h1 align=center> **Proyecto Final individual #1** </h1>

# <h1 align=center> **Machine Learning Operations (MLOps)** </h1>
<p align=center><img src=imagenes/steamDB.png><P>

<br>

## INTRODUCCION

En este proyecto se emula el trabajo de un Data Scientist, asumiendo tareas propias de MLOps Engineer. En este escenario, el MLOps Engineer trabaja para Steam&reg;, una de las plataformas de distribución digital de videojuegos más grandes del mundo, con más de 100 millones de usuarios. El enfoque del proyecto es resolver un problema comercial importante: desarrollar un Producto Mínimo Viable (MVP) que incluya una API para su implementación, y el empleo de un modelo de Machine Learning para desarrollar un sistema de recomendación.

<br>

## DESCRIPCION DEL PROYECTO

El proyecto tiene como principales objetivos:

* Examinar y categorizar las opiniones de los usuarios: para lo cual se utiliza una biblioteca de Procesamiento del Lenguaje Natural (NLP), y así evaluar la polaridad de los sentimientos expresados en cada comentario, clasificándolos como negativos, neutrales o positivos.

* Desarrollar un sistema de recomendación de videojuegos. Este sistema sugiere juegos en base a la similitud que existe entre los mismos.

* Desarrollar una API y desplegarla en un cloud service como Render.

<br>

## DATASETS

Para desarrollar el proyecto se utilizaron tres archivos en formato JSON (en el [DICCIONARIO](diccionario.md) se encuentra información más detallada sobre los mismos):

* `output_steam_games.json`: Contiene información sobre los juegos de la plataforma, como el nombre del juego, desarrollador, precio, géneros, fecha de lanzamiento, etc.

* `australian_users_items.json`: Contiene información sobre los juegos descargados por los usuarios y las horas que el usuario acumula en cada uno de sus juegos, entre otros.

* `australian_users_reviews.json`: Contiene las reseñas que los usuarios realizaron sobre los juegos que usan y la fecha en que se publicó, si lo recomiendan o no, etc.

<br>

## TECNOLOGIAS EMPLEADAS EN EL PROYECTO

Se utilizó el editor de código **Visual Studio Code**, de Microsoft&reg;, y el lenguaje de programación **Python** (aprovechando la extensión de **Jupyter Notebook** en VSCode) para realizar todas las tareas (y se trabajó con archivos en formato json y parquet).

Se emplearon varias bibliotecas de Python, entre ellas la principales **Pandas** y **Numpy** para trabajar con los dataframes, **Scikit-Learn** para el modelo de recomendación, **Matplotlib** y **Seaborn** para el EDA (Exploratory Data Analysis), y la biblioteca **NLTK** (Natural Language Toolkit) para el análisis de sentimiento.

Para desarrollar la API se utilizó el framework **"FastAPI"**, y para el despliegue y alojamiento web se utilizó el service cloud [**Render**](https://render.com/).





<br>

## DESCRIPCION DE LAS TAREAS

<br>

### 1) ETL (Extraction, Transform, Load):

En esta etapa, se realizó la limpieza de datos. Los datasets se transformaron en DataFrames para facilitar su manejo. También se llevaron a cabo procesos como desanidar columnas, transformar y limpiar datos. Específicamente, se analizaron y limpiaron valores nulos y duplicados, se completaron datos que faltaban, se eliminaron algunas columnas innecesarias y se renombraron otras, además de cambiar los tipos de datos de ciertos campos, entre otras tareas.

![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)

> Para ver en detalle las tareas realizadas en esta etapa, ingrese al siguiente link: [ETL](ETL.ipynb)

<br>

### 2) Feature Engineering

En esta fase, se concentró en analizar los sentimientos expresados en los comentarios (reviews) de los usuarios utilizando la biblioteca **NLTK** (Natural Language Toolkit). Se añadió una nueva columna llamada 'sentiment_analysis' al conjunto de datos 'user_reviews', donde las reseñas de los usuarios se clasifican como positiva, neutral o negativa, utilizando los valores 0 para negativa, 1 para neutra y 2 para positiva.

![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)

> Para ver en detalle las tareas realizadas en esta etapa, ingrese al siguiente link: [ETL](ETL.ipynb) en la PARTE 2 - DATASET USER REVIEWS 

<br>

### 3) EDA (Exploratory Data Analysis):

Se realizó un análisis rápido de distintos aspectos de los datos, como la distribución, media y outliers de precios, correlaciones entre generos y cantidad de generos por juego, cantidad de juegos por año de lanzamiento, etc.

![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat&logo=WordCloud)
![Seaborn](https://img.shields.io/badge/Seaborn-333333?style=flat&logo=Seaborn)

> Para ver en detalle las tareas realizadas en esta etapa, ingrese al siguiente link: [EDA](EDA.ipynb)

<br>

### 4) Modelamiento (Desarrollo de modelos de aprendizaje automático)

En esta fase, desarrollamos nuestro sistema de recomendación basado en la relación entre ítems. Esto significa que seleccionamos un ítem y, comparándolo con otros en función de su similitud, recomendamos aquellos que son más parecidos utilizando la técnica de similitud de coseno.
Relación Item-Item: Se elige un ítem y, a través de los generos que poseemos como información, identificamos y recomendamos cinco ítems similares.
Para construir este sistema de recomendación, utilizamos el conjunto de datos que obtuvimos de las etapas previas y creamos un nuevo dataset específicamente diseñado para apoyar este proceso.

![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)

<br>

### 5) Desarrollo de la API y despliegue

Se construyó una API mediante el uso del framework FastAPI. Esta API ofrece varias funciones, estas son: 

- **Developer:** Función que recibe como parametro el nombre de una empresa desarrolladora y retorna la cantidad de items y porcentaje de contenido gratuito por año según la empresa dada. 

- **User_Data:** Función que recibe como parametro un identificador de usuario y retorna la cantidad de dinero gastado por el mismo, el porcentaje de recomendación y cantidad de items. 

- **User_For_Genre:** Función que recibe como parametro un genero de juego y retorna el usuario con más horas jugadas para dicho genero y una acumulación de horas jugadas por año de lanzamiento.

- **Best_Developer_Year:** Función que recibe como parametro un año y retorna el TOP 3 de desarrolladores con más recomendaciones para el año dado.

- **Developer_Reviews_Analysis:** Función que recibe como parametro el nombre de una empresa desarrolladora y retorna la cantidad de reseñas positivas y negativas, descartando las neutras.

- **Recomendacion_Juego:** Esta función recibe como parametro el id de un juego y retorna una lista de los 5 juegos recomendados similares al ingreso.

Para desplegar la API, se utilizó el web service de **Render**, el cual se vinculó a otro repositorio de GitHub que contiene lo mínimo necesario para que funcione la API, el cual puede ver en el siguiente link: [Repositorio para deployar en Render](https://github.com/LJFunes/P1_render)

![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)


> Para poder interactuar con las funciones, ingrese al siguiente link: [Deploy en Render](https://p1-render.onrender.com/)

<br>

### 6) Presentación de resultados del MVP

Se graba un video para mostrar que las herramientas funcionan, explicando el resultado de las consultas propuestas y del modelo de ML entrenado para el sistema de recomendación.

> Para ver el video, ingrese al siguiente link: [video explicativo](https://youtu.be/0bAxUdJmAcE)

<br><br><br>

## Autor
Leandro Funes


