import requests
from bs4 import BeautifulSoup

# Collect and parse page
page = requests.get('http://smacie.com/randomizer/simpsons/homer.html')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull the text from the Big tag
result = soup.find('big').text

print(result)
