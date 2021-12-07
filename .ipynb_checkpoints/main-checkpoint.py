from bs4 import BeautifulSoup
import requests
import csv
import time


coin_name = [
'Terra(Luna)','Uniswap', 'ChainLink', 'Dai', 'cEth', 'Lido Staked Ether (STETH)', 'PancakeSwap (CAKE)', 'cDAI (CDAI)', 'The Graph (GRT)', 
'Aave (AAVE)', 'cUSDC (CUSDC)', 'Olympus (OHM)', 'Amp (AMP)', 'Maker (MKR)', 'Sushi (SUSHI)', 'Compound (COMP)', 'Synthetix Network Token (SNX)', 
'Magic Internet Money (MIM)','dYdX (DYDX)', 'yearn.finance (YFI)','Curve DAO Token (CRV)', 'renBTC (RENBTC)', 'Spell Token (SPELL)', 'REN (REN)',
'Nexus Mutual (NXM)',
 'Perpetual Protocol (PERP)', 'Serum (SRM)', 'Bancor Network Token (BNT)', 'xSUSHI (XSUSHI)', '0x (ZRX)', 'Raydium (RAY)', 'UMA (UMA)', 
'Coin98 (C98)', 
'Wonderland (TIME)', 'Liquity USD (LUSD)', '1inch (1INCH)', 'Neutrino USD (USDN)', 'Loopring (LRC', 'Fei Protocol (FEI)', 'Kava (KAVA)', 'Rocket Pool (RPL)',
'Gnosis (GNO)', 
'Reserve Rights Token (RSR)', 'Alpha Finance (ALPHA)', 'Frax (FRAX)', 'Convex Finance (CVX)', 'Rari Governance Token (RGT)', 'Keep Network (KEEP)', 'sETH (SETH)', 'Injective Protocol (INJ)']

coin_abv = [
'Luna','Uniswap', 'ChainLink', 'Dai', 'cEth', 'STETH', 'CAKE', 'CDAI', 'GRT', 
'AAVE', 'CUSDC', 'OHM', 'AMP', 'MKR', 'SUSHI', 'COMP', 'SNX', 
'MIM','DYDX', 'YFI','CRV', 'RENBTC', 'SPELL', 'REN',
'NXM',
'PERP', 'SRM', 'BNT', 'XSUSHI', 'ZRX', 'RAY', 'UMA', 
'C98',
'TIME', 'LUSD', '1INCH', 'USDN', 'LRC', 'FEI', 'KAVA', 'RPL',
'GNO',
 'RSR', 'ALPHA', 'FRAX', 'CVX', 'RGT', 'KEEP', 'SETH', 'INJ']


coin_links = [
'https://www.coingecko.com/en/coins/terra-luna/historical_data/usd?end_date=2021-10-15&start_date=2020-10-15#panel',
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
'https://www.coingecko.com/en/coins/sushi/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/compound/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/synthetix-network-token/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/magic-internet-money/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/dydx/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/yearn-finance/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/curve-dao-token/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/renbtc/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/spell-token/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/ren/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/nexus-mutual/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/perpetual-protocol/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/serum/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/bancor-network/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/xsushi/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/0x/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/raydium/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/uma/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/coin98/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/wonderland/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/liquity-usd/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/1inch/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/neutrino-usd/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/loopring/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/fei-protocol/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/kava/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/rocket-pool/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/gnosis/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/reserve-rights-token/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/alpha-finance/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/frax/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/convex-finance/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/rari-governance-token/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/keep-network/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/seth/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel',
'https://www.coingecko.com/en/coins/injective-protocol/historical_data/usd?end_date=2021-10-16&start_date=2020-10-16#panel']



def remove(string):
    return "".join(string.split())

def  to_num(string):
    no_space = "".join(string.split())
    if no_space =='N/A':
        return no_space
    else:
        no_space = "".join(string.split())
        no_dolla = no_space.replace('$', '')
        no_comma = no_dolla.replace(',', '')
    return float(no_comma)

def create(name, url, abv):

    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')

    table= soup.find('tbody')
    data_objects = table.find_all('tr')

    csv_file = open(f'{name}.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Symbol','Date', 'Market Cap', 'Volume', 'Open', 'Close'])


    for container in range(len(data_objects)):

        first_row = data_objects[container]
        fin_data = first_row.find_all('td', class_='text-center')

        date = remove(first_row.th.text)
        market_cap = to_num(fin_data[0].text)
        volume = to_num(fin_data[1].text)
        open_price = to_num(fin_data[2].text)
        close_pice = to_num(fin_data[3].text)
        coin_abv = abv

        csv_writer.writerow([coin_abv, date, market_cap, volume, open_price, close_pice])

    csv_file.close()
    print(name)

    return 0

if __name__ == '__main__':

    if len(coin_name) == len(coin_links) and len(coin_name) == len(coin_abv):
        for i in range(len(coin_name)):
            create(coin_name[i], coin_links[i], coin_abv[i])
            time.sleep(2)
    else: 
        print('arrays dont match up')
