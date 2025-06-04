from database.DB_connect import DBConnect
from model.order import Order


class DAO():

    @staticmethod
    def getStores():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct s.store_id as id
                from stores s  """

        cursor.execute(query)

        for row in cursor:
            result.append(row["id"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(id):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select o.*
                    from orders o , stores s 
                    where o.store_id = s.store_id 
                    and s.store_id = %s"""

        cursor.execute(query, (id,))

        for row in cursor:
            result.append(Order(**row))

        cursor.close()
        conn.close()
        return result
