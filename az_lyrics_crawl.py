from noArtist import *
from anotherCrawl import *


class AzCrawl:
    def __init__(self):
        pass

    def crawl_az(self, song_title,headers):

        lyrics = no_artist(song_title, headers)
        return lyrics
        '''if lyrics is not None:
            return lyrics
        else:
            lyrics = None
            self.crawl_bollywood_hungana(song_title, headers)'''

    def crawl_bollywood_hungana(self, song_title, headers):
        lyrics1 = mcrawl(song_title, headers)
        return lyrics1
