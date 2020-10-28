from jikanpy import Jikan
from flask import Flask, render_template, url_for, redirect, session, logging, request, flash
from wtforms import Form, StringField, SelectField

jikan = Jikan()

choices = [
    ('Anime', 'Anime'),
    ('Manga', 'Manga')]

class SearchForm(Form):


    select = StringField('')
    search = StringField('')



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == "POST" and search.validate():
        tipe    = search.select.data
        title   = search.search.data

        data = search_stuffs(tipe, title)
        print(data)
        
        return render_template('search.html', form=search, data=data)
    return render_template('search.html', form=search)



def search_stuffs(type, title):
    """ Querying for anime based on type and title, and limit the search to 1 page """
    
    result = jikan.search(type, title, 1)

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



if __name__ == "__main__":
    app.run(debug=True)



