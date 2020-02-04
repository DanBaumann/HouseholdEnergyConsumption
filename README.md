<h1 align='center'>Household Energy Consumption</h1>
<br>
<h3 align='center'>Daniel Baumann</h1>
<br>
____________________________________________________________________________________________________________________________
<h3 align='center'>The Problem</h3>

Accurately forecasting household energy consumption is a problem that energy suppliers often encounter. This project aims to provide a tool in which energy suppliers can forecast energy consumption. 

It is in the interest of energy suppliers to develop models that can forecast energy consumption so that they can reduce energy wastage, and thus cost. In addition to the monetary aspect of energy supply, there is an increasing demand through socially-driven thought to reduce energy wasteage in an attempt to protect the whithering effects of climate change. 

Using a dataset which contains minute-by-minute observation of a single household located near Paris, France, I attempted to accurately forecast energy consumption with different methods of time series forecasting. 
____________________________________________________________________________________________________________________________
<h3 align='center'>Project Objectives</h3>

The aim of this project is to create a model which can accurately predict future energy consumption. As this is a time series data, there will be important seasonal and daily trend factors which can be incorporated into the model.

The dataset includes the following variables [link](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption):

* Global active power (the target variable)
* Global reactive power
* Voltage
* Global intensity
* Power readings across different locations in the household
____________________________________________________________________________________________________________________________
<h3 align='center'>Methods Used</h3>

* Data visualisation
* Feature engineering
* Using DarkSky API for weather data
* Modelling
  * Naive modelling
    * Using daily, weekly and weekly one-year-ago averages to forecast
  * SARIMAX MODELLING
    * Using weather data as an exogenous variable to help with forecasting energy consumption 
  * LSTM Recurrent Neural Networks
    * Using a look-back of 100 minutes to forecast energy consumption 
____________________________________________________________________________________________________________________________
<h3 align='center'>Project Contents</h3>

The project contains the following:
    
* Exploratory data analysis of all variables
  * Producing visualisations including scatter plots and boxplots to determine how energy is consumed
  * Data cleaning for period where energy consumption was anomalous
    * It was apparent that this household took holiday days where consumption was practically zero. This is likely not to be the case across all households so this required some data imputing
* Statistical testing
  * Normality test
  * Dickey-Fuller test for stationaryity of time series data
* There was a clear relationship with outside temperature and energy consumption, so I used DarkSky API to retrieve weather data in the given location (a town just ouside Paris)
* Creating a multitude of models that increased in complexity and computing power
  * Starting with naïve modelling, then to autoregressive moving average models and finally at an LSTM model (this required google cloud computing)
* Visualisations and evaluation of results, using root mean squared error as an evaluation metric
  * RMSE is a good evaluation metric if you want to penalise predictions that are far away from actual values
  
____________________________________________________________________________________________________________________________
<h3 align='center'>Project Description and Results</h3>

The dataset required extensive cleaning and feature engineering to cater for seasonal factors. I saw that the time of year was very important so I added categorical columns of year, quarter, month, and whether it was a weekday or not. To be precise, it was evident that in colder months, energy consumption was at a substantially higher value, as well as weekend consumption being much higher than weekday consumption. Intuitively these both made sense as energy for heating is required in colder months, and more time being spent at home during the weekdays. 

I began with very basic modelling of energy consumption, using daily averages to predict the next day of consumption. I then compared these averages with weekly average and weekly one year averages and found that using daily averages performed the best. 

As the above forecasting techniques were very simple, I wanted to capture more model complexity by adopting a autoregressive moving average technique. By looking for autocorrelation and partial autocorrelation in the data, it was clear that energy consumption was strongly auto-correlated to several time-lags before, but partial autocorrelation was only relevant for one lag. As this is minute-by-minute data this makes sense, with the last minute likely to capture almost the entirety of future energy consumption. I then began to run a SARIMAX model grid-search which tries to look for the best fit, using RMSE as my evaluation metric. I arrived at a RMSE of 51 kilowatts when resampled over hourly predictions. 

The final model invovled using Long-Short Term Memory neural networks. This method uses a self-defined lookback (of which i used 100 minutes) to make the prediction about the next minute. This undoubtedly performed the best as this model is able to use the last 100 minutes of data to make the prediciton about the next minute. The testing set had a RMSE of 0.26, which resampled over an hour is approximately 15.6 kilowatts. This outperforms the SARIMAX model three-fold. The drawbacks of the model are that it requires a constant influx of data to make minute predictions on energy consumption. This could pose both a problem for data collection as well as dynamic energy supply from energy suppliers. However, with the adoption of smart meters across many households, this type of modelling may be possible now, and certainly in the future. 
