from bs4 import BeautifulSoup
import requests

url = 'http://gorillavsbear.net'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

links_to_follow = []
video_urls = []

articles = soup.find('section', class_="blogroll")
articles = articles.find_all('p', class_="more_act")

for article in articles:
    link = article.find('a')
    links_to_follow.append(link.get('href'))

for link in links_to_follow:
    url = link
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    iframes = soup.find_all('iframe')

    for iframe in iframes:
        if 'youtube.com' in iframe['src']:
            video_urls.append(iframe['src'])

print(video_urls)
