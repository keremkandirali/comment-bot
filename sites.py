sites = [
    {
        'url': 'https://www.site1.com/',  # URL of the blog posts.
        'link_selector': 'h2.post-title a',  # Link selector of the first post in the loop. e.g. <h2 class="post-title"><a href="#">The Post</a></h2>
        'title_selector': 'h1.post-title',  # Title selector of the selected post. e.g. <h1 class="post-title">The Post</h1>
        'author_selector': 'cite.fn a',  # Author name selector of the comments section. e.g. <cite class="fn"><a href="#">The Author</a></cite>
        'submit_selector': 'submit',  # Submit button selector (id) of the comments section. e.g. <input type="submit" id="submit">Submit</input>
    },
    {
        'url': 'https://www.site2.com/',
        'link_selector': 'h2.entry-title a',
        'title_selector': 'h1.entry-title',
        'author_selector': 'cite.comment-author a span',
        'submit_selector': 'submit',
    },
    {
        'url': 'https://www.site3.com/',
        'link_selector': '.archive-article a',
        'title_selector': 'h1.article-title',
        'author_selector': 'cite.fn a',
        'submit_selector': 'submit',
    },
]
