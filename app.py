from flask import Flask

app = Flask(__name__)   # add Flask instance

@app.route('/')     # define the starting point, or root.
def hello_world():
    return 'Hello world'

