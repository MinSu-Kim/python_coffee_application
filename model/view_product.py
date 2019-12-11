from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTableView, QAbstractItemView, QHeaderView, QWidget, QMainWindow

from dao.product_dao import ProductDao
from model.model_product import ProductTableModel


class ProductTableView(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # create the view
        tableView = QTableView()

        pdt = ProductDao()
        data = pdt.query_with_fetchmany("select * from product")
        header = ['제품 코드', '제품 명']
        self.model = ProductTableModel(data, header)
        tableView.setModel(self.model)

        # header size
        tableView.horizontalHeader().resizeSection(0, 20)
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

        layout = QVBoxLayout()
        layout.addWidget(tableView)

        self.setLayout(layout)
        self.show()

