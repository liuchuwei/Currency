from jqdatasdk import *

# Authentication
auth('13600081563','Liuchuwei1357')

df=get_price('000001.XSHE',count=2,end_date='2023-01-31',frequency='daily',
                   fields=['open', 'close'],panel = False)
print(df)