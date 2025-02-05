import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    return requests.get(url=url, headers=header).text

def parser_html(response):
    soup = BeautifulSoup(response, 'html.parser')
    li_list = soup.select('ol.grid_view li')
    info = []
    for li in li_list:
        num = li.select('div.pic em')[0].string
        title = li.select('span')[0].string
        tpe = li.select('div.bd p')[0].get_text().replace('\n', '').replace(' ', '').split('/')[-1].strip()
        score = li.select('span.rating_num')[0].string
        comment_num = li.select('div.star span')[3].string

        info.append({'movie_num':num,'movie_name':title,'movie_type':tpe,'movie_score':score,'movie_comment':comment_num})

    with open('movie.csv', 'a+', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['movie_num', 'movie_name', 'movie_type','movie_score', 'movie_comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell()==0:
            writer.writeheader()
        writer.writerows(info)


if __name__ == '__main__':
    url_list = [f"https://movie.douban.com/top250?start={i}&filter=" for i in range(0, 251, 25)]
    for page_url in url_list:
        parser_html(get_html(page_url))