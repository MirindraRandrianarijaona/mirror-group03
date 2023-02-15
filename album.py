import web
import nav
from DB import Db 
web.config.debug = True

urls = (
    '/', 'album',
    '/index','index',
    '/album', 'album'
)

class album:
    def GET(self):
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=10)
        result = '<html><head><title>Album.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<h2>List of albums</h2>'
        result += '<div class=container>'
        result += '<table class="table table-dark">'
        result += '<tr><th>Album</th>'
        for a in a2:
            result +='<tr>'
            result +='<td>'+a.Title+'</td>'
            result +='</tr>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()