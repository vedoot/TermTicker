from time import sleep
import sys
import numpy as np
import pandas as pd
import plotext as plt


#Data Source
import yfinance as yf



color = ""

# wait for input from user
ticker = input("Enter ticker:\n")
        
while(True):
    
    data = yf.download(tickers=ticker, period='1d', interval='1m',prepost = True)

    # Gets the ticker's opening price    
    opening = yf.Ticker(ticker).info['open']

    # Since live, High is calculated as the max of all closing prices (1m apart)
    current_high = max(data["Close"].tolist())

    # y data will only show the most recent 10 hours of trades
    y = data["Close"].tail(600).tolist()

    # Current is the last index of all trades 
    current = y[-1]

    
    # Show red or green chart if price has declined since opening
    if current >= opening:
        color = "green"
    else:
        color = "tomato"


    #For formating
    plt.clear_plot()
    plt.clear_terminal()
    
    
    plt.scatter(y,point_color=color,fill = True,
                label=ticker + "- Open:" + str(opening) + " Current:" + str(current) + "1d High:" + str(current_high)) # Labled as Open: , Current: , High: 
    
    #Most recent hours of trades will be highlighted blue
    plt.scatter(list(range(540,600)),y[-60:],fill=True,label="Current Hour",point_color="blue")
    
    #More formating
    plt.canvas_color('none')
    plt.axes_color("none")
    plt.grid(False, False)
    plt.axes(False, False)
    # Adds padding to right side
    plt.xlim([0,625])    
    plt.ticks(0,10)

    # Render graph every 1m (API only updates at 1m intervals)
    plt.show()
    sleep(60)
   