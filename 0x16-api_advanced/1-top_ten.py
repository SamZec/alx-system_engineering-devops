#!/usr/bin/python3
"""a script for getting top ten hot posts of a subreddit"""

import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/' + subreddit
    para = '/hot.json?q=top&limit=10'
    headers = {'user-agent': 'my-app/0.0.0'}

    r = requests.get(url + para, headers=headers, allow_redirects=False)
    r_json = r.json()
    if r.status_code != 404:
        top_post_children = r_json.get('data').get('children')
        for item in top_post_children:
            print(item.get('data').get('title'))
    else:
        print(None)


if __name__ == '__main__':
    top_ten(subreddit=None)
