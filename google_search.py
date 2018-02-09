from googlesearch import search
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import pycurl
from io import BytesIO

class SearchGoogle:
    def __init__(self):
        self.user_agent = UserAgent()
        self.header = {'User-Agent': str(self.user_agent.chrome)}
        self.html_regex = re.compile(r'<.*?>')

    def search_it(self, song_title):
        suffix = 'lyrics'
        query = song_title+' '+suffix
        print(query)
        clean_lyrics = None
        hit_res = None
        try:
            result = search(query, num=15, stop=1, pause=2)
        except Exception as ex:
            return 'could not query google {}'.format(ex.__str__())

        for res in result:
            print(res)

            if 'lyricsmint' in res:
                hit_res = requests.get(res, params=self.header)
                print(hit_res.status_code)
                if hit_res.status_code == 200:
                    page_soup = BeautifulSoup(hit_res.text, 'html.parser')
                    lyrics = page_soup.find('div', attrs={'id': 'lyric'})
                    # print(lyrics)
                    clean_lyrics = self.html_regex.sub('', str(lyrics))
                    # print(clean_lyrics)
                    # return clean_lyrics

            elif 'songolyrics' in res:
                hit_res = requests.get(res, params=self.header)
                print(hit_res.status_code)
                if hit_res.status_code == 200:
                    page_soup = BeautifulSoup(hit_res.text, 'html.parser')
                    lyrics = page_soup.find('p', attrs={'id': 'lyrics'})
                    # print(lyrics)
                    clean_lyrics = self.html_regex.sub('', str(lyrics))
                    # print(clean_lyrics)
                    # return clean_lyrics

            elif 'lyricsmasti' in res:
                hit_res = requests.get(res, params=self.header)
                print(hit_res.status_code)
                if hit_res.status_code == 200:
                    page_soup = BeautifulSoup(hit_res.text, 'html.parser')
                    lyrics = page_soup.find('code')
                    # print(lyrics)
                    # lyrics_raw = lyrics[0]
                    clean_lyrics = self.html_regex.sub('', str(lyrics))
                    # print(clean_lyrics)
                    # return clean_lyrics

            elif 'lyricsmode' in res:
                hit_res = requests.get(res, params=self.header)
                print(hit_res.status_code)
                if hit_res.status_code == 200:
                    page_soup = BeautifulSoup(hit_res.text, 'html.parser')
                    lyrics = page_soup.find('p', attrs={'id': 'lyrics_text'})
                    clean_lyrics = self.html_regex.sub('', str(lyrics))

            elif 'genius.com' in res:
                hit_res = requests.get(res, params=self.header)
                print(hit_res.status_code)
                if hit_res.status_code == 200:
                    page_soup = BeautifulSoup(hit_res.text, 'html.parser')
                    lyrics = page_soup.find('div', {'class': 'lyrics'}).find('p').text.strip().replace('\n','\t')
                    clean_lyrics = self.html_regex.sub('', str(lyrics))

            elif 'versuri-lyrics' in res:
                hit_res = requests.get(res, params=self.header)
                print(hit_res.status_code)
                if hit_res.status_code == 200:
                    page_soup = BeautifulSoup(hit_res.text, 'html.parser')
                    lyrics = page_soup.find('div', {'class': 'entry-inner'}).find('p').text.strip().replace('\n','\t')
                    clean_lyrics = self.html_regex.sub('', str(lyrics))

            elif 'musixmatch' in res:
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, res)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                c.close()
                body = buffer.getvalue()
                text = body.decode('iso-8859-1')
                page_soup = BeautifulSoup(text, 'html.parser')
                lyrics = page_soup.find('p', {'class': 'mxm-lyrics__content '}).text.strip().replace('\n','\t')
                # print(lyrics)
                clean_lyrics = self.html_regex.sub('', str(lyrics))

        return clean_lyrics


if __name__ == "__main__":
    search_google = SearchGoogle()
    get_lyrics = search_google.search_it('ya ali')
