# -*- coding: utf-8 -*-
from stock_info import StockCodeInfo

# Get Stock information
# stockInfo = StockCodeInfo()
# df = stockInfo.intergrate()

# Get Stock Price
# History
import akshare as ak
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="")

# Current
