from price import GetPriceHist

# Get Stock Price
df = GetPriceHist(symbol="000001", period="1", end_date="2023-09-15 13:45:00", adjust="", count=8)
