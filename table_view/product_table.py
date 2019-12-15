from PyQt5.QtWidgets import QVBoxLayout, QWidget

from dao.product_dao import ProductDao
from model.model_product import ProductTableModel
from table_view.create_table import create_table_view


class ProductTableView(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # create the view
        tableView = create_table_view(20, 60)

        pdt = ProductDao()
        data = pdt.select_product()
        self.model = ProductTableModel(data)

        tableView.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(tableView)

        self.setLayout(layout)
        self.show()



