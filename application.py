import spacy
from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/extractcredential", methods=["GET","POST"])
@cross_origin()
def extractcredential():
    return("Hello world")