############################################################
############################################################
# scrapper_BeautifulSoup
############################################################
# This scraps the provided website and brings back requested
# results
############################################################
############################################################
# # Install bs4 (pip install bs4)
# Install requests (pip install requests)
# Import BeautifulSoup
from bs4 import BeautifulSoup
import requests

def scrapper_BeautifulSoup():
    website_to_scrape = "https://quotes.toscrape.com/"
    page_to_scrape = requests.get(website_to_scrape)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    qoutes = soup.find_all("span", attrs={"class":"text"})
    authors = soup.find_all("small", attrs={"class","author"})
    
    for quote, author in zip(qoutes, authors):
        print(quote.text + "." + author.text)

scrapper_BeautifulSoup()