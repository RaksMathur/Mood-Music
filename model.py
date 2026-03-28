import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

# Load the dataset
df = pd.read_csv('dataset.csv')

# Drop rows with missing values
df = df.dropna()

# These are the audio features we use to match moods
features = ['valence', 'energy', 'danceability', 'tempo', 'acousticness']

# Keep only the columns we need
df = df[['track_name', 'artists', 'album_name', 'popularity'] + features].dropna()

# Reset index cleanly
df = df.reset_index(drop=True)

# Normalize all features to a scale of 0 to 1
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(df[features])

# Mood profiles
mood_profiles = {
    'happy':     [0.9, 0.8, 0.8, 0.7, 0.2],
    'sad':       [0.1, 0.2, 0.2, 0.3, 0.8],
    'energetic': [0.7, 0.9, 0.9, 0.9, 0.1],
    'calm':      [0.6, 0.2, 0.3, 0.2, 0.9],
    'angry':     [0.2, 0.9, 0.5, 0.8, 0.1],
    'romantic':  [0.7, 0.4, 0.5, 0.3, 0.7],
}

# Train KNN on the scaled numpy array directly (fixes the warning)
knn = NearestNeighbors(n_neighbors=50, metric='euclidean')
knn.fit(scaled_features)

def recommend_songs(mood, min_popularity=0):
    profile = mood_profiles.get(mood.lower())
    if not profile:
        return []

    # Use numpy array to avoid feature name warning
    profile_array = np.array(profile).reshape(1, -1)
    distances, indices = knn.kneighbors(profile_array)

    # Get matched songs
    results = df.iloc[indices[0]].copy()

    # Filter by popularity
    if min_popularity > 0:
        results = results[results['popularity'] >= min_popularity]

    # If filter is too strict and removes all songs, return unfiltered
    if len(results) == 0:
        results = df.iloc[indices[0]].copy()

    # Shuffle for variety
    results = results.sample(frac=1).reset_index(drop=True)

    # Return top 20
    return results.head(20)[['track_name', 'artists', 'album_name', 'popularity']].to_dict('records')