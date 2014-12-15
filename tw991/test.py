"""
Creator: Tian Wang

Contributor: Wenxi Lei, Sylvia Zhao
"""

from measures_and_portfolio.stockfunction import *
from datetime import datetime
import unittest

class Test_sma(unittest.TestCase):
    """
    Test sma(Series, int) function
    """
    def setUp(self):
        self.input_2col_df = pd.DataFrame({'a':[1,2,3],'b':[10,20,30]})
        self.dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
        self.input_true_df = pd.Series([1,2,3,4,5,6], index = self.dates, name = 'Return')
        self.output_true_df = pd.Series([np.nan, np.nan, 2, 3, 4, 5], index = self.dates, name = 'Return_sma_3')

    def test_trueoutput(self):
        sma_answer = sma(self.input_true_df, 3)
        self.assertListEqual(list(sma_answer[~np.isnan(sma_answer)]), list(self.output_true_df[~np.isnan(self.output_true_df)]))
        self.assertEqual(len(sma_answer), len(self.output_true_df))
        self.assertEqual(sma_answer.name, self.output_true_df.name)

    def test_MultipleCol_exception(self):
        with self.assertRaises(MultipleCol):
            sma(self.input_2col_df, 1)

    def test_Invalidperiodlength_exception(self):
        with self.assertRaises(Invalidperiodlength):
            sma(self.input_true_df, 7)
        with self.assertRaises(Invalidperiodlength):
            sma(self.input_true_df, 1.5)

    def test_InvalidinputData_exception(self):
        with self.assertRaises(InvalidinputData):
            sma('asdf', 11)


class Test_std(unittest.TestCase):
    """
    Test std(Series, int)
    """
    def setUp(self):
        self.dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
        self.input_true_df = pd.Series([1,2,3,4,5,6], index = self.dates, name = 'Return')
        self.output_true_df = pd.Series([np.nan, np.nan, np.std([1,2,3]), np.std([2,3,4]), np.std([3,4,5]), np.std([4,5,6])], index=self.dates, name = 'Return_std_3')

    def test_trueoutput(self):
        std_answer = std(self.input_true_df, 3)
        self.assertListEqual(list(std_answer[~np.isnan(std_answer)]), list(self.output_true_df[~np.isnan(self.output_true_df)]))
        self.assertEqual(len(std_answer), len(self.output_true_df))
        self.assertEqual(std_answer.name, self.output_true_df.name)


class Test_boll(unittest.TestCase):
    """
    Test boll(Series, int, float)
    """
    def setUp(self):
        self.input_2col_df = pd.DataFrame({'a':[1,2,3],'b':[10,20,30]})
        self.dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
        self.input_true_df = pd.Series([1,2,3,4,5,6], index = self.dates, name = 'Return')
        self.output_true_df = pd.DataFrame({'Return_boll_3_1_Upper':[np.nan, np.nan, 2 + np.std([1,2,3]), 3 + np.std([2,3,4]), 4 + np.std([3,4,5]), 5 + np.std([4,5,6])], 'Return_boll_3_1_Lower':[np.nan, np.nan, 2 - np.std([1,2,3]), 3 - np.std([2,3,4]), 4 - np.std([3,4,5]), 5 - np.std([4,5,6])] , 'Return_boll_3_1_Mean':[np.nan, np.nan, 2, 3, 4, 5]})
        self.output_true_df = self.output_true_df[['Return_boll_3_1_Upper', 'Return_boll_3_1_Lower', 'Return_boll_3_1_Mean']]

    def test_trueoutput(self):
        boll_answer = boll(self.input_true_df, 3, 1)
        self.assertListEqual(list(boll_answer[~np.isnan(boll_answer)]), list(self.output_true_df[~np.isnan(self.output_true_df)]))
        self.assertEqual(len(boll_answer), len(self.output_true_df))
        self.assertListEqual(list(boll_answer.columns), list(self.output_true_df.columns))

    def test_MultipleCol_exception(self):
        with self.assertRaises(MultipleCol):
            boll(self.input_2col_df, 1,3)

    def test_Invalidperiodlength_exception(self):
        with self.assertRaises(Invalidperiodlength):
            boll(self.input_true_df, -1, 3)
        with self.assertRaises(Invalidperiodlength):
            boll(self.input_true_df, 'aa', 4)
        with self.assertRaises(Invalidperiodlength):
            boll(self.input_true_df, 0.5, 3)
        with self.assertRaises(Invalidperiodlength):
            boll(self.input_true_df, 7, 2)

    def test_BollinvalidK_exception(self):
        with self.assertRaises(BollinvalidK):
            boll(self.input_true_df, 1, -1)
        with self.assertRaises(BollinvalidK):
            boll(self.input_true_df, 1, 'aa')


