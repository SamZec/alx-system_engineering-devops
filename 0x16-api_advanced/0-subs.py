#!/usr/bin/python3
"""a script for getting subreddit  subscribers"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers  for a given subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/about/.json'
    headers = {'user-agent': 'my-app/0.0.0'}
    total_subscribers = 0

    r = requests.get(url, headers=headers, allow_redirects=False)
    r_json = r.json()
    if r.status_code == 404:
        return total_subscribers
    else:
        total_subscribers = r_json.get('data').get('subscribers')
        return total_subscribers


if __name__ == '__main__':
    number_of_subscribers(subreddit=None)
