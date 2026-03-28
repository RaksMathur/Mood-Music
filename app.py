from flask import Flask, render_template, request
from model import recommend_songs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form.get('mood')
    popularity = int(request.form.get('popularity', 0))
    songs = recommend_songs(mood, min_popularity=popularity)
    return render_template('results.html', mood=mood, songs=songs)

if __name__ == '__main__':
    app.run(debug=True)