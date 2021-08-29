from flask import Flask 

app = Flask(__name__)

@app.r
def index():
    return 'Hello World'