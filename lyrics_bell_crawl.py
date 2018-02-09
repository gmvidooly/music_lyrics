import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re


class LyricBell:
    def __init__(self):
        self.user_agent = UserAgent()
        self.header = {'User-Agent': str(self.user_agent.safari)}
        self.header1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}
        self.main_url = 'http://www.lyricsbell.com/?s={}'
        # self.main_url1 = 'https://www.lyricsmasti.com/search?type=song&q={}'
        self.main_uri0 = 'https://www.lyricsmasti.com{}'
        self.html_regex = re.compile(r'<.*?>')

    def get_lyrics(self, song_name):
        hit_req = None
        lyric_req = None
        arg_to_send = song_name.replace(' ', '+')
        res_href = {}
        song_name_to_search = song_name.replace(' ', '-').lower()
        pre_search = self.main_url.format(arg_to_send)
        print(pre_search)
        try:
            print('header', self.header)
            hit_req = requests.get(pre_search, params=self.header)
        except Exception as ex:
            print(ex.__str__())
            return hit_req
        print(hit_req.status_code)
        print(hit_req.headers)
        # print(hit_req.text)
        # soup = BeautifulSoup(hit_req.text, 'lxml')
        # anchors = soup.find_all('a', href=True)
        # # print(type(anchors), anchors)
        # print(song_name_to_search)
        # for a in anchors:
        #     if song_name_to_search in a['href'].strip().lower():
        #         if a['href'].strip() not in res_href:
        #             res_href['href'] = a['href'].strip()
        # print(res_href)
        # lyric_url = self.main_uri0.format(res_href['href'])
        # print(lyric_url)
        # try:
        #     lyric_req = requests.get(lyric_url, params=self.header)
        # except Exception as ex:
        #     print(ex.__str__())
        #     return lyric_req
        #
        # if lyric_req.status_code == 200:
        #     lyric_soup = BeautifulSoup(lyric_req.text, 'lxml')
        #     lyric_code = lyric_soup.find_all('code')
        #     # print(lyric_code)
        #     # print(len(lyric_code))
        #     lyrics_raw = lyric_code[0]
        #     # print(lyrics_raw)
        #     cleaned_lyrics = self.html_regex.sub('', str(lyrics_raw))
        #     print(cleaned_lyrics.strip())


if __name__ == "__main__":
    lyrics_obj = LyricBell()
    lyrics_obj.get_lyrics('qismat')
