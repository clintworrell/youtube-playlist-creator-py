from bs4 import BeautifulSoup
import requests


def get_html():
    url = 'http://gorillavsbear.net'
    req = requests.get(url)
    html_doc = req.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup


def scrape_html(soup):
    links_to_follow = []
    video_urls = []

    articles = soup.find('section', class_="blogroll")
    articles = articles.find_all('p', class_="more_act")

    for article in articles:
        link = article.find('a')
        links_to_follow.append(link.get('href'))

    for link in links_to_follow:
        url = link
        req = requests.get(url)
        html_doc = req.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        iframes = soup.find_all('iframe')

        for iframe in iframes:
            if 'youtube.com' in iframe['src']:
                video_urls.append(iframe['src'])

    return video_urls


def main():
    soup = get_html()
    video_urls = scrape_html(soup)
    print(video_urls)


if __name__ == "__main__":
    main()
