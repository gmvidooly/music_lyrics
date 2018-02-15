import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import time

class LyricMasti:
    def __init__(self):
        self.user_agent = UserAgent()
        self.header = {'User-Agent': str('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')}
        self.main_url = 'http://www.songlyrics.com/index.php?section=search&searchW={}&submit=Search&searchIn1=artist&searchIn2=album&searchIn3=song&searchIn4=lyrics'
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
            hit_req = requests.get(pre_search, params=self.header)
        except Exception as ex:
            print(ex.__str__())
            return hit_req
        print(hit_req.status_code)
        soup = BeautifulSoup(hit_req.text, 'html.parser')
        anchors = soup.find_all("div", {"class" : 'serpresult'})
        # print(type(anchors), anchors)
        print(song_name_to_search)
        # print(anchors)
        for a in anchors:
            # print(a)
            a = a.find('a', href=True)
            print(a['href'])
            # if 'href' in a:
            if a['href'].strip() not in res_href:
                lyric_url = a['href'].strip()
                break
        # print(res_href)
        # lyric_url = self.main_uri0.format(res_href['href'])
        print(lyric_url)
        try:
            lyric_req = requests.get(lyric_url, params=self.header)
        except Exception as ex:
            print(ex.__str__())
            return lyric_req

        if lyric_req.status_code == 200:
            lyric_soup = BeautifulSoup(lyric_req.text, 'html.parser')
            lyric_code = lyric_soup.find('p', attrs={'id': 'songLyricsDiv'})
            # print(lyric_code)
            print(len(lyric_code))
            # lyrics_raw = lyric_code[0]
            # print(lyrics_raw)
            cleaned_lyrics = self.html_regex.sub('', str(lyric_code))
            # print(cleaned_lyrics.strip())
            return cleaned_lyrics.strip()


if __name__ == "__main__":
    lyrics_obj = LyricMasti()
    # lyrics_obj.get_lyrics('All+Time+Low+-+Take+Cover')

    ft = open('data/uk_musics_2_1_51_80_list.txt', 'r').readlines()
    print(len(ft))
    fout = open('data/uk_musics_2_1_51_80_lyrics_songlyrics.txt', 'a+')
    ft_er = open('data/uk_musics_2_1_51_80_lyrics_err_songlyrics.txt', 'a+')
    for line in ft:
        # line = 'Loreno Mayer & Nickobella ft. Alius - Home'
        try:
            vi_t, vid, chid, ch_t, dur = line.strip().split('\t')
            lyrics = lyrics_obj.get_lyrics(vi_t).replace('\n',' , ')
            print('in main', lyrics)
            fout.write(line.strip() + '\t' + lyrics + '\n')
        except Exception as e:
            print(e)
            time.sleep(3)
            ft_er.write(line.strip() + '\t' + str(e) + '\n')
    fout.close()
    ft_er.close()
