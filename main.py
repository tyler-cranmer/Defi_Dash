from bs4 import BeautifulSoup
import requests
import csv

coin_name = 'Terra(Luna)'
source = requests.get('https://www.coingecko.com/en/coins/terra-luna/historical_data/usd?end_date=2021-10-15&start_date=2020-10-15#panel').text

soup = BeautifulSoup(source, 'lxml')

table= soup.find('tbody')
data_objects = table.find_all('tr')
# first_row = data_objects[0]
# fin_data = first_row.find_all('td', class_='text-center')

coin_name = ['Terra(Luna)','Uniswap', 'ChainLink', 'Dai', 'cEth', 'Lido Staked Ether (STETH)', 'PancakeSwap (CAKE)', 'cDAI (CDAI)', 'The Graph (GRT)', 
'Aave (AAVE)', 'cUSDC (CUSDC)', 'Olympus (OHM)', 'Amp (AMP)', 'Maker (MKR)', 'Sushi (SUSHI)']
coin_links = ['https://www.coingecko.com/en/coins/terra-luna/historical_data/usd?end_date=2021-10-15&start_date=2020-10-15#panel',
'https://www.coingecko.com/en/coins/uniswap/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel', 
'https://www.coingecko.com/en/coins/chainlink/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/dai/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/compound-ether/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/lido-staked-ether/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/pancakeswap/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/compound-dai/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel', 
'https://www.coingecko.com/en/coins/the-graph/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/aave/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/compound-usd-coin/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/olympus/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/amp/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel', 
'https://www.coingecko.com/en/coins/maker/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/sushi/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel'
]


def remove(string):
    return "".join(string.split())

def  to_num(string):
    no_space = "".join(string.split())
    no_dolla = no_space.replace('$', '')
    return float(no_dolla)


# csv_file = open(f'{coin_name}.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Date', 'Market Cap', 'Volume', 'Open', 'Close'])


for container in range(len(data_objects)):

    first_row = data_objects[container]
    fin_data = first_row.find_all('td', class_='text-center')

    date = remove(first_row.th.text)
    market_cap = remove(fin_data[0].text)
    volume = remove(fin_data[1].text)
    open_price = remove(fin_data[2].text)
    close_pice = remove(fin_data[3].text)

    # dates.append(date)
    # market_caps.append(market_cap)
    # volumes.append(volume)
    # open_prices.append(open_price)
    # close_prices.append(close_pice)
    # csv_writer.writerow([date, market_cap, volume, open_price, close_pice])
    print(type(close_pice))

csv_file.close()





