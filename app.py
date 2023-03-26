from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="JS AzDO", org=os.environ.get("ADO_ORG"), pat=os.environ.get("ADO_PAT"))
