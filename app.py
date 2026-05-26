from flask import Flask, render_template, request

from stock_data import get_stock_data


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def home():

    stock = None

    if request.method == "POST":

        ticker = request.form["ticker"].upper()

        stock = get_stock_data(ticker)

    return render_template("dashboard.html", stock=stock)


if __name__ == "__main__":

    app.run(debug=True)