from jikanpy import Jikan

jikan = Jikan()

def search_anime(type, title, page):
    """ Querying for anime based on type and title, and limit the search to 1 page """
    result = jikan.search(type, title, page)

    for i in result['results']:
        animeDetail = {
            
            'url'         : i['url'],
            'image'       : i['image_url'],
            'title'       : i['title'],
            'episodes'    : i['episodes'],
            'airing'      : i['airing'],
            'rated'       : i['rated']
        }

        return animeDetail

    

