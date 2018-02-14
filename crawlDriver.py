from az_lyrics_crawl import AzCrawl
from fake_useragent import UserAgent
from google_search import SearchGoogle
import sys
import time


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
    #lyrics = lcrawl.fetch_lyrics('Loreno Mayer & Nickobella ft. Alius - Home')
    #print('in main', lyrics)
    ft = open('data/uk_musics_2_1_51_80_list.txt', 'r').readlines()
    print(len(ft))
    fout = open('data/uk_musics_2_1_51_80_lyrics.txt','a+')
    ft_er = open('data/uk_musics_2_1_51_80_lyrics_err.txt','a+')
    for line in ft:
        #line = 'Loreno Mayer & Nickobella ft. Alius - Home'
        try:
            vi_t,vid,chid,ch_t,dur=line.strip().split('\t')
            lyrics = lcrawl.fetch_lyrics(vi_t)
            print('in main', lyrics)
            fout.write(line.strip()+'\t'+lyrics+'\n')
        except Exception as e:
            print(e)
            time.sleep(3)
            ft_er.write(line.strip()+'\t'+str(e)+'\n')
    fout.close()
    ft_er.close()
