import requests
from bs4 import BeautifulSoup
from requests import Session

session = requests.Session()

def login():
    print('login...')
    datas = {
        'username': 'user',
        'password': 'user12345'
    }

    res = Session.post('http://127.0.0.1:5000/login', data=datas)

    f = open('./res.html', 'w+')
    f.write(res.text)
    f.close()

    soup = BeautifulSoup(res.text, 'html5lib')

    page_item = soup.find_all('li', attrs={'class': 'page-item'})
    print_pages = len(page_item) - 2
    return total_pages

def get_urls():
    print('getting urls...')

def get_detail():
    print('getting detail...')

def create_csv():
    print('csv generated...')

def run():
    login()
    get_urls()
    get_detail()
    create_csv()

if __name__ == '__main__':
    run()
