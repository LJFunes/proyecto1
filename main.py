# Importaciones
from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


df_developer = pd.read_parquet('datasets/def_developer.parquet')
df_user_data_final = pd.read_parquet('datasets/def_user_data.parquet')
df_user_genre = pd.read_parquet('datasets/def_user_for_genre.parquet')
df_best_developer = pd.read_parquet('datasets/def_best_developer_year.parquet')
df_developer_reviews = pd.read_parquet('datasets/def_developer_reviews_analysis.parquet')
df_modelo_recomendacion = pd.read_parquet('datasets/def_recomendacion_juego.parquet')




def develop(desarrollador):
    developer_filtrado = df_developer[df_developer['developer'] == desarrollador]
    if not developer_filtrado.empty:
        cantidad_anio = developer_filtrado.groupby('release_year')['item_id'].count()
        gratis_anio = (developer_filtrado[developer_filtrado['price'] == 0.0].groupby('release_year')['item_id'].count() / cantidad_anio * 100).fillna(0).astype(int)

        # Convertir los valores de las Series a listas
        cantidad_anio_list = cantidad_anio.tolist()
        gratis_anio_list = gratis_anio.tolist()

        # Convertir los índices a una lista
        anios_list = cantidad_anio.index.tolist()

        # Crear un diccionario con los resultados
        resultados = []
        for i in range(len(anios_list)):
            resultados.append({
                'Año': anios_list[i],
                'Cantidad de juegos': cantidad_anio_list[i],
                '% juegos gratis': gratis_anio_list[i]
            })

        return resultados
    else:
        return {'Error': 'Developer no encontrado... intente con otro developer, por favor'}


def userdata(usuario):
    user_filtrado = df_user_data_final[df_user_data_final['user_id'] == usuario]
    if not user_filtrado.empty:
        # Convertir los valores de NumPy a tipos nativos de Python usando int() y float()
        cantidad_dinero = int(user_filtrado['total_spent'].iloc[0])
        items_totales = int(user_filtrado['items_count'].iloc[0])
        total_recomendaciones = float(user_filtrado['recommend'].iloc[0])

        return {
            'Usuario': usuario, 
            'Cantidad de dinero gastado': cantidad_dinero, 
            'Porcentaje de recomendación': total_recomendaciones, 
            'Items totales en biblioteca': items_totales
        }
    else:
        return {'Error': 'Usuario no encontrado'}




def userforgenre(genero):
    df=pd.DataFrame(df_user_genre)
    
    # Filtrar por género
    df_genero = df[df['genres'] == genero]

    # Usuario con más horas jugadas por género
    usuario_mas_horas = df_genero.groupby('user_id')['playtime_forever'].sum().idxmax()
    usuario_mas_horas_df = df_genero[df_genero['user_id'] == usuario_mas_horas].iloc[0]

    # Filtrar por el usuario con más horas jugadas y calcular las horas jugadas por año de lanzamiento
    df_usuario_mas_horas = df_genero[df_genero['user_id'] == usuario_mas_horas]
    horas_por_anio = df_usuario_mas_horas.groupby('release_year')['playtime_forever'].sum().to_dict()

    return {"Usuario con más horas jugadas por género": usuario_mas_horas_df['user_id'], 
            "Género": usuario_mas_horas_df['genres'], 
            "Horas jugadas por año de lanzamiento" : horas_por_anio}




def bestdeveloperyear(year):
    df = pd.DataFrame(df_best_developer)
    
    # Filtrar por año y recomendaciones True
    df_year = df[(df['release_year'] == year) & (df['recommend'] == True)]
    if not df_year.empty:
        # Calcular la cantidad de recomendaciones por desarrollador
        developer_recommendations = df_year.groupby('developer')['recommend'].count().reset_index()

        # Ordenar en orden descendente y obtener el top 3
        top_developers = developer_recommendations.nlargest(3, 'recommend')

        # Crear la lista de resultados con los puestos y los desarrolladores
        resultado = [
            {"Puesto 1": top_developers.iloc[0]['developer'], "Recomendaciones": int(top_developers.iloc[0]['recommend'])},
            {"Puesto 2": top_developers.iloc[1]['developer'], "Recomendaciones": int(top_developers.iloc[1]['recommend'])},
            {"Puesto 3": top_developers.iloc[2]['developer'], "Recomendaciones": int(top_developers.iloc[2]['recommend'])},
        ]

        return resultado
    else:
        return {'Error': 'año no encontrado o sin datos que mostrar... pruebe con otro año, por favor'}



