Fastapi =>  FastAPI is a modern, fast web framework for building APIs with Python 

uvicorn=> With fastapi i have used uvicorn. Uvicorn is a fast and asynchronus production ready server for python web applications.

mockdata.py => this file is used for random data as a constant db.

myapi.py => this file is used for writing code of api endpoints. 

==> for retrieving a particular trade we pass "client" and "trade_id" as params and it will return the result in dictionary format.

==> Pagination => for pagination initially we have decided number of trades on a page, so remaining part it will show on next page, which can be accessed using url. it is also showing metadata of remaining pages.
url example->  http://localhost:8000/trades?page_size=2&page_num=2

=> for searching trade with query like "counterparty","instrumentName",InstrumentId and "trader", I have used simple string matching algorithm.

==>Advanced filtering - in this case, search_trades_advanced function loops through entire database and returns the value in form of json response if it meets the specified search criteria. 


==> the application has been assigned port 8000 on localhost.

==> for running application type <myapi.py > in terminal.

