from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class ProductUI():
    def __init__(self):
        super().__init__()
        self.ui= uic.loadUi("product.ui")
        self.ui.show()


app = QApplication([])
window = ProductUI()
app.exec_()

# Form, Window = uic.loadUiType("product.ui")
# print(type(Form), type(Window))
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec_()
