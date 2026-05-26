import yfinance as yf

from datetime import datetime


def get_stock_data(ticker):

    try:

        stock = yf.Ticker(ticker)

        info = stock.info

        if not info or "symbol" not in info:

            return {"error": "Invalid ticker symbol"}

        earnings_date = "Not Available"

        try:

            calendar = stock.calendar

            if calendar:

                earnings_value = calendar.get(
                    "Earnings Date"
                )

                if earnings_value:

                    earnings_date = earnings_value[0].strftime(
                        "%d-%m-%Y"
                    )

        except Exception:

            pass

        data = {

            "company_name":
                info.get("longName")
                or info.get("shortName")
                or "Unknown Company",

            "symbol": info.get("symbol"),

            "current_price": info.get("currentPrice"),

            "market_cap": info.get("marketCap"),

            "pe_ratio": info.get("trailingPE"),

            "fifty_two_week_high":
                info.get("fiftyTwoWeekHigh"),

            "fifty_two_week_low":
                info.get("fiftyTwoWeekLow"),

            "volume": info.get("volume"),

            "average_volume":
                info.get("averageVolume"),

            "sector": info.get("sector"),

            "industry": info.get("industry"),

            "country": info.get("country"),

            "website": info.get("website"),

            "employees":
                info.get("fullTimeEmployees"),

            "analyst_target":
                info.get("targetMeanPrice"),

            "recommendation":
                info.get("recommendationKey"),

            "summary":
                info.get("longBusinessSummary"),

            "next_earnings_date":
                earnings_date

        }

        return data

    except Exception as e:

        return {"error": str(e)}