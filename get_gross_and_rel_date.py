import requests
import urllib
from bs4 import BeautifulSoup


def get_data(title):
    search_stem = 'https://boxofficemojo.com/search/?q=' 
    movie_stem =  'https://boxofficemojo.com'
    url_encoded_title = urllib.parse.quote_plus(title)
    response = requests.get(search_stem + url_encoded_title)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_title_link = soup.find('a', text=title)
    response = requests.get(movie_stem + movie_title_link['href'])
    movie_page = BeautifulSoup(response.text, 'html.parser')
    rows = movie_page.find_all('table')[3].find_all('tr')
    bolds = []
    for row in rows:
        bolds.extend(row.find_all('b'))
    print(bolds[1].text, bolds[3].text)

#    row = movie_title_link.parent.parent.parent.parent
#    columns = row.find_all('td')
#    print(columns[0].text, columns[2].text, columns[6].text)


