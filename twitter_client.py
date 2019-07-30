import twitter
import csv

g = open('movies_with_twitter.csv', 'w')
fieldnames = ['title', 'keyword', 'gross', 'budget', 'release_date', 'twitter_buzz']
writer = csv.DictWriter(g, fieldnames=fieldnames)

f = open('improved_import_movies.csv')
reader = csv.DictReader(f)
idx = 0
sys.stdout.write("[")
sys.stdout.flush()
for row in reader:
    tile, release_date = row['title'], row['release_date']
    twitter_buzz = len(twitter.get_tweets(twitter.make_movie_rule(title, release_date)))
    writer.writerow({
        'title': row['title'],
        'keyword': row['keyword'],
        'gross': gross,
        'budget': budget,
        'release_date': release_date,
        'twitter_buzz': twitter_buzz
        })
    idx += 1
    if idx % 16 == 0:
        sys.stdout.write("=", end="")
        sys.stdout.flush()

   
sys.stdout.write("]")
sys.stdout.flush()
