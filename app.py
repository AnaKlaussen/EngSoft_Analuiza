from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mackenzie, nosso nome é Ana Luíza e Sophia sz"
