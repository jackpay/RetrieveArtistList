__author__ = 'jackpay'

import musicbrainzngs as mb

def RetrieveArtistsList():
    outD = mb.search_artists()

if __name__ == "__main__":
    mb.set_useragent(app="retrievArtist",version="1.0")
    RetrieveArtistsList()