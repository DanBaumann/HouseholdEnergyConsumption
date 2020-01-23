import pandas as pd
from scipy import stats
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv(filename):
    data = pd.read_csv(filename, infer_datetime_format=True, index_col=['datetime'])
    data.index = pd.to_datetime(data.index)
    return data 

def normality_test(data):
    statistic, p = stats.normaltest(data.global_active_power)
    alpha = 0.05
    if p > alpha:
        print('Data is Gaussian: failure to reject the null hypothesis')
    else:
        print('Data is not Gaussian: reject the null hypothesis, and accept the alternative')
    return statistic, p

def distribution_plot(data):
    plt.figure(figsize=(15, 6))
    sns.distplot(data.global_active_power)
    plt.title('Distribution of Global Active Power')
    plt.xlabel('Global Active Power')
    plt.yticks([])

    print('Kurtosis of Global Active Power Distribution: {}'.format(stats.kurtosis(data.global_active_power)))
    print('Skewness of Global Active Power Distribution: {}'.format(stats.skew(data.global_active_power)))
    

def test_stationarity(timeseries):
    rolmean = timeseries.rolling(window=30).mean()
    rolstd = timeseries.rolling(window=30).std()
    
    plt.figure(figsize=(14,5))
    sns.despine(left=True)
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')

    plt.legend(loc='best'); plt.title('Rolling Mean & Standard Deviation')

    
    print ('<Results of Dickey-Fuller Test>')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4],
                         index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)

def day_resample(data):
    data_days = data.resample('D')
    data_days = data_days.sum()
    return data_days