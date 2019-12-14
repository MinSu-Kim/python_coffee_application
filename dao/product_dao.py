import inspect

from mysql.connector import Error

from db_connection.connection_pool import ConnectionPool


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


class ProductDao:
    def __init__(self):
        self.connection_pool = ConnectionPool.get_instance()

    def __do_query(self, query=None, p_args=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            if p_args is not None:
                cursor.execute(query, p_args)
            else:
                cursor.execute(query)
            conn.commit()
        except Error as e:
            print(e)
            raise e
        finally:
            cursor.close()
            conn.close()

    def insert_product(self, sql="Insert into product values(%s, %s)", code=None, name=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        args = (code, name)
        try:
            self.__do_query(query=sql, p_args=args)
            return True
        except Error:
            return False

    def update_product(self, sql="update product set name = %s where code = %s", name=None, code=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        args = (name, code)
        try:
            self.__do_query(query=sql, p_args=args)
            return True
        except Error:
            return False

    def delete_product(self, sql="delete from product where code = %s", code=None):
        args = (code,)
        try:
            self.__do_query(query=sql, p_args=args)
            return True
        except Error:
            return False

    def select_product(self, sql="select * from product", code=None):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql) if code is None else cursor.execute(sql, (code,))
            res = []
            [res.append(row) for row in iter_row(cursor, 5)]
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()