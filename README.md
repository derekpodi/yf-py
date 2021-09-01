# yf-py

Produce a quick pie chart of buy/sell consensus of a stock.

Info taken from yahoo finance api (yfinance); investment grades counted and presented via Plotly.

Implements a python script as a GUI via Gooey.

Optional verbose feature to produce line graph via matplotlib - prints recent close prices to the command line.


# Non GUI Version
Old version of the script didn't have GUI implemented. 

Can use script directly from the command line (with or without user input) in the following way:
```
$ python3 yf.py <Stock Ticker>
```
Omission of the stock ticker will prompt user input.
