import pandas as pd
import matplotlib.pyplot as plt


filename = 'Prices.xlsx'
xl = pd.ExcelFile(filename)
gram_per_ounce = 31.1034768

print(xl.sheet_names)

#Load sheet from xl named Daily
df = xl.parse('Daily',skiprows=8,usecols=[3,10],index_col='Name')

inr_col = 'Indian rupee'
df[inr_col] = df[inr_col].map(lambda x: x / gram_per_ounce)

from_2010_to_feb_2018 = df['2010':'2018'].resample('M')

cumulative = pd.DataFrame({"High": from_2010_to_feb_2018.max()[inr_col],
                    "Average": from_2010_to_feb_2018.mean()[inr_col],
                   "Low": from_2010_to_feb_2018.min()[inr_col]})
cumulative.plot()
plt.ylabel('Gold rate per gram (INR)')
plt.xlabel('Monthly')
plt.show()
