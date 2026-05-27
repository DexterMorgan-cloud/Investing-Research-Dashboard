from datetime import datetime

import pytz


def get_market_status():

    eastern = pytz.timezone("US/Eastern")

    current_time = datetime.now(eastern)

    market_open = current_time.replace(
        hour=9,
        minute=30,
        second=0
    )

    market_close = current_time.replace(
        hour=16,
        minute=0,
        second=0
    )

    if (
        current_time.weekday() < 5
        and market_open <= current_time <= market_close
    ):

        return "Open"

    else:

        return "Closed"