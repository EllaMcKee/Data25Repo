import requests
from pprint import pprint

# Scrape data from bbc website
requests_bbc = requests.get("https://www.bbc.co.uk/")

pprint(requests_bbc.content)