from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
from typing import List, Optional

raw_data = pd.read_csv("D:\\bitcoin\\demo\\Python-VeryPet\\visualize\\item_price.csv")
raw_data['price'] = raw_data.price.astype(float)
raw_data['volume'] = raw_data.volume.astype(int)
raw_data['time'] = pd.to_datetime(raw_data['time'])

dates = raw_data['time']
prices = raw_data['price']
volumes = raw_data['volume']

def mean(xs: List[float]) -> float:
    '''Mean value'''
    return sum(xs)/len(xs)

def l_min(xs: List[float]) -> float:
    '''Mix value'''
    return min(xs)

def l_max(xs : List[float]) -> float:
    '''Max value'''
    return max(xs)

def median(xs: List[float]) -> float:
    '''Find median'''
    xs = sorted(xs)
    if len(xs) % 2 == 0:
        pos1: int = len(xs) // 2
        pos2: float = pos1-1
        return (xs[pos1] + xs[pos2]) / 2
    else:
        return xs[len(xs) // 2] 

def quantile(xs: List[float],p:float) -> float:
    '''Find quantile value'''
    p_index = int(p*len(xs))
    return sorted(xs)[p_index]

def mode(xs: List[float]) -> List[float]:
    '''Find mode value(s)'''
    counts = Counter(xs)
    max_count = max(counts.values())
    return [xs_i for xs_i,count in counts.items() if count == max_count]

if __name__ == '__main__':
    print("mean:\t\t",mean(prices))
    print("min:\t\t",l_min(prices))
    print("max:\t\t",l_max(prices))
    print("median:\t\t",median(prices))
    print("quantile:\t",quantile(prices,0.75))
    print("mode:\t\t",mode(prices))
