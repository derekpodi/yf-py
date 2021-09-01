#!usr/bin/env python3
#yf.py -- quick pie chart of buy/sell consensus from yahoo finance api investment bank grades

import argparse
import yfinance as yf
import sys
import os   #os.sys depreciated?
#import subprocess
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

from gooey import Gooey


def buy_or_sell(argv: str) -> None:
    ticker = yf.Ticker(str(argv))

    df = pd.DataFrame(ticker.recommendations)
    count = pd.DataFrame(df["To Grade"].value_counts())

    pie_chart(count)


def pie_chart(forecast: pd.DataFrame()) -> None:
    fig = px.pie(forecast, values="To Grade", names=forecast.index, title= ' Stock Consensus')           #title= argv + ' Stock Consensus'
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.show()


def open_close(argv: str) -> None:
    data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = argv,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "2y",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )
    print(argv + " Stock Close Price Information for the Past 5 Days:")
    close = data['Close']
    print(close.tail(5))
    plot_close(close, argv)


def plot_close(close, argv):
    #matplotlib
    ax = close.plot(title= argv + ' Stock Close Prices 2020 - Present')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close')
    ax.grid()
    plt.show()


@Gooey
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stock", type=str,
                    help="display buy/sell and trend of stock ticker")
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity - include line graph and recent close info")

    args = parser.parse_args()
    argv = args.stock.upper()
    
    if args.verbosity >= 1:
        try:
            argv = args.stock.upper()
            buy_or_sell(argv)
            open_close(argv)
        except:
            print("Exception occured. No data on stock input or maybe incorrect ticker symbol.")
    else:
        try:
            argv = args.stock.upper()
            buy_or_sell(argv)
        except:
            print("Exception occured. No data on stock input or maybe incorrect ticker symbol.")



if __name__ == '__main__':
    main()
    
    
    '''
    #Non-Gooey Approach -> use sys.argv checks, allows user input at command line

    if not len(sys.argv) > 1:
        #USER INPUT
        try:
            argv = str(input("Input the stock ticker: ")).upper()
            #os.system('python3 yf.py {}'.format(test))
            buy_or_sell(argv)
            open_close(argv)
        except:
            print("Exception occured. No data on stock input or maybe incorrect ticker symbol.")
        
    else:
        # COMMAND LINE 
        # $python3 yf.py <Stock Ticker>
        try:
            argv = str(sys.argv[1])
            buy_or_sell(argv)
            open_close(argv)
        except:
            print("Exception occured. No data on stock input or maybe incorrect ticker symbol.")
    '''
