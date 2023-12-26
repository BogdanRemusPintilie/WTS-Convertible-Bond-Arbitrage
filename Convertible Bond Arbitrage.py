import math
from scipy.stats import norm
#from xbbg import blp
import pandas as pd
from datetime import datetime

tickers=[]
current_date= datetime.now()
formated_current_date=current_date.strftime("%d-%m-%y")
formated_current_date=datetime.strptime(formated_current_date, "%d-%m-%y")

data = r"C:\Users\Bogdan\Desktop\CLEAN\WTS\Convertible bond arbitrage\cleaned_data.csv"

df = pd.read_csv(data)

for index, row in df.iterrows():

    ticker= row["Ticker"]
    coupon_rate = row["Cpn"]

    maturity_date = datetime.strptime(row["Maturity"], "%d-%m-%y")
    maturity= (maturity_date - formated_current_date).days / 365
    
    conversion_ratio = row["Conversion Ratio"]
    stock_price =  100 #blp.bdp(ticker "US Equity", ["px_last"])['px_last'].values[0]
    risk_free_rate =  0.01 #blp.bdp("USGG10YR Index", ["px_last"])["px_last"].values[0]    ## It is actually px_last, stupid, is what it is
    face_value = 1000
    conversion_price = row["CV Conversion Price"]
    volatility = row["CV Stock Volatility"] #should be live data
    market_value = 200 #blp.bdp("ticker", ['px_last'])['px_last'].values[0]

    def calculate_bond_value(face_value, coupon_rate, risk_free_rate, maturity):
        coupon_payment = coupon_rate * face_value / 2
        bond_value = 0
        for t in range(1, int(2 * maturity) + 1):
            bond_value += coupon_payment / (1 + risk_free_rate / 2) ** t
        bond_value += face_value / (1 + risk_free_rate) ** maturity
        return bond_value

    def calculate_call_option_value(stock_price, conversion_price, risk_free_rate, maturity, volatility):
        d1 = (math.log(stock_price / conversion_price) + (risk_free_rate + (volatility ** 2) / 2) * maturity) / volatility  #*math.sqrt(maturity))
        d2 = d1 - volatility #* math.sqrt(maturity)
        call_option_value = stock_price * math.exp(-risk_free_rate * maturity) * norm.cdf(d1) - conversion_price * norm.cdf(d2)
        return call_option_value

    def calculate_fair_value_convertible_bond(face_value, coupon_rate, risk_free_rate, maturity, conversion_price, stock_price, volatility):
        bond_value = calculate_bond_value(face_value, coupon_rate, risk_free_rate, maturity)
        call_option_value = calculate_call_option_value(stock_price, conversion_price, risk_free_rate, maturity, volatility)
        fair_value = bond_value + call_option_value
        return fair_value

    fair_value = calculate_fair_value_convertible_bond(face_value, coupon_rate, risk_free_rate, maturity, conversion_price, stock_price, volatility)
    if fair_value<market_value:
        tickers.append(ticker)

print(tickers)
