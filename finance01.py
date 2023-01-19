# https://www.youtube.com/watch?v=28dG0gyXz80&list=PLIHpLBNsiHE3pAd2JQUAFrgb7h6o6I4l3

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.seasonal import seasonal_decompose

ticket = yf.Ticker('^BVSP')

df = ticket.history(interval = '1d', start = '2022-01-01', end = '2023-01-01')

print(df.head())

