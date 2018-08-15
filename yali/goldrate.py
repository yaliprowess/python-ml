import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gold_daily_rate.csv',index_col='Name',parse_dates=True)
gram_per_ounce = 31.1034768

data = df['Indian rupee'].replace('[\,]', '', regex=True).astype(float) / gram_per_ounce
df_new = pd.DataFrame(data=data,index=df.index)
inr_col = 'Indian rupee'


from_2010_to_feb_2018 = df_new['2010':'2018'].resample('M')

cumulative = pd.DataFrame({"High": from_2010_to_feb_2018.max()[inr_col],
                    "Average": from_2010_to_feb_2018.mean()[inr_col],
                   "Low": from_2010_to_feb_2018.min()[inr_col]})
cumulative.plot()
plt.ylabel('Gold rate per gram (INR)')
plt.xlabel('Monthly')
plt.show()
