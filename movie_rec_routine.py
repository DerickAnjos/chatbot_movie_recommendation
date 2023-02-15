# Importing necessary packages
import numpy as np
import pandas as pd

import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading data
movies_data = pd.read_csv('movies.csv')

# Selecting important features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director', 'title', 'release_date', 'index']

# Treating missing values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Joining all the selected features
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + \
                    movies_data['cast'] + ' ' + movies_data['director']

# Transforming the text data into feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Creating a list with all the movies names given in the dataset
list_of_all_titles = movies_data['title'].tolist()

# Cosine similarity ----------------------------------------------------------------------------------------------------
# Getting the similarity score
similarity = cosine_similarity(feature_vectors).round(2)

with open(r'movie_titles', 'w', encoding="utf-8") as title:
    title.write("\n".join(list_of_all_titles))

def movie_rec(movie_name):
    # Getting the movie name from the user
    #movie_name = input(' Enter your favorite movie: ')

    # Finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_close_match[0]

    # Finding the index of the movie with title
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

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