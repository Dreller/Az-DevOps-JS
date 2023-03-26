from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="ADO JS Interaction", org="dreller08xp1", pat="rkriqbbxnebqzrdhmydcn762ueue6qdlvht7qixxvn4gbrdqwhsq")
