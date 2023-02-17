# Importing necessary packages
import numpy as np
import pandas as pd
import pyarrow
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv('movies.csv')
#movies_data.info()
#movies_data.columns = movies_data.columns.astype()
#movies_data.info()
list_of_all_titles = movies_data['title'].tolist()

#list_of_all_titles = pd.read_csv('list_of_all_titles.csv')
#similarity = pd.read_csv('similarity.csv')
# Lendo um arquivo parquet
#similarity = pd.read_parquet('similarity', engine='pyarrow')
#a.info()
#a.memory_usage()



#similarity = np.array(similarity)
#print(type(similarity))



#print(similarity[68])





#similarity_old = pd.read_parquet('similarity', engine='pyarrow', chunked  = 1000)
# Verificando os shapes de um dataframe de 30 mil linhas e 10 cols
#for chunk in similarity_old:
#    print(chunk.shape)

# Juntando os chunks em um novo dataframe
#similarity = pd.DataFrame()
#for chunk in pd.read_csv(path, chunksize=10000):
#    new_df = new_df.append(chunk)







def movie_rec(movie_name, similarity):
    # Getting the movie name from the user
    #movie_name = input(' Enter your favorite movie: ')
    print(movie_name)
    # Finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_close_match[0]

    # Finding the index of the movie with title
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    print(type(index_of_the_movie))
    # Getting a list of similar movie
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    # Sorting the movies based on their similarity score
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

    i = 1
    movie_sugestion = 'Based on the movie "'
    for movie in sorted_similar_movies:

        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        release_from_index = movies_data[movies_data.index == index]['release_date'].values[0]

        if (i==1):
            movie_sugestion = movie_sugestion + (title_from_index + '" (' +
                                                 release_from_index[0:4] + '), directed by ' +
                                                 movies_data[movies_data.index == index]['director'].values[0] +
                                                 ", I recommend you see: <br>")
            i+=1
            continue

        if (i<7):
            movie_sugestion = movie_sugestion + ("<br>" + str(i-1) + '. ' + title_from_index + " (" +
                                                 release_from_index[0:4] + ")")
            i+=1

    # Printing the name of similar movies based on the index
    return movie_sugestion