import requests
import bs4
from fake_useragent import UserAgent
import re


def get_raw_html(url: str) -> str:
    headers = {
        'User-Agent': UserAgent().random
    }
    request_data = requests.get(url, headers=headers)
    return request_data.text


def get_parsed_data(url: str) -> dict:
    data = get_raw_html(url)
    return parse_html(data)


def search_for_class(bs_tree, classname: str) -> list:
    class_list = []
    for tag in bs_tree.find_all(class_=re.compile(classname)):
        if tag.text != '':
            class_list.append(tag.text.replace('\n', ''))
    return class_list


def parse_html(raw_html: str) -> dict:
    bs = bs4.BeautifulSoup(raw_html, 'html.parser')
    prices_list, products = [], []

    products = search_for_class(bs, r'name')
    prices_list = search_for_class(bs, r'price')

    return dict(zip(products, prices_list))
