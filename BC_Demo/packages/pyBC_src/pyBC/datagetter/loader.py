from pyBC.datagetter.db import df_db_insert
import pandas as pd
import numpy as np
 


@df_db_insert
def get_data(con) -> pd.DataFrame:
    query = """
    SELECT "Date",  "Close",   ticker
	FROM public.equity_mkt
    where "Date" > '2022-01-01'
    """
    df = pd.read_sql(query, con=con)
     
    return df 


def get_prices_df() -> pd.DataFrame:
    df = get_data()
    tabular = df.pivot(index='Date', columns='ticker', values='Close')
    tabular = tabular.reset_index().set_index('Date')
    return tabular

