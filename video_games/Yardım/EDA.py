import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def DescribeData(data):
    print(data.describe())
    print("------\n Column Types -----------")
    print(data.dtypes.value_counts())

def controlNaNvalues(data):
    print(data.isna().sum())
    print("-----\n")
    x=(data.isna().sum())/(data.shape[0])
    df=pd.DataFrame({'Bos_Sutunların_oranı': x})
    return df

def visSwarmPlot(data,x,y,hue):

    sns.swarmplot(data = data, 
                y = y, 
                x = x,hue=hue,dodge=True)
    plt.title('Title Sentiment Analysis')
    plt.legend(prop={'size': 5})
    plt.show()