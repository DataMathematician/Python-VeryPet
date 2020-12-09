from matplotlib import pyplot as plt
import pandas as pd

raw_data = pd.read_csv("item_price.csv")
raw_data['price'] = raw_data.price.astype(float)
raw_data['volume'] = raw_data.volume.astype(int)
raw_data['time'] = pd.to_datetime(raw_data['time'])

plt.plot(raw_data.time,raw_data.price)
plt.bar(raw_data.time,raw_data.volume)