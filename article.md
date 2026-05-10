# Time Series with the of power demand using Prophet in Python

This project uses hourly energy demand data from ERCOT in Texas to predict future demand.

### Time Series Forecasting example using power demand with Prophet in Python 

This project uses hourly energy demand data from ERCOT in Texas to predict future demand.



This chart is messy because it is hourly figures. We could smooth this out using resampling. For now, I am going to leave it.

Now let's predict the next 90 day period using Prophet.



In the chart we see that there are actual values (dots) that are more extreme than the predicted values. There does seem to be an annual pattern of ups and downs.

We can look at the predicted values from Prophet. The module creates a predictive value and a likely range.



Now we will create a graph using Plotly. This is HTML based so it can be put in normal websites and it allows users to "zoom in" to get more detail.


At a four year view, it is hard to see patterns.



We can zoom in to see the daily fluctuations.


Importing things we need.


Lets plot the data.



We are going to create new features based on the calendar.



The darker colors indicate increased demand.



Now we can slipt the data and see how things look



We split the data and now we build a model using the training data only. Then we can compare the test set with the predicted values.



We can decompose the time series to look at the seasonality and trends that are hidden in the time series.



Plot the forecast with the actual values.



Below are a few other stories I have written about time series.

[**Time series for solar power production with Prophet**\ *This simple project takes cumulative power production data from solar panels and predicts future generation. I use a...*medium.com](https://medium.com/@kylejones_47003/time-series-for-solar-power-production-with-prophet-9c0c0fac537b "https://medium.com/@kylejones_47003/time-series-for-solar-power-production-with-prophet-9c0c0fac537b")[](https://medium.com/@kylejones_47003/time-series-for-solar-power-production-with-prophet-9c0c0fac537b) [**Time series for unemployment and natural gas using Prophet and Plotly**\ *This simple project uses Bayesian time series to predict unemployment in the US. We visualize the data using Plotly...*medium.com](https://medium.com/@kylejones_47003/time-series-for-unemployment-and-natural-gas-using-prophet-and-plotly-cc0fb7417a1f "https://medium.com/@kylejones_47003/time-series-for-unemployment-and-natural-gas-using-prophet-and-plotly-cc0fb7417a1f")[](https://medium.com/@kylejones_47003/time-series-for-unemployment-and-natural-gas-using-prophet-and-plotly-cc0fb7417a1f) [**Time Series forecasting of natural gas prices with Python**\ *A common task in finance is forecasting values. There are several methods for creating forecasts such as ARIMA...*medium.com](https://medium.com/@kylejones_47003/time-series-forecasting-of-natural-gas-prices-with-python-b21c0d11019d "https://medium.com/@kylejones_47003/time-series-forecasting-of-natural-gas-prices-with-python-b21c0d11019d")[](https://medium.com/@kylejones_47003/time-series-forecasting-of-natural-gas-prices-with-python-b21c0d11019d)
