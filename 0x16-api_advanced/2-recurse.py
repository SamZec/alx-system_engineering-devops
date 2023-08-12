#!/usr/bin/python3
"""a script that get titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    para = {'after': after, 'count': count, 'limit': 100}
    headers = {'user-agent': 'my-app/0.0.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    r = requests.get(url, headers=headers, params=para, allow_redirects=False)
    r_json = r.json()
    if r.status_code == 404:
        return None

    result = r_json.get('data')
    after = result.get('after')
    count += result.get('dist')

    for item in result.get('children'):
        hot_list.append(item.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list


if __name__ == '__main__':
    recurse()
