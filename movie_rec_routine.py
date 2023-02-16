# Importing necessary packages
import numpy as np
import pandas as pd
import pyarrow
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv('movies.csv')
list_of_all_titles = pd.read_csv('list_of_all_titles.csv')
#similarity = pd.read_csv('similarity.csv')
# Lendo um arquivo parquet
a = pd.read_parquet('similarity', engine='pyarrow')
#a.info()
#a.memory_usage()






#similarity_old = pd.read_parquet('similarity', engine='pyarrow', chunked  = 1000)
# Verificando os shapes de um dataframe de 30 mil linhas e 10 cols
#for chunk in similarity_old:
#    print(chunk.shape)

# Juntando os chunks em um novo dataframe
#similarity = pd.DataFrame()
#for chunk in pd.read_csv(path, chunksize=10000):
#    new_df = new_df.append(chunk)







def movie_rec(movie_name):
    # Getting the movie name from the user
    #movie_name = input(' Enter your favorite movie: ')

    movie_sugestion = movie_name

    # Printing the name of similar movies based on the index
    return movie_sugestion