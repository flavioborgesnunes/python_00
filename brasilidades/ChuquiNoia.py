#!/usr/bin/python3
import requests
from googletrans import Translator

r = requests.get(f'https://api.chucknorris.io/jokes/random').json()

print(Translator().translate(r['value'], src='en', dest='pt').text)