class Test_macd(unittest.TestCase):
    """
    Test macd(series, slow, fast) function
    """
    def setUp(self):
        self.dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
        self.input_true_df = pd.Series([1,2,3,4,5,6], index = self.dates, name = 'Return')
        self.output_true_df = pd.Series([np.nan, np.nan, np.nan, 0.5, 0.5, 0.5], index=self.dates, name = 'Return_macd_4_3')

    def test_trueoutput(self):
        macd_answer = macd(self.input_true_df, 4, 3)
        self.assertListEqual(list(macd_answer[~np.isnan(macd_answer)]), list(self.output_true_df[~np.isnan(self.output_true_df)]))
        self.assertEqual(len(macd_answer), len(self.output_true_df))
        self.assertEqual(macd_answer.name, self.output_true_df.name)

    def test_Invalidperiodlength_exception(self):
        with self.assertRaises(Invalidperiodlength):
            macd(self.input_true_df, -1, 3)
        with self.assertRaises(Invalidperiodlength):
            macd(self.input_true_df, 1, -5)
        with self.assertRaises(Invalidperiodlength):
            macd(self.input_true_df, 'aa', 4)
        with self.assertRaises(Invalidperiodlength):
            macd(self.input_true_df, 0.5, 3)
        with self.assertRaises(Invalidperiodlength):
            macd(self.input_true_df, 7, 2)


class Test_daily_return(unittest.TestCase):
    """
    Test daily_return(series) function
    """
    def setUp(self):
        self.dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
        self.input_true_df = pd.Series([1,2,3,4,5,6], index = self.dates, name = 'Close')
        self.output_true_df = pd.Series([np.nan, float(1)/1, 0.5, float(1)/3, float(1)/4, float(1)/5], index=self.dates, name='return')
        self.input_negative = pd.Series([1,-2,3,4,5,6], index = self.dates, name = 'Close')

    def test_trueoutput(self):
        daily_return_answer = daily_return(self.input_true_df)
        self.assertListEqual(list(daily_return_answer[~np.isnan(daily_return_answer)]), list(self.output_true_df[~np.isnan(self.output_true_df)]))
        self.assertEqual(len(daily_return_answer), len(self.output_true_df))
        self.assertEqual(self.output_true_df.name, daily_return_answer.name)

    def test_Negativevalue_exception(self):
        with self.assertRaises(Negativevalue):
            daily_return(self.input_negative)

class Test_sharpe(unittest.TestCase):
    """
    Test sharpe(series, period) function
    """
    def setUp(self):
        self.dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
        self.input_true_df = pd.Series([1,2,3,4,5,6], index = self.dates, name = 'Close')
        self.daily_returns = daily_return(self.input_true_df)
        self.output_true_df = pd.Series([np.nan, np.nan, round(2/np.std([1/1,float(1)/2]),3), round(1/np.std([float(1)/2, float(1)/3]), 3), round(float(2)/3/(np.std([float(1)/3, float(1)/4])), 3), round(0.5/np.std([float(1)/4, float(1)/5]), 3)], index=self.dates, name='sharpe')
        self.input_negative = pd.Series([1,-2,3,4,5,6], index = self.dates, name = 'Close')

    def test_trueoutput(self):
        sharpe_answer = sharpe(self.input_true_df, 3)
        self.assertListEqual(list(sharpe_answer[~np.isnan(sharpe_answer)]), list(self.output_true_df[~np.isnan(self.output_true_df)]))
        self.assertEqual(len(sharpe_answer), len(self.output_true_df))
        self.assertEqual(self.output_true_df.name, sharpe_answer.name)

    def test_Negativevalue_exception(self):
        with self.assertRaises(Negativevalue):
            sharpe(self.input_negative, 3)


if __name__ == '__main__':
    unittest.main()

