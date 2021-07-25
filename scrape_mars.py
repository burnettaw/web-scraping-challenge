#!/usr/bin/env python
# coding: utf-8

import pandas as pd

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
def scrape_info():
     # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)


    mars = {}


    # ### NASA MARS NEWS
    # ### Scrape the Mars News Site and collect the latest News Title and Paragraph Text. 
    # Assign the text to variables.
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.find_all('div', class_='content_title')
    results = quotes[0]
    mars["newstitle"] = results.text

    paragraph = soup.find_all('div', class_='article_teaser_body')
    paragraph=paragraph[0].text
    paragraph
    mars["paragraph"] = paragraph
    mars


    # ### JPL Mars Space Images - Featured Image
    # ### Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.find('img', class_='fancybox-image').get('src')
    quotes2 = "https://spaceimages-mars.com/"+quotes
    mars['featured_image_url'] = quotes2
    mars

    # ### Mars Facts
    # ### Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, 
    # ### Mass, etc. Use Pandas to convert the data to a HTML table string.
    url2= 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url2)
    df = tables[0]
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    df
    mars['facts']=df.to_html()
    mars


    # ### Mars Hemisphere
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    hemisphere_image_urls = []
    for i in range(4):
        browser.find_by_css("a.product-item h3")[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find("h2", class_ = "title").get_text()
        element = soup.find("a", text = "Sample").get("href")
        hemispheres = {}
        hemispheres["img_url"] = url+element
        hemispheres["title"] = title
        hemisphere_image_urls.append(hemispheres)
        browser.back()

    mars["hemispheres"] = hemisphere_image_urls
    return mars

if __name__ == "__main__":
    print(scrape_info())
