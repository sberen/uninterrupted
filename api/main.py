from flask import Flask, jsonify

app = Flask(__name__)

songs = [
    {
        "title": "Rockstar",
        "artist": "Dababy",
        "genre": "rap",
    },
    {
        "title": "Say So",
        "artist": "Doja Cat",
        "genre": "Hiphop",
    },
    {
        "title": "Panini",
        "artist": "Lil Nas X",
        "genre": "Hiphop"
    }
]

@app.route('/')
def home():
  return jsonify(songs)

if __name__ == '__main__':
  app.run()