from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class CoffeeProduct(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/product.ui")
        # self.ui.show()
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

    def get_product(self):
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        pdt = (code, name)
        return pdt

    def set_product(self, code=None, name=None):
        self.ui.le_code.setText(code)
        self.ui.le_name.setText(name)