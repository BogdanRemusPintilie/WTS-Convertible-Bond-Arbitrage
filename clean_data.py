import pandas as pd

data = r"C:\Users\Bogdan\Desktop\CLEAN\WTS\Convertible bond arbitrage\data.csv"

df = pd.read_csv(data, na_values=["#N/A Field Not Applicable"])

df.dropna(inplace=True)

df = df[df['CV Stock Volatility'] != 0]

cleaned_file_path= r"C:\Users\Bogdan\Desktop\CLEAN\WTS\Convertible bond arbitrage\cleaned_data.csv"

df.to_csv(cleaned_file_path, index=False)
