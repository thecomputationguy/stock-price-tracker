import methods as methods

if __name__ == '__main__':

    # Read the config file to set the analysis parameters
    print("Reading Config File...")
    config = methods.read_config("config.json")

    tickers = config['tickers']
    start_date = config['start_date']
    end_date = config['end_date']
    latest_closing_date = config['latest_closing_date']
    source = config['source']
    print('Done.')
    
    # Clean up the data and extract the daily closing prices
    print("Cleaning and Extracting Data...")
    raw_data = methods.get_data_from_web(tickers, source, start_date, end_date, latest_closing_date )
    closing_price_data = methods.clean_data(raw_data, start_date, end_date, latest_closing_date)
    print('Done.')

    # Perform some simple statistical and correlation analysis and plotting
    print("Analyzing and Plotting data...")
    methods.analyze_data(raw_data, closing_price_data)
    methods.plot_data(closing_price_data, tickers)
    print('Done.')