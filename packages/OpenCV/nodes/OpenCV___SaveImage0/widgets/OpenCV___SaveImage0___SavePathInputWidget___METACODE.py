from PySide2.QtWidgets import QPushButton, QFileDialog
from PySide2.QtCore import Signal
# from PySide2.QtGui import ...

class %INPUT_WIDGET_TITLE%_PortInstanceWidget(QPushButton):
    path_chosen = Signal(str)

    def __init__(self, parent_port_instance, parent_node_instance):
        super(%INPUT_WIDGET_TITLE%_PortInstanceWidget, self).__init__("Select")

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setStyleSheet('''
            color: #cccccc;
            border-radius: 5px;
            border: 1px solid #aaaaaa;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 25px;
            padding-right: 25px;
            background: transparent;
        ''')

        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        file_path = QFileDialog.getSaveFileName(self, 'Save')[0]
        self.path_chosen.emit(file_path)

    def get_data(self):
        return self.text()

    def set_data(self, data):
        self.setText(data)

    def removing(self):
        pass
