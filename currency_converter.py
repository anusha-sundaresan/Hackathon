#this is a code created with the help of copilot to convert currency from one to another

import requests
from bs4 import BeautifulSoup

def currency_converter(amount, from_currency, to_currency):
    url = 'https://www.x-rates.com/calculator/?from={}&to={}&amount={}'.format(from_currency, to_currency, amount)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find('span', {'class': 'ccOutputTrail'}).text
    return result

def main():
    # amount = float(input("Enter amount: "))
    # from_currency = input("Enter from currency: ")
    # to_currency = input("Enter to currency: ")
    # result = currency_converter(amount, from_currency, to_currency)
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("Enter from currency: ")
        to_currency = input("Enter to currency: ")
        result = currency_converter(amount, from_currency, to_currency)
        print("Converted amount: {}".format(result))
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    except requests.exceptions.RequestException:
        print("An error occurred while making the request. Please try again later.")