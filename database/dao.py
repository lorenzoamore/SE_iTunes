from database.DB_connect import DBConnect
from model.album import Album
from model.connessione import Connessione


class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_albums(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select a.id, a.title, a.artist_id, sum(milliseconds/60000) as durata
                    from album a, track t
                    where a.id = t.album_id 
                    group by a.id, a.title, a.artist_id 
                    having durata > %s"""

        cursor.execute(query,(durata,))

        for row in cursor:
            album = Album(
                id = row['id'],
                title = row['title'],
                artist_id = row['artist_id'],
                durata = row['durata'],
            )
            result.append(album)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ with album_selected as(select a.id, a.title, a.artist_id, sum(milliseconds/60000) as durata
                    from album a, track t
                    where a.id = t.album_id 
                    group by a.id, a.title, a.artist_id
                    having durata > %s)
                    select t1.album_id as id1, t2.album_id as id2
                    from track t1, track t2, album_selected a1,album_selected a2, playlist_track pt1, playlist_track pt2
                    where pt1.playlist_id = pt2.playlist_id and pt1.track_id  = t1.id and pt2.track_id = t2.id
                            and a1.id = t1.album_id and a2.id = t2.album_id and a1.id > a2.id
                    group by t1.album_id, t2.album_id"""

        cursor.execute(query,(durata,))

        for row in cursor:
            connessione = Connessione(
                id1 = row['id1'],
                id2 = row['id2'],
            )
            result.append(connessione)

        cursor.close()
        conn.close()
        return result