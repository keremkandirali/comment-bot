import random

author_name = 'YourName'
author_email = 'YourEmail@gmail.com'
author_website = 'https://www.YourSite.com'

comments = [
    'Your comment 1',
    'Your comment 2',
    'Your comment 3',
    'Your comment 4',
    'Your comment 5',
]


def random_comment():
    return comments[random.randrange(len(comments))]
