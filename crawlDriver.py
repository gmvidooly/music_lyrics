from az_lyrics_crawl import AzCrawl
from fake_useragent import UserAgent
from google_search import SearchGoogle
import sys


class CrawlMain:

    def __init__(self):
        self.az_obj = AzCrawl()
        self.gsobj = SearchGoogle()

    def get_user_agent(self):
        ua = UserAgent()
        header = {'User-Agent': str(ua.chrome)}
        return header

    def fetch_lyrics(self, song_title):
        header = self.get_user_agent()
        lyrics = self.az_obj.crawl_az(song_title, header)
        if lyrics is None:
            lyrics = self.gsobj.search_it(song_title)

        return lyrics


if __name__=="__main__":
    lcrawl = CrawlMain()
    lyrics = lcrawl.fetch_lyrics('G-Eazy & Halsey - Him & I')
    print('in main', lyrics)