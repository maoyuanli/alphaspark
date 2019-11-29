from utils.quandl_data_fetcher import QuandlDataFetcher

quandlDF = QuandlDataFetcher.fetch_data('EURONEXT/INGA')
print(quandlDF)