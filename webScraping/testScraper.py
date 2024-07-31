from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://edhrec.com/commanders/gyrus-waker-of-corpses")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")
names = soup.findAll("span", attrs={"class":"Card_name__Mpa7S"})

for name in names:
    print(name.text)