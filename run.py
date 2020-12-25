import json
import requests
from bs4 import BeautifulSoup
# from requests import Session

session = requests.Session()


def login():
    print('login...')
    datas = {
        'username': 'user',
        'password': 'user12345'
    }

    res = session.post('http://127.0.0.1:5000/login', data=datas)
    soup = BeautifulSoup(res.text, 'html.parser')
    page_item = soup.find_all('li', attrs={'class': 'page-item'})
    total_pages = len(page_item) - 2
    return total_pages


def get_urls(page):
    print('getting urls... page {}'.format(page))
    params = {
        'page': page
    }
    res = session.get('http://127.0.0.1:5000', params=params)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.find_all('h4', attrs={'class': 'card-title'})
    urls = []
    for title in titles:
        url = title.find('a')['href']
        urls.append(url)
    return urls


def get_detail():
    print('getting detail...')
    # res = session.get(url)
    # f = open('./res.html', 'w+')
    # f.write(res.text)
    # f.close()


def create_csv():
    print('csv generated...')


def run():
    total_pages = login()

    total_urls = []
    for i in range(total_pages):
        page = i + 1
        urls = get_urls(page)
        total_urls += urls  # total_urls = total_urls + urls

    with open('all_urls.json', 'w') as outfile:
        json.dump(total_urls, outfile)


    get_detail()

    create_csv()


if __name__ == '__main__':
    run()
