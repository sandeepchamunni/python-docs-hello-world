import spacy
from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/extractcredential", methods=["GET","POST"])
@cross_origin()
def extractcredential():
    nlp2 = spacy.load("custom_ner_model_credential")
    doc2 = nlp2("Please update the username for the credential XD_FAST_056. The new username is XD_USERNAME and the password is XD$qa123")
    response = "{"
    for ent in doc2.ents:
        response = response + " " + ent.label_ + " " + "," + " " + ent.text + " "
    return(response)