from flask import (
    Flask,render_template,redirect,url_for
)
from userGenerate import userName
import os
import json
import uuid

app = Flask(__name__ , static_url_path = "")
#app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "msayak1269"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/sayak")
# def creatRandomUser():
#     firstName,lastName,userEmail = userName.randomUser()
#     user = {
#         "firstName" : firstName,
#         "lastName" : lastName,
#         "userEmail" : userEmail
#     }

#     return render_template("index.html",user = user)

if __name__ == "__main__":
    app.run(port = 5001 ,debug = True , host = '0.0.0.0')    