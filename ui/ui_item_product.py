from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QHBoxLayout

from dto.product_dto import ProductDto
from table_view.product_table import ProductTableView


class ProductUI(QWidget):

    def __init__(self):
        super().__init__()
        self.__product_dao = None
        self.p = ProductDto()

        self.btn_ok = QPushButton("확인")
        self.btn_cancel = QPushButton("취소")

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.btn_ok)
        hlayout.addWidget(self.btn_cancel)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.p)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(ProductTableView())

        self.setLayout(vlayout)
        self.show()

        self.btn_ok.clicked.connect(self.confirm)
        self.btn_cancel.clicked.connect(self.clear)

    def confirm(self):
        p = self.p.get_product()
        print(type(p), p)

    def clear(self):
        self.p.set_product('', '')

    def select_res(self):
        result = self.__product_dao.select_item()
        for row in result:
            print(type(row), row)

    @property
    def product_dao(self):
        return self.__product_dao

    @product_dao.setter
    def product_dao(self, product_dao):
        self.__product_dao = product_dao
        self.select_res()
