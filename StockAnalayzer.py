import statistics
import requests

stocksymbol = input('What Share Do You Want To Analyze? (Make Sure Stock Symbol Is In All Caps)')

# gets all current stock info as of last posted values
current = requests.get('https://finnhub.io/api/v1/quote?symbol=' + stocksymbol + '&token=bto4nln48v6v7atimad0')

# gets all stock info for q1 of 2020
q1i = requests.get(
    'https://finnhub.io/api/v1/stock/candle?symbol=' + stocksymbol + '&resolution=1&from=1577836800&to=1585612800&token=bto4nln48v6v7atimad0')

# gets all stock info for q2 of 2020
q2i = requests.get(
    'https://finnhub.io/api/v1/stock/candle?symbol=' + stocksymbol + '&resolution=1&from=1585699200&to=1593475200&token=bto4nln48v6v7atimad0')

# gets all stock info for q3 of 2020
q3i = requests.get(
    'https://finnhub.io/api/v1/stock/candle?symbol=' + stocksymbol + '&resolution=1&from=1593561600&to=1601424000&token=bto4nln48v6v7atimad0')

# gets all stock info for q4 of 2020
q4i = requests.get(
    'https://finnhub.io/api/v1/stock/candle?symbol=' + stocksymbol + '&resolution=1&from=1601510400&to=1609372800&token=bto4nln48v6v7atimad0')

# gets earnings for q1
q1e = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2020-01-01&to=2020-03-31&symbol=' + stocksymbol + '&token=bto4nln48v6v7atimad0')

# gets earnings for q2
q2e = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2020-04-01&to=2020-06-30&symbol=' + stocksymbol + '&token=bto4nln48v6v7atimad0')

# gets earnings for q3
q3e = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2020-07-01&to=2020-09-30&symbol=' + stocksymbol + '&token=bto4nln48v6v7atimad0')

# gets earnings for q4
q4e = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2020-10-01&to=2020-12-31&symbol=' + stocksymbol + '&token=bto4nln48v6v7atimad0')

# converts all request into readable information
currentinfo = current.json()
q1info = q1i.json()
q2info = q2i.json()
q3info = q3i.json()
q4info = q4i.json()

q1earn = q1e.json()
q2earn = q2e.json()
q3earn = q3e.json()
q4earn = q4e.json()



# gets avgs of 'c'
currentc = currentinfo['c']
q1cavg = statistics.mean(q1info['c'])
q2cavg = statistics.mean(q2info['c'])

q1actual = q1earn['earningsCalendar']
q1a = q1actual[0]
q1aa = q1a['revenueActual']

print(q1aa)


