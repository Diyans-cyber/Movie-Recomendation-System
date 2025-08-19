import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# ----------------------------
# Helper functions
# ----------------------------
def top_movies(n=10, min_ratings=50):
    """Return top N movies sorted by rating & numOfRatings"""
    popular = df[df["numOfRatings"] >= min_ratings]
    popular = popular.sort_values(["rating", "numOfRatings"], ascending=False)
    return popular[["title", "rating", "numOfRatings"]].head(n)

def recommend_movie(movie_name):
    """Return recommendations for a given movie"""
    row = df[df["title"].str.lower() == movie_name.lower()]
    if row.empty:
        return []
    
    recs = []
    for col in ["FirstMovieRecommendation", "SecondMovieRecommendation", 
                "ThirdMovieRecommendation", "FourthMovieRecommendation"]:
        if col in row.columns:
            recs.append(row.iloc[0][col])
    return recs

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="🎬 Movie Recommendation System", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Pick a movie to get recommendations, or explore the most popular ones!")

# Dropdown for movie selection
movie_list = df["title"].dropna().unique().tolist()
selected_movie = st.selectbox("Choose a movie:", sorted(movie_list))

if st.button("Get Recommendations"):
    recs = recommend_movie(selected_movie)
    if recs:
        st.subheader(f"✨ Because you liked **{selected_movie}**, you may also enjoy:")
        for i, r in enumerate(recs, 1):
            st.write(f"{i}. {r}")
    else:
        st.warning("No recommendations found for this movie.")

# Show Top 10 Movies
st.subheader("🔥 Top 10 Popular Movies")
st.dataframe(top_movies(10))
