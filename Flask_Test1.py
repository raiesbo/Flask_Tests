from flask import Flask, template_rendered

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'