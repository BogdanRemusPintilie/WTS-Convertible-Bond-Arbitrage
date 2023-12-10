# Convertible Bond Arbitrage Strategy
# Variables
coupon_rate = 0.05
maturity = 5  # in years
conversion_ratio = 10
stock_price = 150  # Current stock price
risk_free_rate = 0.02  # Risk-free interest rate
face_value = 100000000 # How much money you trade
conversion_price = 170  # Conversion price of the convertible bond = price of equity if option excercised
volatility = 0.3  # stock's volatility

# Calculate the fair value of the bond
coupon_payment = coupon_rate * face_value / 2  # Assuming semi-annual payments so you collect this 10 times #HERE IS THE MISTAKE CAUSE CUPON PAYMENT IS NOT CONSTANT IT INCREASES CAUSE YOU FACTOR IN THE INTEREST YOU RECIVE IN THE PREVIOUS ITERATION
bond_value = 0

for t in range(1, 2 * maturity + 1):
    bond_value += coupon_payment / (1 + risk_free_rate / 2) ** t # risk_free_rate/2 because of the semi annual payment

bond_value += face_value / (1 + risk_free_rate) ** maturity

import math
#Calculate fair price of option                         ## THIS BIT HAS TO BE REPLACED. NEED SMTH FOR CONVERTIBLE BONDS
# Function to calculate Black-Scholes d1 and d2
def calculate_d1_d2(stock_price, conversion_price, risk_free_rate, maturity, volatility):
    d1 = (math.log(stock_price / conversion_price) + (risk_free_rate + (volatility ** 2) / 2) * maturity) / (volatility * math.sqrt(maturity))
    d2 = d1 - volatility * math.sqrt(maturity)
    return d1, d2
       
# Calculate d1 and d2 using the function
d1, d2 = calculate_d1_d2(stock_price, conversion_price, risk_free_rate, maturity, volatility)

                                                    

from scipy.stats import norm
# Calculate the call option value using Black-Scholes formula
call_option_value = stock_price * math.exp(-risk_free_rate * maturity) * norm.cdf(d1) - conversion_price * norm.cdf(d2)



                                                        ########


fair_value_convertible_bond = bond_value + call_option_value

print("The fair value of the convertible bond is:", fair_value_convertible_bond)
