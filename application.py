from flask import Flask
app = Flask(__name__)

@app.route("/")  # / represents defalt page
def index():
    return "Hello, world!"
