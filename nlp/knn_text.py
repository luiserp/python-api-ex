import json
import numpy as np
from nlp.embeddings import get_embeddings

def knn_text(text, database, k=5):
    cursor = database.connection.cursor()
    
    # Ejecutar la consulta SQL con parámetros seguros (%s)
    sql = '''
        SELECT book_id, embeddings FROM book_embeddings
    '''
    cursor.execute(sql)  # Se pasa (1,) como tupla para el parámetro
    
    # Recuperar todas las filas resultantes
    rv = cursor.fetchall()
    
    # Cerrar el cursor
    cursor.close()
    
    # Convertir las filas a un arreglo de numpy
    X = np.array([json.loads(row[1]) for row in rv])       
    Xhat = np.array([get_embeddings(text)["embeddings"]]).reshape(1, -1)
    
    distances, indices = find_nearest_texts(X, Xhat, k)
        
    return get_books_by_id(distances, indices, database)


def euclidean_distance(embedding1, embedding2):
    return np.linalg.norm(embedding1 - embedding2)


def find_nearest_texts(embeddings_array, new_embedding, k=5):
    distances = []

    # Calcular la distancia entre el nuevo embedding y cada embedding en el array
    for idx, embedding in enumerate(embeddings_array):
        distance = euclidean_distance(embedding, new_embedding)
        distances.append((idx, distance))

    # Ordenar los embeddings por distancia y seleccionar los k más cercanos
    # Ordenar por la distancia (el segundo elemento de la tupla)
    distances.sort(key=lambda x: x[1])
    indices = [dist[0] for dist in distances[:k]]
    distances = [dist[1] for dist in distances[:k]]
    
    return distances, indices


def get_books_by_id(distances, indices, database):
        
    cursor = database.connection.cursor()
    
    # Ejecutar la consulta SQL con parámetros seguros (%s)
    sql = '''
        SELECT id, title FROM books WHERE id IN (%s)
    '''
    
    in_p = ', '.join(list(map(lambda x: '%s', indices)))
    sql = sql % in_p
    
    cursor.execute(sql, indices) 
    
    # Recuperar todas las filas resultantes
    rv = cursor.fetchall()
    
    # Cerrar el cursor
    cursor.close()
        
    return [{"id": row[0], "title": row[1], "distance": distances[i]} for i, row in enumerate(rv)]
