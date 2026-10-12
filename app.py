import streamlit as st
import pickle

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:11]

    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

# Streamlit interface
st.title("Movie Recommendation System")
st.write("Select a movie and get 10 similar movies.")
movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(movie_name)
    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recommendations,start=1):
        st.write(i, movie)