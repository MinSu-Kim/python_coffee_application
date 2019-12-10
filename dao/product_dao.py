import inspect

from mysql.connector import Error

from db_connection.connection_pool import ConnectionPool


class ProductDao:
    def __init__(self):
        self.connection_pool = ConnectionPool.get_instance()

    def __do_query(self, sql, p_args=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            if p_args is not None:
                cursor.execute(sql, p_args)
            else:
                cursor.execute(sql)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def insert_product(self, sql, code, name):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        args = (code, name)
        self.__do_query(sql, p_args=args)

    def update_product(self, sql, name, code):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        args = (name, code)
        self.__do_query(sql, p_args=args)

    def delete_product(self, sql, code):
        args = (code,)
        self.__do_query(sql, p_args=args)

    def query_with_fetchmany(self, sql):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            res = []
            for row in self.iter_row(cursor, 5):
                res.append(row)
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def iter_row(self, cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row
