import requests
import urllib
from bs4 import BeautifulSoup
import csv
import sys
import time


def get_data(title):
    search_stem = 'https://boxofficemojo.com/search/?q=' 
    movie_stem =  'https://boxofficemojo.com'
    url_encoded_title = urllib.parse.quote_plus(title)
    s = requests.Session()
    response = s.get(search_stem + url_encoded_title)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_title_link = soup.find('a', text=title)
    try:
        response = s.get(movie_stem + movie_title_link['href'])
    except TypeError:
        return (False, False, False)
    movie_page = BeautifulSoup(response.text, 'html.parser')
    data_table = movie_page.find_all('table')[3]
    bold_tags = data_table.find_all('b')
    bold_texts = []
    bold_texts.extend(tag.text for tag in bold_tags)
    if 'Lifetime' in str(data_table):
        gross = bold_texts[1]
        release_date = bold_texts[4]
        budget = bold_texts[8]
    elif 'Gross' in str(data_table):
        gross = bold_texts[1]
        release_date = bold_texts[3]
        budget = bold_texts[7]
    else:
        return (False, False, False)
    return (gross, release_date, budget)

g = open('import_movies.csv', 'w')
fieldnames = ['title', 'keyword', 'gross', 'budget', 'release_date']
writer = csv.DictWriter(g, fieldnames=fieldnames)
writer.writeheader()

with open('no_tv_keywords.csv') as f:
    reader = csv.DictReader(f, delimiter=",", skipinitialspace=True)
    idx = 0
    print("[", end='')
    sys.stdout.flush()
    for row in reader:
        gross, release_date, budget = get_data(row['title'])
        time.sleep(1)
        if not gross or not budget:
            continue
        if budget =='N/A':
            continue
        writer.writerow({
            'title': row['title'],
            'keyword': row['keyword'],
            'gross': gross,
            'budget': budget,
            'release_date': release_date
            })
        idx += 1
        if idx % 36 == 0:
            sys.stdout.write('=')
            sys.stdout.flush()
    sys.stdout.write("]")
    sys.stdout.flush()
        
g.close()
