from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hellow_world():
    return "<p>Привет участникам электива<p>"

app.run()
