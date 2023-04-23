from datetime import datetime
import datetime as dt

# mock database 
db = {
    "client1": {
        "trades": {
            "1": {
                "asset_class": "Equity",
                "counterparty": "goldman",
                "instrument_id": "AAPL",
                "instrument_name": "Apple Inc",
                "trade_date_time": dt.datetime.now(),
                "trade_details": {
                    "buy_sell_indicator": "BUY",
                    "price": 150.0,
                    "quantity": 100
                },
                "trade_id": "1",
                "trader": "John Doe"
            }
        }
    },
        "client2": {
        "trades": {
            "2": {
                "asset_class": "Bond",
                "counterparty": "Deutsche bank",
                "instrument_id": "AAPL",
                "instrument_name": "Microsoft inc",
                "trade_date_time": dt.datetime.now(),
                "trade_details": {
                    "buy_sell_indicator": "SELL",
                    "price": 1500.0,
                    "quantity": 1000
                },
                "trade_id": "2",
                "trader": "Mark Henry"
            }
        }
    },
     "client3": {
        "trades": {
            "3": {
                "asset_class": "CDS",
                "counterparty": "Morgan Stanley",
                "instrument_id": "IKEA-Tab",
                "instrument_name": "Ikea furniture",
                "trade_date_time": dt.datetime.now(),
                "trade_details": {
                    "buy_sell_indicator": "BUY",
                    "price": 15099.0,
                    "quantity": 300
                },
                "trade_id": "3",
                "trader": "Ray Dalio"
            }
        }
    },
     "client4": {
        "trades": {
            "4": {
                "asset_class": "Debenture",
                "counterparty": "Credit suisse",
                "instrument_id": "Sensors",
                "instrument_name": "Apple Inc",
                "trade_date_time": dt.datetime.now(),
                "trade_details": {
                    "buy_sell_indicator": "SELL",
                    "price": 1509.0,
                    "quantity": 1090
                },
                "trade_id": "4",
                "trader": "John Cena"
            }
        }
    },
     "client5": {
        "trades": {
            "5": {
                "asset_class": "Gold",
                "counterparty": "Lehmann brothers",
                "instrument_id": "Au",
                "instrument_name": "Digital gold",
                "trade_date_time": dt.datetime.now(),
                "trade_details": {
                    "buy_sell_indicator": "BUY",
                    "price": 150000.0,
                    "quantity": 100000
                },
                "trade_id": "5",
                "trader": "George Soros"
            }
        }
    },
     "client6": {
        "trades": {
            "6": {
                "asset_class": "Currency",
                "counterparty": "Jane street",
                "instrument_id": "INR",
                "instrument_name": "Indian rupee",
                "trade_date_time": dt.datetime.now(),
                "trade_details": {
                    "buy_sell_indicator": "BUY",
                    "price": 80.0,
                    "quantity": 100000000
                },
                "trade_id": "6",
                "trader": "Michael Burry"
            }
        }
    }
}
