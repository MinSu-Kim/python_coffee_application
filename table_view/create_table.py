from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView, QAbstractItemView, QHeaderView


def create_table_view(*args):
    tableView = QTableView()

    # header size
    for i, width in enumerate(args):
        tableView.horizontalHeader().resizeSection(i, width)

    tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 회색

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
    return tableView