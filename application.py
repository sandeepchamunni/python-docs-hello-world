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
    CredentialName = ""
    UserName = ""
    Password = ""
    doc2 = nlp2(request.form.get('mailbody'))
    response = "{"
    for ent in doc2.ents:
        if ent.label_ == "CREDENTIAL":
            CredentialName = ent.text
        if ent.label_ == "USER":
            UserName = ent.text
        if ent.label_ == "PASSWORD":
            Password = ent.text
        response = r'{"Credential":"' + CredentialName + '","Username":"' + UserName + '","Password":"' + Password + '"}'
    return(response)