import statistics
import requests

stocksymbol = input('What Share Do You Want To Analyze? (Make Sure Stock Symbol Is In All Caps)')

stocksymbol = stocksymbol.upper()

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

# gets recommendations for stock
recs = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=' + stocksymbol + '&token=bto4nln48v6v7atimad0')

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

recommendations = recs.json()

# gets avgs of 'h'
currenth = currentinfo['h']
q1havg = statistics.mean(q1info['h'])
q2havg = statistics.mean(q2info['h'])
q3havg = statistics.mean(q3info['h'])
q4havg = statistics.mean(q4info['h'])

havg = (q1havg + q2havg + q3havg + q4havg) / 4

# gets avgs of 'l'
currentl = currentinfo['l']
q1lavg = statistics.mean(q1info['l'])
q2lavg = statistics.mean(q2info['l'])
q3lavg = statistics.mean(q3info['l'])
q4lavg = statistics.mean(q4info['l'])

lavg = (q1lavg + q2lavg + q3lavg + q4lavg) / 4

# gets actual and estimated revenues for each quarter
q1actual = q1earn['earningsCalendar'][0]['revenueActual']
q1estimate = q1earn['earningsCalendar'][0]['revenueEstimate']

q2actual = q2earn['earningsCalendar'][0]['revenueActual']
q2estimate = q2earn['earningsCalendar'][0]['revenueEstimate']

q3actual = q3earn['earningsCalendar'][0]['revenueActual']
q3estimate = q3earn['earningsCalendar'][0]['revenueEstimate']

q4actual = q4earn['earningsCalendar'][0]['revenueActual']
q4estimate = q4earn['earningsCalendar'][0]['revenueEstimate']

if q1actual > q1estimate:
    print(stocksymbol + ' did better than expected for q1')
elif q1actual < q1estimate:
    print(stocksymbol + ' did worse than expected for q1')
if q2actual > q2estimate:
    print(stocksymbol + ' did better than expected for q2')
elif q2actual < q2estimate:
    print(stocksymbol + ' did worse than expected for q2')
if q3actual > q3estimate:
    print(stocksymbol + ' did better than expected for q3')
elif q3actual < q3estimate:
    print(stocksymbol + ' did worse than expected for q3')
if q4actual > q4estimate:
    print(stocksymbol + ' did better than expected for q4')
elif q4actual < q4estimate:
    print(stocksymbol + ' did worse than expected for q4')
