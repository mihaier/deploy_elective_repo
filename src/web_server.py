from flask import Flask
from flask import request
import json


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hellow_world():
    return "<p>Привет участникам электива<p>"

@app.route("/parse/<job>")
def parse_param(job):
    return "Вы обратились на {}".format(job)

@app.route("/sample_post", methods=["POST"])
def parse_param_post():
    d = json.loads(request.data)
    return "Вы обратились по посту на {}".format(d.['body'])

#app.run()
