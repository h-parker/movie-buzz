import searchtweets
import datetime

premium_search_args = searchtweets.load_credentials('twitter.yaml')

def make_movie_rule(title, release_date):
    """title, release_date"""
    year, month, day = map(int, release_date.split('-'))
    release_date = datetime.datetime(year, month, day)
    date_from = release_date - datetime.timedelta(weeks=2)
    date_to = release_date + datetime.timedelta(weeks=2)
    return searchtweets.gen_rule_payload(title, from_date=date_from.strftime("%Y-%m-%d"), to_date=date_to.strftime("%Y-%m-%d"))

def get_tweets(rule):
    """rule, search_args"""
    return searchtweets.collect_results(rule, result_stream_args=premium_search_args)

def get_result_stream(rule):
    return searchtweets.ResultStream(rule=rule, max_results=500, max_pages
