from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO

    def rifugi_fino_a(anno):
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)

        query = """
                        SELECT DISTINCT r.id AS id_rifugio, r.nome
                        FROM mountain_paths.rifugio r
                        JOIN mountain_paths.connessione c
                        ON r.id = c.id_rifugio1 OR r.id = c.id_rifugio2
                        WHERE c.anno <= %s

                """
        try:
            cursor.execute(query,(anno,))
            for row in cursor:
                rifugio = Rifugio(row['id_rifugio'],row['nome'])
                result.append(rifugio)
        except:
            print("Errore nel database")

        finally:
            cursor.close()
            cnx.close()
        return result

    def connessioni(anno):
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """
                            SELECT id_rifugio1,id_rifugio2
                            from mountain_paths.connessione c,mountain_paths.rifugio r 
                            where anno<=%s and r.id =c.id_rifugio1
                """
        try:
            cursor.execute(query,(anno,))
            for row in cursor:
                conn = Connessione(row['id_rifugio1'],row['id_rifugio2'])
                result.append(conn)
        except:
            print("Errore nel database")
        finally:
            cursor.close()
            cnx.close()
            return result





'''
    def ricerca_rifugi1_anno(anno):
        from model.connessione import Connessione
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)

        query = """
                        select r.nome as nome ,c.id_rifugio1 as id_1, c.id_rifugio2 as id_2
                        from mountain_paths.rifugio r, mountain_paths.connessione c
                        where c.id_rifugio1 = r.id and c.anno <=%s
        """

        cursor.execute(query, (anno,))
        for row in cursor:
            conn = Connessione(row['nome'], row['id_1'], row['id_2'])
            result.append(conn)

        cursor.close()
        cnx.close()
        return result

    def ricerca_rifugi2_anno(anno):
        from model.connessione import Connessione
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)

        query = """
                        select r.nome as nome ,c.id_rifugio1 as id_1, c.id_rifugio2 as id_2
                        from mountain_paths.rifugio r, mountain_paths.connessione c
                        where c.id_rifugio2 = r.id and c.anno <=%s
        """

        cursor.execute(query, (anno,))
        for row in cursor:
            conn = Connessione(row['nome'], row['id_1'], row['id_2'])
            result.append(conn)

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def ricerca_tutti_i_rifugi():
        from model.rifugio import Rifugio

        cnx = DBConnect.get_connection()
        result = {}
        cursor = cnx.cursor(dictionary=True)

        query = """
                    SELECT r.id as id, r.nome as nome 
                    FROM mountain_paths.rifugio r
            """

        try:
            cursor.execute(query)
            for row in cursor:
                rif = Rifugio(row["id"], row["nome"])
                result[rif.id] = rif

        except Exception as e:
            print(f"Errore nella query ricerca_tutti_i_rifugi: {e}")

        finally:
            cursor.close()
            cnx.close()

        return result

'''