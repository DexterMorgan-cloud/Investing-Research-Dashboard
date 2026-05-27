import feedparser


def get_stock_news(ticker):

    url = (
        f"https://finance.yahoo.com/rss/headline?s={ticker}"
    )

    feed = feedparser.parse(url)

    news_list = []

    company_words = ticker.lower()

    for entry in feed.entries:

     title = entry.title.lower()

     if company_words in title:

        news = {

            "title": entry.title,

            "link": entry.link

        }

        news_list.append(news)

     if len(news_list) == 5:

        break

        news = {

            "title": entry.title,

            "link": entry.link

        }

        news_list.append(news)

    return news_list