import web
from DB import Db 
web.config.debug = True

urls = (
    '/', 'artist'
    '/index', 'index',
    '/artist', 'artist'
)

class artist:
    def GET(self):
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=10)
        artists=db.select('Artist', limit=10)

        result = '<html><head><title>Artist.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<nav class="navbar navbar-expand-sm bg-light">'
        result += '<div class="container-fluid">'
        result += '<ul class="navbar-nav">'
        result += '<li class="nav-item"><a class="nav-link" href="/index">Accueil</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/genre">Genre</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/artist">Artists</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/album">Album</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/track">Track</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/media">Media type</a></li>'
        result += '<li class="nav-item"><a class="nav-link" href="/playlist">Playlist</a></li>'
        result += '</ul>'
        result += '</div>'
        result += '</nav>'
        result += '<h2>List of the artists</h2>'
        result += '<div class=container>'
        result += '<table class="table table-dark">'
        result += '<tr><th>Artists</th>'
        for a in a2:
            result +='<tr>'
            for artist in artists:
                result +='<td>'+artist.Name+'</td>'
                break
            result +='</tr>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()