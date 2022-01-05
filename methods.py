import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd
import json
import os
from datetime import date
from pykalman import KalmanFilter

def read_config(filename):
    if (os.path.exists(filename)):
        with open("config.json", 'r') as jsonfile:
            config = json.load(jsonfile)
        return config
    else:
        raise FileNotFoundError   


def get_data_from_web(tickers, source, start_date, end_date, latest_closing_date=True):
    if latest_closing_date == True:
        today = date.today()
        end_date = today.strftime("%Y-%m-%d")
        
    panel_data = web.DataReader(tickers, source, start_date, end_date)

    return panel_data


def clean_data(raw_data, start_date, end_date, latest_closing_date):
    closing_price = raw_data['Close']

    if latest_closing_date == True:
        today = date.today()
        end_date = today.strftime("%Y-%m-%d")

    weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
    closing_price = closing_price.reindex(weekdays)
    closing_price = closing_price.fillna(method='ffill')
    closing_price = closing_price.fillna(method='bfill')

    return closing_price

def kalman_smoothing(series_data):
    kf = KalmanFilter(
                transition_matrices=[1],
                observation_matrices=[1],
                initial_state_mean=0,
                initial_state_covariance=1,
                observation_covariance=1,
                transition_covariance=0.01
            )
    state_means, _ = kf.filter(series_data)

    return state_means
    

def plot_data(data, tickers):
    for ticker in tickers:
        ticker_series = data.loc[:, ticker]
        short_term_rolling_average = ticker_series.rolling(window=7).mean()
        long_term_rolling_average = ticker_series.rolling(window=30).mean()        
        state_means = kalman_smoothing(ticker_series)

        fig, ax = plt.subplots(figsize=(16,9))

        ax.plot(ticker_series.index, ticker_series, label=ticker)
        ax.plot(short_term_rolling_average.index, short_term_rolling_average, label='7 Days Rolling Average')
        ax.plot(long_term_rolling_average.index, long_term_rolling_average, label='30 Days Rolling Average')
        ax.plot(ticker_series.index, state_means, label='Kalman Filter smoothed')

        ax.set_xlabel('Date')
        ax.set_ylabel('Adjusted closing price ($)')
        ax.set_title(ticker)
        ax.legend()
        plt.savefig('analysis/' + ticker + '.jpg')

    
def generate_statistics(raw_data, closing_price_data):
    if os.path.exists('analysis/statistics.txt'):
        file = open('analysis/statistics.txt', 'w')
        print(raw_data.describe(), file=file)
        file.close()
    else:
        with open('analysis/statistics.txt', 'w'):
            file = open('analysis/statistics.txt', 'w')
            print(raw_data.describe(), file=file)
            file.close()

    if os.path.exists('analysis/correlation.txt'):
        file = open('analysis/correlation.txt', 'w')
        print(closing_price_data.corr(), file=file)
        file.close()
    else:
        with open('analysis/correlation.txt', 'w'):
            file = open('analysis/correlation.txt', 'w')
            print(closing_price_data.corr(), file=file)
            file.close()

    closing_price_data.to_pickle('analysis/time_series_closing_data.pkl')