import akshare as ak
import datetime

# get price
def Get_price(symbol, period, start_date=None, end_date=None, adjust="", count=None):
    if not count is None:
        if start_date is None:
            end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
            start_date = end_date - datetime.timedelta(days=count)
            end_date = str(end_date.year) + str(end_date.month).zfill(2) + str(end_date.day).zfill(2)
            start_date = str(start_date.year) + str(start_date.month).zfill(2) + str(start_date.day).zfill(2)

        elif end_date is None:
            start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
            end_date = start_date + datetime.timedelta(days=count)
            end_date = str(end_date.year) + str(end_date.month).zfill(2) + str(end_date.day).zfill(2)
            start_date = str(start_date.year) + str(start_date.month).zfill(2) + str(start_date.day).zfill(2)

        df = ak.stock_zh_a_hist(symbol=symbol, period=period, start_date=start_date, end_date=end_date, adjust="")

    else:
        df = ak.stock_zh_a_hist(symbol=symbol, period=period, start_date=start_date, end_date=end_date, adjust="")
    return df

df = Get_price(symbol="000001", period="weekly", end_date='20210222', adjust="", count=100)
print(df)