import json
import sys
import pandas

# class for hosting configurations
class Configurations:
    inner = {}
    # read JSON configuration file to dictionary
    def __init__(self, filePathName):
        self.inner = json.load(open(filePathName))
    # return value for a given configuration key
    # 'overload' indexing operator
    def __getitem__(self, key):
        return self.inner[key.upper()]

# configuration file string is command line argument
configurationsFilePathName = sys.argv[1]

# create configurations object
config = Configurations(configurationsFilePathName)

# create market data based on configuration
market = pandas.read_csv(config['MarketData'])
print('2Y EUR swap rate:')
print(market.head())

# create fixings data based on configuration
fixings = pandas.read_csv(config['FixingsData'])
print('6M Euribor fixings:')
print(fixings.head())