def developerreviewsanalysis(developer):
    df_filtrado = df_developer_reviews[df_developer_reviews['developer'] == developer]
    
    cantidad_positivos = df_filtrado[df_filtrado['sentiment_analysis'] == 2].shape[0]
    cantidad_negativos = df_filtrado[df_filtrado['sentiment_analysis'] == 0].shape[0]
    
    resultado = {"Desarrolladora": developer,"Análisis de sentimiento": {"Positivos": cantidad_positivos,"Negativos": cantidad_negativos}}
    
    return resultado



def recomendacionjuego(id_producto):

    global df_modelo_recomendacion
    # Agrupar y combinar géneros por item_id
    df_modelo_recomendacion = df_modelo_recomendacion.groupby('item_id').agg({'genres': lambda x: ','.join(set(x)),'app_name': 'first','developer': 'first','recommend_y': 'mean'}).reset_index()
   
    # Filtrar los juegos que coinciden con el item_id dado
    juego_filtrado = df_modelo_recomendacion[df_modelo_recomendacion['item_id'] == id_producto]
    
    if juego_filtrado.empty:
        return {"error": "El juego con el id_producto dado no existe en el DataFrame."}

    # Obtener el nombre del juego filtrado para la salida final
    nombre_juego = juego_filtrado['app_name'].iloc[0]

    # Crear un vectorizador de texto para los géneros
    vectorizer = CountVectorizer(binary=True)
    # vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','), binary=True)
    
    # Vectorizar todos los géneros en el DataFrame
    genre_matrix = vectorizer.fit_transform(df_modelo_recomendacion['genres'])
    
    # Vectorizar los géneros del juego dado
    genre_vector = vectorizer.transform(juego_filtrado['genres'])
    
    # Calcular la similitud del coseno entre el juego dado y todos los demás juegos
    cosine_similarities = cosine_similarity(genre_matrix, genre_vector).flatten()
    
    # Asegurarse de que el DataFrame no está siendo modificado con copia
    df_modelo_recomendacion = df_modelo_recomendacion.copy()

    # Añadir la similitud al DataFrame
    df_modelo_recomendacion['similarity'] = cosine_similarities
    
    # Filtrar juegos con al menos un género en común
    juegos_recomendados = df_modelo_recomendacion[df_modelo_recomendacion['similarity'] > 0]
    
    # Ordenar los juegos por similitud y recomendación en orden descendente
    juegos_recomendados = juegos_recomendados.sort_values(['similarity', 'recommend_y'], ascending=[False, False])
    
    # Seleccionar los 5 juegos con mayor similitud y recomendación
    top_juegos_recomendados = juegos_recomendados.head(5)
    
    # Preparar la salida
    juegos_recomendados_dict = {}
    juegos_recomendados_dict[f'Debido a que te gustó {nombre_juego}, también podría interesarte...'] = top_juegos_recomendados[['app_name', 'developer']].to_dict(orient='records')
    
    return juegos_recomendados_dict



# Se instancia la aplicación
app = FastAPI()


@app.get('/')
def mensaje():
    return "MVP para realizar consultas en la base de datos de STEAM (c)"

@app.get('/developer')
async def developer(desarrollador: str):
    return develop(desarrollador)

@app.get('/user_data')
async def user_data(usuario: str):
    return userdata(usuario)


@app.get('/userforgenre')
def user_for_genre(genero: str):
    return userforgenre(genero)


@app.get('/best_developer_year')
async def best_developer_year(year: int):
    return bestdeveloperyear(year)


@app.get('/developerreviewsanalisis')
def developer_reviews_analysis(developer: str):
    return developerreviewsanalysis(developer)


@app.get('/recomendacion_juego')
async def recomendacion_juego(id_producto: int):
    return recomendacionjuego(id_producto)









