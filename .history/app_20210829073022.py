from flask import Flask 

app = Flask(__name__)

@app.ro
def index():
    return 'Hello World'