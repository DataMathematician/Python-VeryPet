from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
from typing import List, Optional
from visualize.central_tendentions import mean,quantile
from math import sqrt

raw_data = pd.read_csv("D:\\bitcoin\\demo\\Python-VeryPet\\visualize\\item_price.csv")
raw_data['price'] = raw_data.price.astype(float)
raw_data['volume'] = raw_data.volume.astype(int)
raw_data['time'] = pd.to_datetime(raw_data['time'])

dates = raw_data['time']
prices = raw_data['price']
volumes = raw_data['volume']

def _sq_deviations(xs: List[float]) -> List[float]:
    mat = mean(xs)
    return [(x - mat)**2 for x in xs]



def data_range(xs: List[float]) -> float:
    '''Range between max and min values in list'''
    return max(xs) - min(xs)


def variance(xs: List[float]) -> float:
    '''General variance'''
    return sum(_sq_deviations(xs)) / len(xs) 

def mean_sqrt_error(a:float) -> float:
    '''Mead square error'''
    return sqrt(a)

def iq_range(xs: List[float]) -> float:
    '''Interquantile range'''
    return quantile(xs,0.75) - quantile(xs,0.25)

if __name__ == "__main__":
    print("Range:\t\t",data_range(prices))
    print("Variance:\t",variance(prices))
    print("MSE:\t\t",mean_sqrt_error(variance(prices)))
    print("IQRange:\t",iq_range(prices))