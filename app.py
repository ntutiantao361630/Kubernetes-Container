from urllib.request import urlopen as Ureq

from bs4 import BeautifulSoup as soup

import datetime

# import sys

import re





def striphtml(data):

    p = re.compile(r'<.*?>')

    return p.sub('', data)





my_url = "https://store.steampowered.com/search/?specials=1"

uClient = Ureq(my_url)

page_html = uClient.read()

uClient.close



page_soup = soup(page_html, 'html.parser')

games = page_soup.find_all("span", {"class": "title"})



games_titles = list()

for n in games:

    n = str(n)

    title = striphtml(n)

    games_titles.append(title)



now = datetime.datetime.now()

file_name = now.strftime("%m.%d.%Y_%H.%M.%S")

write_file = open(file_name+".txt", "w", encoding='UTF-8')

for item in games_titles:

    write_file.write("%s\n" % item)

write_file.close()
