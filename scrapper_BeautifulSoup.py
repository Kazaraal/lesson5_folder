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
# Import requests
import requests
# Import csv
import csv

def scrapper_BeautifulSoup():
    website_to_scrape = "https://quotes.toscrape.com/"
    page_to_scrape = requests.get(website_to_scrape)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    qoutes = soup.find_all("span", attrs={"class":"text"})
    authors = soup.find_all("small", attrs={"class","author"})
    
    file = open("scrapped_quotes.csv", "w")
    writer = csv.writer(file)

    writer.writerow(["QUOTES", "AUTHORS"])

    for quote, author in zip(qoutes, authors):
        print(quote.text + "." + author.text)
        writer.writerow([quote.text, author.text])
    file.close()

scrapper_BeautifulSoup()