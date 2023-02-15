import web
import nav
from DB import Db 

web.config.debug = True

urls = (
    '/', 'media',
    '/index','index',
    '/media', 'media'
    
)

class media:
    def GET(self):
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=10)
        media_types=db.select('MediaType', limit=10)

        result = '<html><head><title>Artist.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.nav()
        result += '<h2>List of media type</h2>'
        result += '<div class=container>'
        result += '<table class="table table-dark">'
        result += '<tr><th>Media type</th>'
        for a in a2:
            result +='<tr>'
            for media_type in media_types:
                result +='<td>'+media_type.Name+'</td>'
                break
            result +='</tr>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()