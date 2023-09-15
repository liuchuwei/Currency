import akshare as ak
import datetime
from dateutil.relativedelta import relativedelta
# History
def GetPriceHist(symbol="000001", period="daily", start_date=None, end_date=None,
             adjust="", count=None):
    """
    :param symbol: 股票代码
    :param period: 时间间隔:daily, weekly, monthly
    :param start_date: 开始查询的日期
    :param end_date: 结束查询的日期
    :param adjust: 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据
    :param count: 返回多少条数据
    :return:历史行情
    """

    if period in ["daily", "weekly", "monthly"]:
        if not count is None:
            if start_date is None:
                end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
                if period == "daily":
                    start_date = end_date - relativedelta(days=count)
                elif period == "weekly":
                    start_date = end_date - relativedelta(weeks=count)
                elif period == "monthly":
                    start_date = end_date - relativedelta(months=count)

                end_date = str(end_date.year) + str(end_date.month).zfill(2) + str(end_date.day).zfill(2)
                start_date = str(start_date.year) + str(start_date.month).zfill(2) + str(start_date.day).zfill(2)

            elif end_date is None:
                start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
                if period == "daily":
                    end_date = start_date - relativedelta(days=count)
                elif period == "weekly":
                    end_date = start_date - relativedelta(weeks=count)
                elif period == "monthly":
                    end_date = start_date - relativedelta(months=count)

                end_date = str(end_date.year) + str(end_date.month).zfill(2) + str(end_date.day).zfill(2)
                start_date = str(start_date.year) + str(start_date.month).zfill(2) + str(start_date.day).zfill(2)

        df = ak.stock_zh_a_hist(symbol=symbol, period=period, start_date=start_date, end_date=end_date,
                                                adjust=adjust)

    elif period in ['1', '5', '15', '30', '60']:
        if not count is None:
            if start_date is None:
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
                start_date = end_date - relativedelta(minutes=count*int(period))
                end_date =  str(end_date.year) + "-" + str(end_date.month).zfill(2) + "-" + str(end_date.day).zfill(2) \
                             + " " + str(end_date.hour).zfill(2) + ":" + str(end_date.minute).zfill(2) + ":" + str(end_date.second).zfill(2)
                start_date = str(start_date.year) + "-" + str(start_date.month).zfill(2) + "-" + str(start_date.day).zfill(2) \
                             + " " + str(start_date.hour).zfill(2) + ":" + str(start_date.minute).zfill(2) + ":" + str(start_date.second).zfill(2)

            elif end_date is None:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
                end_date = start_date - relativedelta(minutes=count*int(period))
                end_date =  str(end_date.year) + "-" + str(end_date.month).zfill(2) + "-" + str(end_date.day).zfill(2) \
                             + " " + str(end_date.hour).zfill(2) + ":" + str(end_date.minute).zfill(2) + ":" + str(end_date.second).zfill(2)
                start_date = str(start_date.year) + "-" + str(start_date.month).zfill(2) + "-" + str(start_date.day).zfill(2) \
                             + " " + str(start_date.hour).zfill(2) + ":" + str(start_date.minute).zfill(2) + ":" + str(start_date.second).zfill(2)

        df = ak.stock_zh_a_hist_min_em(symbol=symbol, start_date=start_date,
                                                              end_date=end_date, period=period, adjust=adjust)
        # df = ak.stock_zh_a_hist_min_em(symbol=symbol, start_date="2021-09-01 09:32:00",
        #                                                       end_date="2021-09-06 09:32:00", period=period, adjust=adjust)

    return df
