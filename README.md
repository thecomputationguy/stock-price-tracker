# stock-price-tracker
Python program to track the evolution of multiple stocks in a specified time-interval.

To track the historical evolution of stocks of your interest, enter the NASDAQ ticker symbol (e.g : APPL, TSLA etc.) in the 'config.json' file, in the "tickers" field. Then set the starting date of the request by setting it in the "start_date" field and the closing date under "end_date" and setting the "latest_closing_date" to 0. In case you want the latest closing date for your analysis, keep the "latest_closing_date" to 1.

This program uses the "pandas_datareader" method to fetch the past data from the yahoo finance api. The fetched data, plots and some basic analysis can be found in the analysis folder.

Parts of this program were motivated by the following article :

https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/