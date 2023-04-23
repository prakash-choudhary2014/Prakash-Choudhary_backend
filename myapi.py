


from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime as dt
import uvicorn
from mockdata import db

app = FastAPI()

# define the Trade model
class TradeDetails(BaseModel):
    buy_sell_indicator: str = Field(description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")

class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")
    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")
    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")
    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")
    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")
    trader: str = Field(description="The name of the Trader")


# retrieve a single trade by ID
@app.get("/trades/{client}/{trade_id}")
async def retrieve_single_trade(client: str, trade_id: str):
    try:
        trade = db[client]["trades"][trade_id]
        return {"client": client, "trade": trade}
    except KeyError:
        raise HTTPException(status_code=404, detail="Trade not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



#  Fetching all trades without pagination   
@app.get("/trades")
async def get_trades():
    return db    



# fetching all trades with pagination
# url example http://localhost:8000/trades?page_size=2&page_num=2
@app.get("/trades")
async def get_trades(page_size: int = 2, page_num: int = 1):
    trades = list(db.values())
    total_trades = len(trades)
    start_index = (page_num - 1) * page_size
    end_index = start_index + page_size

    trades_slice = trades[start_index:end_index]
    num_results = len(trades_slice)
    has_more = end_index < total_trades

    return {
        "results": trades_slice,
        "metadata": {
            "page_size": page_size,
            "page_number": page_num,
            "total_results": total_trades,
            "num_results": num_results,
            "has_more": has_more,
        }
    }





# endpoint for searching trade with search query
@app.get("/trades/search")
async def search_trades(q: str):
    matched_trades = []
    for client in db.values():
        for trade in client["trades"].values():
            if (q.lower() in trade["instrument_id"].lower() or
                q.lower() in trade["instrument_name"].lower() or
                q.lower() in trade["counterparty"].lower() or
                q.lower() in trade["trader"].lower()):
                matched_trades.append(trade)
    return matched_trades






# endpoint for advanced filtering
@app.get("/search_trades_advanced")
async def search_trades_advanced(assetClass: Optional[str] = Query(None, description="Asset class of the trade."),
                                end: Optional[dt.datetime] = Query(None, description="The maximum date for the tradeDateTime field."),
                                maxPrice: Optional[float] = Query(None, description="The maximum value for the tradeDetails.price field."),
                                minPrice: Optional[float] = Query(None, description="The minimum value for the tradeDetails.price field."),
                                start: Optional[dt.datetime] = Query(None, description="The minimum date for the tradeDateTime field."),
                                tradeType: Optional[str] = Query(None, description="The tradeDetails.buySellIndicator is a BUY or SELL")):
    result = []
    for client in db:
        for trade_id in db[client]["trades"]:
            trade = db[client]["trades"][trade_id]
            if (not assetClass or trade["asset_class"].lower() == assetClass.lower()) and \
                (not tradeType or trade["trade_details"]["buy_sell_indicator"].lower() == tradeType.lower()) and \
                (not minPrice or trade["trade_details"]["price"] >= minPrice) and \
                (not maxPrice or trade["trade_details"]["price"] <= maxPrice) and \
                (not start or trade["trade_date_time"] >= start) and \
                (not end or trade["trade_date_time"] <= end):
                    result.append(trade)
    return {"trades": result}




# Running server
if __name__ == "__main__":
    
    uvicorn.run(app, host="localhost", port=8000)
