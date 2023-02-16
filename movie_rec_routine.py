# Importing necessary packages
import numpy as np
import pandas as pd

import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv('movies.csv')
list_of_all_titles = pd.read_csv('list_of_all_titles.csv')
#similarity = pd.read_csv('similarity.csv')

def movie_rec(movie_name):
    # Getting the movie name from the user
    #movie_name = input(' Enter your favorite movie: ')

    movie_sugestion = movie_name

    # Printing the name of similar movies based on the index
    return movie_sugestion