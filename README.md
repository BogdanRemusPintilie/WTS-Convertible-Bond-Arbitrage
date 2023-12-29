# WTS-Convertible-Bond-Arbitrage
Convertible bond arbitrage trading strategy using live Bloomberg data.

I used Bloomberg's API since Yahoo Finance doesn't provide data on convertible bonds from what I have seen

Problems:
The main issue is when you extract data from Bloomberg in Excel you will not get the ticker name in full. However, hover any ticker and you'll see the full name. For example, a US equity would go MSFT US Equity not just MSFT and you don't retrieve any DataFrame unless you use the full name. So you need the full ticker name of the Convertible Bond. The method in Python blp.bdp() requires the ticker. Tried with CUSIP, ISIN doesn't retrieve anything. So if you fix the ticker I reckon you can fetch live stock_price and CB_price. The risk-free rate is good.

I might have messed up the maturity so I commented it out of the code, so make sure you fix that otherwise the formulas are hot garbage. I got math errors so I assummed maturity <=0 which shouldn't happen given I filtered for future maturity dates and there is an if statement which should take care of it and still got error, so once fixed get rid of if state,ment. So I messed up the maturity somehow.

Rest can be seen in comments.

The data comes from Bloomberg. Add path to data = r"..."

Good luck!
