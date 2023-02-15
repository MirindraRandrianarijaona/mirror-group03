import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'genre',
    '/index','index',
    '/genre', 'genre'
)

class genre:
    def GET(self):
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=10)
        genres=db.select('Genre', limit=10)


        result = '<html><head><title>Genre.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<h2>List of genre</h2>'
        result += '<div class=container>'
        result += '<table class="table table-dark">'
        result += '<tr><th>Genre</th>'
        for a in a2:
            result +='<tr>'
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            result +='</tr>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()