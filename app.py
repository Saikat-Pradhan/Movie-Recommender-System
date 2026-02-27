import streamlit as st
import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity

# Load Data
movies_df = pickle.load(open('movies.pkl', 'rb'))
cv = pickle.load(open('CountVectorizer.pkl', 'rb'))

# Vector Creation
vectors = cv.fit_transform(movies_df['tags']).toarray()
similarity = cosine_similarity(vectors)

# Fetch Poster Path from TMDB API
def fetch_poster(movie_id):
    response = requests.get(
        f'http://api.themoviedb.org/3/movie/{movie_id}?api_key=71b0417dd8849851130c19750b9b550a&language=en-US'
    )
    data = response.json()

    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

# Recommendation function
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommend_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movies_posters

# Frontend
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select a Movie',
    options=movies_df['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx])
            st.text(names[idx])