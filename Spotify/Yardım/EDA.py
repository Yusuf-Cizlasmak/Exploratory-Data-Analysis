import numpy as np 
import pandas as pd
from Yardım.EDA import *

import matplotlib.pyplot as plt
import seaborn as sns


def DescribeData(data):
    print(data.describe().T)
    print("------\n")
    print(data.dtypes.value_counts())

def controlNaNvalues(data):
    print(data.isna().sum())
    print("-----\n")
    x=(data.isna().sum())/(data.shape[0])
    df=pd.DataFrame(data=x)
    


## GÖRSELLEŞTİRME 
def PopularBarPlot(data,n):
    """datanızı temsil ederken , n ise topN temsil etmektedir. En popüler kaç ismi görmek istersiniz gibi. """
    
    mostPopular=data['popularity'].sort_values(ascending=False)

    x=list(mostPopular.index[:n])
    y=list(mostPopular.values[:n])

    name=[]
    for i in x:
        name.append(data.loc[i,'artist_name'])
    
    print(name)
    plt.figure(figsize=(10,7))
    plt.barh(name,y,color='#306632')

    plt.show()