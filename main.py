import bs4
import requests
import fake_headers
KEYWORD = ['дизайн', 'фото', 'web', 'Python']
URL = 'https://habr.com/ru/all/'
HEADERS = fake_headers.Headers(browser='chrome', os='win', headers=True).generate()

respons = requests.get(URL, headers=HEADERS)

text = respons.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articl = soup.find_all('article')
for art in articl:
    hubs = art.find_all(class_="tm-article-snippet tm-article-snippet")
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        if set(hub.split(' ')) & set(KEYWORD):
            href = art.find(class_="tm-article-snippet__title-link").attrs["href"]
            title = art.find("h2").find("span").text
            date_ = art.find(class_="tm-article-snippet__datetime-published").text
            result = f'{date_} {title} ==> {URL}{href}'
            print(result)