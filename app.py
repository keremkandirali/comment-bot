import sites
import comments
from selenium import webdriver
import time

with open('commented.txt', 'r') as commented:
    post_titles = commented.read().splitlines()


def browse_sites():
    browser = webdriver.Chrome()

    for site in sites.sites:
        browser.get(site['url'])
        post_url = browser.find_element_by_css_selector(site['link_selector']).get_attribute('href')
        browser.get(post_url)
        post_title = browser.find_element_by_css_selector(site['title_selector']).text
        submit_button = browser.find_element_by_id(site['submit_selector'])
        author_names = browser.find_elements_by_css_selector(site['author_selector'])
        availability = True

        for author in author_names:
            if author.text.lower() == comments.author_name.lower():
                availability = False

        if post_title not in post_titles and availability:
            comment_fields = (
                browser.find_element_by_id('comment'),
                browser.find_element_by_id('author'),
                browser.find_element_by_id('email'),
                browser.find_element_by_id('url'),
            )

            comment_properties = (
                comments.random_comment(),
                comments.author_name,
                comments.author_email,
                comments.author_website,
            )

            post_comment(comment_fields, comment_properties, submit_button)
            with open('commented.txt', 'a') as add_commented:
                add_commented.write(post_title + '\n')
            post_titles.append(post_title)
            print('Commented on', post_url, comment_properties[0])
            time.sleep(3)
        else:
            print('Already commented on', post_url)


def post_comment(fields, properties, button):
    for field, prop in zip(fields, properties):
        field.clear()
        field.send_keys(prop)
    button.click()


browse_sites()
print('Done.')
