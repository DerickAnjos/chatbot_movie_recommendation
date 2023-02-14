from flask import Flask, render_template, request, jsonify
from chatbot import get_response
#from movie_rec_routine import movie_rec
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/')
def index_get():
    return render_template('base.html')

@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    # CHECK IF TEXT IS VALID

    if text[0:6].lower() == 'movie:':
        #message = {'answer': movie_rec(text[6:])}
        message = {'answer': 'movie_rec(text[6:])'}
        return jsonify(message)

    else:
        response = get_response(text)
        message = {'answer': response}
        return jsonify(message)

if __name__ == "__main__":
    app.run()

