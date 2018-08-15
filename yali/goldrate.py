import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gold_daily_rate.csv',index_col='Name',parse_dates=True)

data = df['Indian rupee'].replace('[\,]', '', regex=True).astype(float)
df_new = pd.DataFrame(data=data,index=df.index)

dec_2010_to_feb_2018 = df_new['2010':'2018'].resample('M')
dec_2010_to_feb_2018_median = dec_2010_to_feb_2018.mean()
dec_2010_to_feb_2018_max = dec_2010_to_feb_2018.max()
dec_2010_to_feb_2018_min = dec_2010_to_feb_2018.min()


#res = df_new[df_new['Indian rupee'] == max_of_dec_2016_to_feb_2018]
#print(res)


plt.plot(dec_2010_to_feb_2018_max)
plt.plot(dec_2010_to_feb_2018_median)
plt.plot(dec_2010_to_feb_2018_min)

plt.ylabel('Gold rate (INR)')
plt.xlabel('Monthy (min, avg, max)')
plt.show()
