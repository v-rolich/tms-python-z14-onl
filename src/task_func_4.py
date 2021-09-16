from datetime import datetime


def validate_pages(pages):
    if not isinstance(pages, int):
        raise TypeError
    elif pages < 1:
        raise ValueError


def validate_year(year):
    if not isinstance(year, int):
        raise TypeError
    elif year > datetime.now().year:
        raise ValueError


def validate_author(author):
    if not isinstance(author, str):
        raise TypeError
    elif not author:
        raise ValueError


def validate_price(price):
    if not (isinstance(price, (int, float))):
        raise TypeError
    elif price < 0:
        raise ValueError
