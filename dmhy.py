from typing import Optional
from requests import get
from lxml.etree import HTML
from chardet import detect
from opencc import OpenCC


c = OpenCC('t2s')


def get_homepage(page_number: int, keyword: Optional[str], simplified_chinese: Optional[bool]):
    url = 'http://dmhy.org/topics/list/page/' + str(page_number)
    if keyword is not None:
        url += '?keyword=' + keyword

    response = get(url)
    encoding = detect(response.content)['encoding']
    content = response.content.decode(encoding)

    html = HTML(content)

    page = []

    for item in html.xpath('//table[1]//tr[position() > 2]'):

        try:
            post_datetime = item.xpath('.//td[1]//span//text()')[0]
        except:
            post_datetime = ''

        try:
            sort_id = item.xpath('.//td[2]//a//@class')[0].strip().split('-')[1]
        except:
            sort_id = ''

        try:
            sort_name = item.xpath('.//td[2]//a//font//text()')[0].strip()
            if simplified_chinese:
                sort_name = c.convert(sort_name)
        except:
            sort_name = ''

        try:
            team_id = item.xpath('.//td[3]//span//a//@href')[0].strip().split('/')[4]
        except:
            team_id = ''

        try:
            team_name = item.xpath('.//td[3]//span/a//text()')[0].strip()
            if simplified_chinese:
                team_name = c.convert(team_name)
        except:
            team_name = ''

        try:
            title = ''.join(item.xpath('.//td[3]/a//text()')).strip()
            if simplified_chinese:
                title = c.convert(title)
        except:
            title = ''

        try:
            magnet = item.xpath('.//td[4]//a//@href')[0].strip()
        except:
            magnet = ''

        try:
            size = item.xpath('.//td[5]//text()')[0].strip()
        except:
            size = ''

        try:
            seeding_number = item.xpath('.//td[6]//text()')[0].strip()
        except:
            seeding_number = ''

        try:
            downloading_number = item.xpath('.//td[7]//text()')[0].strip()
        except:
            downloading_number = ''

        try:
            finished_number = item.xpath('.//td[8]//text()')[0].strip()
        except:
            finished_number = ''

        page.append({
            'post_datetime': post_datetime,
            'sort_id': sort_id,
            'sort_name': sort_name,
            'team_id': team_id,
            'team_name': team_name,
            'title': title,
            'magnet': magnet,
            'size': size,
            'seeding_number': seeding_number,
            'downloading_number': downloading_number,
            'finished_number': finished_number})
    return page
