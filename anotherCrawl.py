import requests
from bs4 import BeautifulSoup
import re


def make_request(uri, headers):
    data=None
    try:
        data = requests.get(uri, headers)
    except Exception:
        return data
    bsoup = BeautifulSoup(data.text, "lxml")
    return bsoup


def parse_data(data, song_title):
    all_anchors = data.find_all('a')
    song_title = song_title.replace(' ', '').lower()
    songlinks = []
    for anchors in all_anchors:
        title = str(anchors.get('title'))
        title = title.replace(' ', '').lower()
        if song_title in title:
            songlinks.append(anchors.get('href'))

    if len(songlinks) > 0:
        return songlinks[0]
    else:
        return None


def fetchLyrics(song_link, headers):

    data = requests.get(song_link, headers)
    data_soup = BeautifulSoup(data.text,"lxml")
    song_div = data_soup.find('div', attrs={'class':'song-lyrics-content entry-content post-content'})
    html_regex = re.compile(r'<.*?>')
    lyrics = html_regex.sub('', str(song_div))
    return lyrics


def mcrawl(song_title, headers):
    #url = 'http://www.metrolyrics.com/search.html?search='
    #url = 'http://www.lyricsmint.com/?s='
    url = 'http://www.bollywoodhungama.com/?s='
    #song_title = 'tamma tamma'
    end = '&type=music'
    lyrics = None
    song_title1 = (song_title.replace(' ', '+')).lower()
    search_uri = url+song_title1+end
    print(search_uri)
    data = make_request(search_uri, headers)
    parsed_data = None
    if data is not None:
        parsed_data = parse_data(data, song_title)

    if parsed_data is not None:
        lyrics = fetchLyrics(parsed_data, headers)
    return lyrics
