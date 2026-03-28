# 🎵 Mood Music

A machine learning web app that recommends songs based on your mood.
Built with Flask, scikit-learn, pandas and a Spotify tracks dataset.

## Moods supported
😊 Happy | 😢 Sad | ⚡ Energetic | 😌 Calm | 😠 Angry | ❤️ Romantic

## How it works
Uses KNN algorithm to match mood profiles to audio features
like valence, energy, danceability, tempo and acousticness.

## How to run
1. Install requirements: pip install flask scikit-learn pandas numpy
2. Add dataset.csv from Kaggle (Spotify Tracks Dataset)
3. Run: python app.py
4. Open: http://127.0.0.1:5000
