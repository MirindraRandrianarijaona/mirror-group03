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
        a2=db.select('Album', limit=10)
        albumids=db.select('Album', limit=10)
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre', limit=10)
        tracks=db.select('Track', limit=10)
        media_types=db.select('MediaType', limit=10)
        playlists=db.select('Playlist', limit=10)
        
        result = '<html><head><title>Server.py G03</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
        result += '</head>'
        result += '<h2>List of album with their genre</h2>'
        result += '<div class=container>'
        result += '<table class="table table-striped">'
        result += '<tr><th>Id</th><th>Genre</th><th>Artists</th><th>Album</th><th>Track</th><th>Media type</th><th>Playlist</th>'
        for a in a2:
            result +='<tr>'
            for albumid in albumids:
                result +='<td>'+str(albumid.AlbumId)+'</td>'
                break
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            for artist in artists:
                result +='<td>'+artist.Name+'</td>'
                break
            for track in tracks:
                result +='<td>'+track.Name+'</td>'
                break
            for media_type in media_types:
                result +='<td>'+media_type.Name+'</td>'
                break
            for playlist in playlists:
                result +='<td>'+playlist.Name+'</td>'
                break
            result +='<td>'+a.Title+'</td>'
            result +='</tr>'
        result +='</table>'
        result +='</div>'
        result += '</body></html>'
        return result
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
