# stock-price-tracker
Python program to track the evolution of multiple stocks in a specified time-interval.

To track the historical evolution of stocks of your interest, enter the NASDAQ ticker symbol (e.g : APPL, TSLA etc.) in the 'config.json' file, in the "tickers" field. Then set the start date of the request by setting it in the "start_date" field and the closing date under "end_date" and setting the "latest_closing_date" to 0. In case you want the end date of your analysis to be set to today (or the last working day), keep the "latest_closing_date" to 1.

This program uses the "pandas_datareader" method to fetch the data from the yahoo finance api. The fetched time series data, plots and some basic analysis can be found in the analysis folder.

To run the program,

    1. In a Linux terminal, navigate to the program folder and run 'pip3 install -r requirements.txt'

    2. Once the dependencies are installed via Step 1, check if the paramters in the 'config.json' are to you liking or modify them as you wish.

    3. Run 'python3 price_tracker.py'

Parts of this program were motivated by the following article :

https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/