import pandas as pd
from .db import df_db_insert
import yfinance as yf 

HOST = "postgresql://postgres:postgres@localhost/bluecrest"
 
# list.csv is a list of all equity market tickers
df = pd.read_csv('list.csv')
df = df[df['Symbol'].notnull()] # apparently nulls in the data

 
@df_db_insert
def load_all_tickers(con):
    for symbol in df['Symbol'].to_list():
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="max")
        #hist.to_sql(f"ticker_{symbol}", con=con, if_exists='append') # save to a 
        hist['ticker'] = symbol 
        hist.to_sql(f"equity_mkt", con=con, if_exists='append', )
        #hist.to_csv(f"ticker_{symbol}.csv")
        print('finished', symbol)

if __name__ == '__main__':
    load_all_tickers()