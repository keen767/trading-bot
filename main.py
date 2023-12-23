from datetime import date, timedelta
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt

c = CurrencyRates()
#print(c.get_rates('USD'))   # you can directly call get_rates('USD')

def forex_graph(currency1, currency2):
    forex = []
    for delta_days in range(30):
        day = date.today() - timedelta(days=delta_days)
        exchrate = c.get_rate(currency1, currency2, day)
        forex.append(exchrate)
    return forex

def plot(data):
    plt.plot(data)
    plt.show()

forex = forex_graph('USD','SGD')
plot(forex)