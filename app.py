from flask import Flask
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, World! This is my basic Flask app."

@app.route('/about')
def about():
    print("This is print statement by saipavan")
    return "This is the about page."

@app.route("/newendpoint")  
def newendpoint():
    return "success"

if __name__ == '__main__':
    app.run(debug=True)