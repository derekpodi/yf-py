# yf.py

Produce a quick pie chart of buy/sell consensus of a stock.

Implements a python script as a GUI via Gooey.

```
$python3 yf.py 
```

Data taken from yahoo finance api (yfinance). Investment grade ratios are transformed via Pandas and presented via Plotly.

Optional verbose feature to produce line graph via matplotlib - prints recent close prices to the command line.


# Non GUI Version
Old version of the script didn't have GUI implemented. 

Can use script directly from the command line (with or without user input) in the following way:
```
$ python3 yf.py <Stock Ticker>
```
Omission of the stock ticker will prompt user input.

* Must uncomment block in python script under main() *
