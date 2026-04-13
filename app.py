from flask import Flask, render_template, request

app = Flask(__name__)

import random

import random

def love_rate(nama1, nama2):
    random.seed(nama1 + nama2)  # biar hasil tetap sama untuk nama yang sama
    return random.randint(50, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        nama1 = request.form["nama1"]
        nama2 = request.form["nama2"]

        hasil = love_rate(nama1, nama2)

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
