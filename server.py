import web
web.config.debug = True

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00',
        )
        a2=db.select('Album', limit=20)
        artists=db.select('Artist', limit=20)
        genres=db.select('Genre',limit=20)
        result = '<html><head><title>test</title></head>'
        result += '<table border="1">'
        result += '<tr><th>Genre</th><th>Artists</th><th>Album</th>'
        for a in a2:
            result +='<tr>'
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            for artist in artists:
                result +='<td>'+artist.Name+'</td>'
                break
            result +='<td>'+a.Title+'</td>'
            result +='</tr>'
        result +='</table>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
