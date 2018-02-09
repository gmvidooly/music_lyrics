import requests
from bs4 import BeautifulSoup
from crawl_with_link import crawl_it

#ua = UserAgent()
# print(ua.chrome)
#header = {'User-Agent':str(ua.chrome)}
# print(header)

#song = 'love the way you lie'
#url = 'https://search.azlyrics.com/search.php?q='
#req_uri = url+song
# print(req_uri)


def no_artist(song_title, headers):
    url = 'https://search.azlyrics.com/search.php?q='
    req_uri = url + song_title
    data = None
    try:
        data = requests.get(req_uri, headers=headers)
    except Exception:
        return data
    bsoup = BeautifulSoup(data.text, "html.parser")
    song_regex = song_title.replace(' ', '')+'.html'
    song_links = bsoup.find_all('a')
    songs=[]

    for links in song_links:
        parts = links.get('href').split("/")
        if song_regex in parts:
            songs.append(links.get('href'))
    lyrics = None
    if len(songs) < 1:
        lyrics = None
    else:
        song_to_send = songs[0]
        lyrics = crawl_it(song_to_send)
    return lyrics
