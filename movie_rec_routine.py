# Importing necessary packages
import pandas as pd
import difflib

movies_data = pd.read_csv('movies.csv')
list_of_all_titles = movies_data['title'].tolist()

def movie_rec(movie_name, similarity):
    # Getting the movie name from the user
    print('inicio_funcao')
    # Finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_close_match[0]
    print('2_funcao')
    # Finding the index of the movie with title
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    print('3_funcao')
    # Getting a list of similar movie
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    print('4_funcao')
    # Sorting the movies based on their similarity score
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
    print('5_funcao')
    i = 1
    movie_sugestion = 'Based on the movie "'
    for movie in sorted_similar_movies:

        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        release_from_index = movies_data[movies_data.index == index]['release_date'].values[0]
        print('6_funcao')
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