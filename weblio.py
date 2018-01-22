#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

URL = 'https://ejje.weblio.jp/content/'


def search(word):
    r = requests.get(URL + word)
    soup = BeautifulSoup(r.text, 'html.parser')
    meanings = soup.find('td', class_='content-explanation')
    print(meanings.text)


def main():
    argv = sys.argv
    word = argv[1]
    if word == '':
        print('Enter the word.')
    else:
        search(word)


if __name__ == '__main__':
    main()
