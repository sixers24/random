from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd
from functools import wraps


# normally this would be set by env vars or config
HOST = "postgresql://postgres:postgres@localhost/bluecrest"


# use the simplest version of sql alchemy architecture instead of full blown class defintions with metadata
#engine = create_engine(HOST)


def df_db_insert(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        engine = create_engine(HOST)
        with engine.connect() as con:
            func(con, *args, **kwargs)
    
    return wrapper

 

if __name__ == '__main__':
    df = pd.DataFrame([{'a': 1}])
    table = 'alpha_dev'
    
    @df_db_insert
    def foo(con):
        df.to_sql(table, if_exists='append', index=False, con=con)


    foo()


# with engine.connect() as con:
#     df.to_sql("first", con=con, if_exists='append', index=False)