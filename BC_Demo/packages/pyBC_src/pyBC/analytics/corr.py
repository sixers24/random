import pandas as pd 
import numpy as np
import statsmodels.api as sm


class PairwiseCorr(object):

    def __init__(self, df, period:int) -> None:
        self.raw_df = df
        self.df = df

    @staticmethod
    def pairwise_corr(df, n=5) -> pd.DataFrame:
        corr_df = df.corr()
        corr_df = corr_df.where(np.triu(np.ones(corr_df.shape)).astype(np.bool)) # get upper left diagonal correlation matrix ( to avoid duplicates)
        top_corr = pd.DataFrame(corr_df.unstack())
        top_corr['ticker1'] = top_corr.index.get_level_values(0)
        top_corr['ticker2'] = top_corr.index.get_level_values(1)

        #top_corr.index = [i for i in range(0, len(top_corr))]

        top_corr = top_corr[top_corr['ticker1'] != top_corr['ticker2']]
        top_corr.rename(columns={0: 'corr'}, inplace=True)

        top_corr  = top_corr[top_corr['corr'].notnull()]

        top_corr.sort_values('corr', ascending=False, inplace=True)
        top_bottom_n_corr = pd.concat([top_corr.head(n), top_corr.tail(n)]).reset_index(drop=True)
        return top_bottom_n_corr

    @staticmethod
    def OLS_regression(df, combo) -> float:
        """
        Find max of R^2 as explained by model, not a good measure I know
        """
        mod = sm.OLS(df[combo[0]], df[combo[1]])
        res = mod.fit()
        return res.rsquared

    @staticmethod
    def cointegration(df, combo) -> int:
        return 1



class CorrClient(object):

    def __init__(self, df, period) -> None:
        self.raw_df = df
        self.df = df
        self.period = period  

    # def numeric_period_cut(self, n=None):
    #     if n is None:
    #         n = self.period
    #     else:
    #         self.period = n  

    #     self.df = self.raw_df[:n]

    # def duration_period_cut(self, start=None, end=None):
    #     start = self.raw_df.index.min() if start is None else start 
    #     end = self.raw_df.index.max() if end is None else end 
    #     self.df = self.raw_df[start:end]
 
    @staticmethod
    def pearson(df, n=5) -> pd.DataFrame:
        corr_df = df.corr()
        corr_df = corr_df.where(np.triu(np.ones(corr_df.shape)).astype(np.bool)) # get upper left diagonal correlation matrix ( to avoid duplicates)
        top_corr = pd.DataFrame(corr_df.unstack())
        top_corr['ticker1'] = top_corr.index.get_level_values(0)
        top_corr['ticker2'] = top_corr.index.get_level_values(1)

        #top_corr.index = [i for i in range(0, len(top_corr))]

        top_corr = top_corr[top_corr['ticker1'] != top_corr['ticker2']]
        top_corr.rename(columns={0: 'corr'}, inplace=True)

        top_corr  = top_corr[top_corr['corr'].notnull()]

        top_corr.sort_values('corr', ascending=False, inplace=True)
        top_bottom_n_corr = pd.concat([top_corr.head(n), top_corr.tail(n)]).reset_index(drop=True)
        return top_bottom_n_corr

    @staticmethod
    def OLS_regression(df, combo) -> float:
        """
        Find max of R^2 as explained by model, not a good measure I know
        """
        mod = sm.OLS(df[combo[0]], df[combo[1]])
        res = mod.fit()
        return res.rsquared