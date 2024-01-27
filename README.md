# WTS-Convertible-Bond-Arbitrage
Convertible bond arbitrage trading strategy using live Bloomberg data.

I used Bloomberg's API since, from what I have seen, Yahoo Finance doesn't provide data on convertible bonds.

Problems:
The main issue is that you will not get the ticker name in full when you extract data from Bloomberg in Excel. However, hover any ticker, and you'll see the full name. For example, a US equity would go MSFT US Equity, not just MSFT, and you don't retrieve any DataFrame unless you use the full name. So you need the full ticker name of the Convertible Bond. The method in Python blp.bdp() requires the ticker. I tried with CUSIP and ISIN, but it doesn't retrieve anything. So, if you fix the ticker, I reckon you can fetch live stock_price and CB_price. The risk-free rate is good.

I messed up the maturity, so I commented it out of the code. Could you make sure you fix that? Otherwise, the formulas are hot garbage. I got math errors, so I assumed maturity <=0, which shouldn't happen given that I filtered for future maturity dates. There is an if statement that should take care of it, but it still got an error, so once fixed, get rid of the if statement. So, I messed up the maturity somehow.

The rest can be seen in the comments.

The data.csv comes from Bloomberg.

Good luck!
