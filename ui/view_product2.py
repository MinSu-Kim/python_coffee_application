from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QVBoxLayout, QWidget

from dao.product_dao import ProductDao
from model.model_product import ProductTableModel


class ProductTableViewFromUI(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("ui/product_basic.ui")
        # create the view
        tableView = self.ui.product_table_view

        self.pdt = ProductDao()
        data = self.pdt.query_with_fetchmany("select * from product")
        header = ['제품 코드', '제품 명']

        self.model = ProductTableModel(data, header)
        tableView.setModel(self.model)

        # header size
        tableView.horizontalHeader().resizeSection(0, 40)
        tableView.horizontalHeader().resizeSection(1, 60)

        tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 녹색

        # Set the alignment to the headers
        tableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # 셀 내용 수정불가
        tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # hide grid
        tableView.setShowGrid(True)

        # row단위 선택
        tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # hide vertical header
        hv = tableView.verticalHeader()
        hv.setVisible(True)

        # set horizontal header properties
        hh = tableView.horizontalHeader()
        hh.setStretchLastSection(True)


        # set column width to fit contents
        tableView.resizeColumnsToContents()
        tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.show()
        self.ui.btn_add.clicked.connect(self.add_product)
        self.ui.btn_cancel.clicked.connect(self.cancel_product)

    def add_product(self):
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        print(code, name)

        self.pdt.insert_product(code, name)
        self.cancel_product()
        self.model.endRemoveRows()
        data = self.pdt.query_with_fetchmany("select * from product")

        for idx, row in enumerate(data):
            self.model.setData(idx, row)

    def cancel_product(self):
        self.ui.le_code.clear()
        self.ui.le_name.clear()