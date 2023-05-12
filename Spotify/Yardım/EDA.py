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
    df=pd.DataFrame({'Bos_Sutunların_oranı': x})
    return df
    


## GÖRSELLEŞTİRME 
#Daha kullanışlı.
def BarPlot(data,degisken,n,color):
    """datanızı temsil ederken , degisken: datadaki hangi sutunda gösterileceğini temsil eder ,n ise topN temsil etmektedir. En popüler kaç ismi görmek istersiniz gibi.
     color ise color kodunu giriniz. """
    
    mostPopular=data[degisken].sort_values(ascending=False)

    x=list(mostPopular.index[:n])
    y=list(mostPopular.values[:n])

    name=[]
    for i in x:
        name.append(data.loc[i,'track_name'])
    
    print(name)
    plt.figure(figsize=(10,7))
    plt.barh(name,y,label='Firmadaki En Popüler Sanatçılar',color=color)
    plt.ylabel('Sanatçılar')
    plt.xlabel('Popülerlik Düzeyi')
    plt.title('Pointplot Chart')
    plt.legend()
    plt.show()



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
    plt.barh(name,y,label='Firmadaki En Popüler Sanatçılar',color='#306632')
    plt.xlabel('Sanatçılar')
    plt.ylabel('Popülerlik Düzeyi')
    plt.title('Pointplot Chart')
    plt.legend()
    plt.show()


def LoudnessBarPlot(data,n):
    MostLoudness=data['loudness'].sort_values(ascending=False)

    x=list(MostLoudness.index[:n])
    y=list(MostLoudness.values[:n])


    name=[]
    for i in x:
        name.append(data.loc[i,'track_name'])

    plt.figure(figsize=(10,10))
    sns.barplot(data=data, x=name, y=y,saturation = 0.1)
    plt.xlabel('Şarkılar')
    plt.ylabel('Gürültü Düzeyi')
    plt.title('Pointplot Chart')
