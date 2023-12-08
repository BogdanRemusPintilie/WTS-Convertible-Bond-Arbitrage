import blpapi
import pandas as pd

# Establish connection to Bloomberg Terminal
sessionOptions = blpapi.SessionOptions()
sessionOptions.setServerHost("your_bloomberg_server_host")
sessionOptions.setServerPort(your_bloomberg_server_port)
session = blpapi.Session(sessionOptions)
session.start()
session.openService("//blp/refdata")

# Fetch current stock price of Apple
ticker = "AAPL"
field = "LAST_PRICE"  # Replace with the desired field
request = service.createRequest("ReferenceDataRequest")
request.getElement("securities").appendValue(ticker)
request.getElement("fields").appendValue(field)
session.sendRequest(request)

# Retrieve and store the stock price
stock_price = None
while True:
    event = session.nextEvent()
    for msg in event:
        if msg.messageType() == blpapi.Name("ReferenceDataResponse"):
            stock_price = msg.getElement("securityData").getElement("fieldData").getElementAsString(field)
            break
    if event.eventType() == blpapi.Event.RESPONSE:
        break

session.stop()

# Use the fetched stock price in your calculations
# Continue with your fair value calculation code using the retrieved stock price variable