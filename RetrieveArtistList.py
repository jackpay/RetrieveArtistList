__author__ = 'jackpay'

import musicbrainzngs as mb, time

def RetrieveArtistsList(outLoc,oset=0,query="type:person"):
    outDoc = open(outLoc,"a")
    art_list = "artist-list"
    art_count = "artist-count"
    alias_list = "alias-list"
    name = "name"
    artists = mb.search_artists(query=query,limit=100)
    offset = oset
    print artists[art_count]
    while offset < artists[art_count]:
        for artist in artists[art_list]:
            outDoc.write(artist[name].encode('UTF-8') + "\n")
            if alias_list in artist:
                for alias in artist[alias_list]:
                    if "alias" in alias:
                        outDoc.write(alias["alias"].encode('UTF-8') + "\n")
        time.sleep(3)
        offset += 100
        print offset
        artists = mb.search_artists(query="type:person",limit=100,offset=offset)
    outDoc.close()
    print "finished"


if __name__ == "__main__":
    oset = 91300
    query = "type:group"
    outLoc = "/Users/jp242/Documents/Projects/Lumi/EntityWhitelist/group-whitelist.txt"
    mb.set_useragent(app="retrieveArtist",version="1.0")
    RetrieveArtistsList(outLoc,oset,query=query)