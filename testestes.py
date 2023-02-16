
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
#feature_vectors = vectorizer.fit_transform(combined_features)

# Creating a list with all the movies names given in the datasetz
list_of_all_titles = movies_data['title'].tolist()

# Cosine similarity ----------------------------------------------------------------------------------------------------
# Getting the similarity score
#similarity = cosine_similarity(vectorizer.fit_transform(combined_features)).round(1)
#similarity = pd.DataFrame(similarity)
#similarity.to_csv('similarity.csv')


with open(r'movie_titles', 'w', encoding="utf-8") as title:
    title.write("\n".join(list_of_all_titles))

list_of_all_titles = pd.DataFrame(list_of_all_titles)
list_of_all_titles.to_csv('list_of_all_titles.csv')