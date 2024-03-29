from PyQt5.QtWidgets import QApplication

from dao.product_dao import ProductDao
from dao.sale_dao import SaleDao
from table_view.product_table import ProductTableView
from ui.ui_item_product import ProductUI
from ui.view_product2 import ProductTableViewFromUI


def select_product():
    result = pdt.select_product("select * from product")
    print(type(result), result)
    for row in result:
        print(type(row), row)


def product_dao_test():
    global pdt
    pdt = ProductDao()
    [print(row) for row in pdt.select_product()]
    [print(row) for row in pdt.select_product(sql="select * from product where code like %s", code='A%')]
    sdt = SaleDao()
    [print(row) for row in sdt.select_item()]
    # sdt.insert_item(code='A001', price=5000, saleCnt=10, marginRate=10)
    [print(row) for row in sdt.select_item(no=1)]
    select_product()
    pdt.insert_product("Insert into product values(%s, %s)", 'C001', '라떼')
    select_product()
    pdt.update_product("update product set name = %s where code = %s", '라떼수정', 'C001')
    select_product()
    pdt.delete_product("delete from product where code = %s", 'C001')
    select_product()


def all_ui():
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    dao = ProductDao()
    ex = ProductTableViewFromUI(dao)
    app.exec_()


def module_ui():
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = ProductUI()
    app.exec_()


if __name__ == "__main__":
    # product_dao_test()
    # module_ui()
    all_ui()