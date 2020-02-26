import requests

def main():
    bitcoins = get_bitcoin_amount()
    usd = bitcoin_to_usd(bitcoins)
    message = ' bitcoins is equal to $'
    display_results(bitcoins, message, usd)

def get_bitcoin_amount():
    bitcoins = input('How many bitcoins do you have?')
    return bitcoins

def get_bitcoin_data():
    bitcoin_data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    return bitcoin_data

def bitcoin_to_usd(bitcoins):
    usd_rate = get_bitcoin_data()['bpi']['USD']['rate_float']
    usd = int(bitcoins) * usd_rate
    return usd

def display_results(currency1, message, currency2):
    print(str(currency1) + message + str(currency2))

if __name__ == '__main__':
    main()