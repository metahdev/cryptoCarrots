import urllib
import requests
import json

CARROT_PRICE = 169

def get_value() -> float:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/usd")
    value = response.json()["bpi"]['USD']["rate_float"]
    answer = float(round(value, 2))
    return answer


def from_usd(value, currency) -> float:
    response = requests.get("https://api.exchangerate.host/convert?from=USD&to=" + str(currency)
                            + "&amount=" + str(value))
    answer = float(round(response.json()["result"], 2))
    return answer


print("Welcome to CryptoCarrot!"
      "\nAre you interested in cryptocurrency and vegetables? "
      "\n- Well, we've got you! This program gives out the bitcoin rate in kg of carrots"
      "(at the price of Kazakhstani carrots) \n")
      
print("Please write the number of bitcoins you would like to convert: ")

amount = input()

try:
   val = float(amount)
except ValueError:
   print("That's not an int!")


usd = get_value() * val
message = '\nBitcoin exchange rate at the moment is: '
kzt = from_usd(usd, 'KZT')
kg = round(kzt / CARROT_PRICE, 2)
print(message + str(kg) + "kg of carrots(calculated in Tenge)\n")
print("Thank you for using CryptoCarrot! Until next time! ")

