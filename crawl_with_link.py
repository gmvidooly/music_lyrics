import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def crawl_it(slink):
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    data = requests.get(slink, headers=header)

    bsoup = BeautifulSoup(data.text, "html.parser")
    lyrics = str(bsoup)
    # print(lyrics)
    up_partition = '<!-- Usage of azlyrics.com content by any ' \
                   'third-party lyrics provider is prohibited by our ' \
                   'licensing agreement. Sorry about that. -->'
    down_partition = '<!-- MxM banner -->'
    lyrics = lyrics.split(up_partition)[1]
    lyrics = lyrics.split(down_partition)[0]
    p = re.compile(r'<.*?>')

    l1 = p.sub('', lyrics)
    return l1
