import math
from scipy.stats import norm
from xbbg import blp
import pandas



def calculate_bond_value(face_value, coupon_rate, risk_free_rate, maturity):
    coupon_payment = coupon_rate * face_value / 2
    bond_value = 0
    for t in range(1, 2 * maturity + 1):
        bond_value += coupon_payment / (1 + risk_free_rate / 2) ** t
    bond_value += face_value / (1 + risk_free_rate) ** maturity
    return bond_value

def calculate_call_option_value(stock_price, conversion_price, risk_free_rate, maturity, volatility):
    d1 = (math.log(stock_price / conversion_price) + (risk_free_rate + (volatility ** 2) / 2) * maturity) / (volatility * math.sqrt(maturity))
    d2 = d1 - volatility * math.sqrt(maturity)
    call_option_value = stock_price * math.exp(-risk_free_rate * maturity) * norm.cdf(d1) - conversion_price * norm.cdf(d2)
    return call_option_value

def calculate_fair_value_convertible_bond(face_value, coupon_rate, risk_free_rate, maturity, conversion_price, stock_price, volatility):
    bond_value = calculate_bond_value(face_value, coupon_rate, risk_free_rate, maturity)
    call_option_value = calculate_call_option_value(stock_price, conversion_price, risk_free_rate, maturity, volatility)
    fair_value = bond_value + call_option_value
    return fair_value

# Example usage:
# The problem is there aren't idnetifiers in Bloomberg for all the below.
# Basically the point is to run this code for all outsdanting tickers and spit out the ones that market price<fair value (ar bigger than)
# so one way is through exporting current data on all CBs from Bloomberg and using that data to do the trick for the variables missing an identifier
coupon_rate = 0.05
maturity = 5
conversion_ratio = 10
stock_price = blp.bdp("MSFT US Equity", ["Security Name", "px_last"])['px_last'].values[0]
risk_free_rate = blp.bdp("USGG10YR", ["px_last"])["px_last"].values[0]
face_value = 100000000
conversion_price = 170
volatility = 0.3

fair_value = calculate_fair_value_convertible_bond(face_value, coupon_rate, risk_free_rate, maturity, conversion_price, stock_price, volatility)
print("The fair value of the convertible bond is:", fair_value)
