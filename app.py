from flask import Flask, render_template, request

from stock_data import get_stock_data

from market_status import get_market_status

from news import get_stock_news


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def home():

    stock = None

    news = []

    market_status = None

    if request.method == "POST":

        ticker = request.form["ticker"].upper()

        stock = get_stock_data(ticker)

        market_status = get_market_status()

        news = get_stock_news(ticker)

    return render_template(

        "dashboard.html",

        stock=stock,

        news=news,

        market_status=market_status

    )


if __name__ == "__main__":

    app.run(debug=True)