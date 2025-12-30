from flask import Flask, render_template, request
import random

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def home():
    result = ""

    if request.method == "POST":
        length = int(request.form["length"])
        swars = ['s', 'r','g', 'm', 'p', 'dha', 'n', 'saa']
        result = ' '.join(random.sample(swars,length))

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)