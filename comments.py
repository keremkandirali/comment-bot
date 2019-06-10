import random

author_name = 'WPSelected'
author_email = 'wpselected@gmail.com'
author_website = 'https://www.wpselected.com'

comments = [
    'Your article touches some important points. It was really helpful for my research. Thanks.',
    'Explanatory, compact and reader-friendly. You made a good job with this post, thanks for sharing!',
    'Generally speaking, I think there is a big need for this kind of useful articles. Thank you!',
    'Great timing :) I was just looking for additional information about this.',
    'I wish to see more blog posts in this clear and informative style.',
    'This is a "must read" article! Already read more than once. Thanks a lot.',
    'It\'s enlightening for the ones who wonder about this topic. Congrats!',
]


def random_comment():
    return comments[random.randrange(len(comments))]

