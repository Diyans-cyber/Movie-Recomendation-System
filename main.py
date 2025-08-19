import pandas as pd

# Load files
ratings = pd.read_csv("MovieRecomendations.csv")
movies = pd.read_csv("movielDtitels.csv")

# Keep useful columns
ratings = ratings[['title', 'rating', 'numOfRatings',
                   'FirstMovieRecommendation', 'SecondMovieRecommendation',
                   'ThirdMovieRecommendation', 'FourthMovieRecommendation']]

# Merge with movies list (on title)
dataset = pd.merge(movies, ratings, on="title", how="left")

# Save combined dataset
dataset.to_csv("dataset.csv", index=False)

print("✅ dataset.csv created successfully!")
