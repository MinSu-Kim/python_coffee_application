from dao.product_dao import ProductDao
from db_connection.connection_pool import ConnectionPool


def select_product():
    result = pdt.query_with_fetchmany("select * from product")
    print(type(result), result)
    for row in result:
        print(type(row), row)


if __name__ == "__main__":
    con = ConnectionPool.get_instance().get_connection()
    print(con)

    pdt = ProductDao()
    select_product()
    pdt.insert_product("Insert into product values(%s, %s)", 'C001', '라떼')
    select_product()

    pdt.update_product("update product set name = %s where code = %s", '라떼수정', 'C001')
    select_product()

    pdt.delete_product("delete from product where code = %s", 'C001')
    select_product()