import pandas as pd
import pandas_datareader as web

counters = {counter: web.get_data_yahoo(counter) for counter in [
    'VTI',
    'VGT',
    ]}


last_prices = {counter: round(counters[counter]['Close'][-1], 2) for counter in counters}
df = pd.DataFrame.from_dict(last_prices, orient = 'index')
df.columns = ['Last Price']
my_prices = {}

with pd.ExcelWriter('Demo_tracker.xlsx', engine = 'xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='data')
    writer.save()
