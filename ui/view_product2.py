from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QVBoxLayout, QWidget, QMessageBox, QAction

from dao.product_dao import ProductDao
from model.model_product import ProductTableModel


class ProductTableViewFromUI(QWidget):

    def __init__(self, product_dao=None):
        super().__init__()
        self.ui = uic.loadUi("ui/product_basic.ui")

        # create the view
        self.tableView = self.ui.product_table_view
        self.__product_dao = product_dao
        self.header = ['제품 코드', '제품 명']
        self.reload_data()

        # header size
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 60)

        self.tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 녹색

        # Set the alignment to the headers
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # 셀 내용 수정불가
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # hide grid
        self.tableView.setShowGrid(True)

        # row단위 선택
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # hide vertical header
        hv = self.tableView.verticalHeader()
        hv.setVisible(False)

        # set horizontal header properties
        hh = self.tableView.horizontalHeader()
        hh.setStretchLastSection(True)

        # set column width to fit contents
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.show()
        self.ui.btn_add.clicked.connect(self.add_product)
        self.ui.btn_cancel.clicked.connect(self.cancel_product)

        self.set_context_menu(self.tableView)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        copy_action = QAction("수정", tv)
        quit_action = QAction("삭제", tv)
        tv.addAction(copy_action)
        tv.addAction(quit_action)
        copy_action.triggered.connect(self.__update)
        quit_action.triggered.connect(self.__delete)

    def __update(self):
        updateIdx = self.tableView.selectedIndexes()[0]
        data = self.data[updateIdx.row()]
        self.ui.le_code.setText(data[0])
        self.ui.le_name.setText(data[1])
        self.ui.btn_add.setText("수정")

    def __delete(self):
        deleteIdx = self.tableView.selectedIndexes()[0]
        data = self.data[deleteIdx.row()]
        self.__product_dao.delete_product(code=data[0])
        self.reload_data()

    def add_product(self):
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        print(code, name)

        if self.ui.btn_add.text() == "추가":
            self.add_item(code, name)
        else:
            self.update_item(code, name)

        self.cancel_product()

    def update_item(self, code, name):
        res = self.__product_dao.update_product(code=code, name=name)
        if res:
            self.reload_data()
            self.ui.btn_add.setText("추가")
            QMessageBox.information(self, 'Success!', '{} {} 수정 되었습니다.'.format(code, name), QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Fail!', '{} {} 수정 실패'.format(code, name), QMessageBox.Ok)

    def add_item(self, code, name):
        res = self.__product_dao.insert_product(code=code, name=name)
        if res:
            self.reload_data()
            QMessageBox.information(self, 'Success!', '{} {} 추가 되었습니다.'.format(code, name), QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Fail!', '{} {} 추가 실패'.format(code, name), QMessageBox.Ok)

    def reload_data(self):
        # self.model = None
        data = self.__product_dao.query_with_fetchmany()
        self.model = ProductTableModel(data, self.header)
        self.tableView.setModel(self.model)

    def cancel_product(self):
        self.ui.le_code.clear()
        self.ui.le_name.clear()
