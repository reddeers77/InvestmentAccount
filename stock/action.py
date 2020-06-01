import yfinance as yf
import pandas as pd


class Action():

    def __init__(self,ticker,date,amount):
        self.ticker=ticker
        self.date=date
        self.amount=amount
        

    def Buy_Price(self):
        try:
            ticker = yf.Ticker(self.ticker)            
            ticker = ticker.history(period='max')    
                      
            ticker = ticker.loc[self.date]    
            
            if len(ticker)>0:
                amount = ticker['Close']
                
                return amount
            else:
                return ('No data')
        except FileNotFoundError:
            print (' There is not file named as {}'.format(self.ticker))

    def Sell_Price(self):
        
        
        ticker = yf.Ticker(self.ticker)
        ticker = ticker.history(period='max')
        try:            
            amount = ticker.iloc[-1]
            amount = amount['Close']

        except KeyError :
            print('Hata')
            
        return amount

    def Today_Money(self,buy_price,sell_price):
        print(type(self.amount))
        print(type(buy_price))
        print('-------------------------------------------')
        paperCount = float((self.amount)/buy_price)
        paperValue = (paperCount*sell_price)
        paperValue = int(paperValue)
        return paperValue 

    def TickerName(self):
        ticker = yf.Ticker(self.ticker)
        data = ticker.info
        name = data['longName']
        return name