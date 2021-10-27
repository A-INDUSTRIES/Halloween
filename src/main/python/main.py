from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets, QtGui, QtCore

import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self, appctxt):
        super().__init__()
        self.appctxt = appctxt
        self.g_layout = QtWidgets.QGridLayout(self)
        self.g_layout.setMargin(0)
        self.background = QtWidgets.QLabel()
        self.background.setPixmap(QtGui.QPixmap(self.appctxt.get_resource("back.PNG")))
        self.g_layout.addWidget(self.background, 1,0,500,1000)
        self.btn_a = QtWidgets.QPushButton()
        self.btn_a.setFixedSize(80, 80)
        self.btn_a.clicked.connect(self.access_denied)
        self.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")

        self.btn_b = QtWidgets.QPushButton()
        self.btn_b.setFixedSize(80, 80)
        self.btn_b.clicked.connect(self.access_denied)

        self.btn_c = QtWidgets.QPushButton()
        self.btn_c.setFixedSize(80, 80)
        self.btn_c.clicked.connect(self.access_denied)

        self.btn_d = QtWidgets.QPushButton()
        self.btn_d.setFixedSize(80, 80)
        self.btn_d.clicked.connect(self.access_denied)

        self.btn_e = QtWidgets.QPushButton()
        self.btn_e.setFixedSize(80, 80)
        self.btn_e.clicked.connect(self.access_denied)

        self.btn_f = QtWidgets.QPushButton()
        self.btn_f.setFixedSize(80, 80)

        self.btn_g = QtWidgets.QPushButton()
        self.btn_g.setFixedSize(80, 80)
        self.btn_g.clicked.connect(self.access_denied)

        self.closebtn = QtWidgets.QPushButton()
        self.closebtn.setFixedSize(40,40)

        self.alttab = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Alt | QtCore.Qt.Key_Tab), self)
        self.alttab.activated.connect(self.nono)

        self.g_layout.addWidget(self.btn_a, 1,0,8,4)
        self.g_layout.addWidget(self.btn_b, 47,0,8,4)
        self.g_layout.addWidget(self.btn_c, 97,0,8,4)
        self.g_layout.addWidget(self.btn_d, 145,0,8,4)
        self.g_layout.addWidget(self.btn_e, 188,0,8,4)
        self.g_layout.addWidget(self.btn_f, 230,0,8,4)
        self.g_layout.addWidget(self.btn_g, 280,0,8,4)
        self.g_layout.addWidget(self.closebtn, 484,2,9,4)
    
    def access_denied(self):
        self.win = QtWidgets.QMessageBox()
        self.win.setText("Acess Denied.")
        self.win.setWindowTitle("Error")
        self.win.setIcon(QtWidgets.QMessageBox.Critical)
        self.win.show()

    def closeEvent(self, event: QtGui.QCloseEvent):
        self.nono()
        return event.ignore()
    
    def nono(self):
        self.win = QtWidgets.QMessageBox()
        self.win.setText("I'm afraid you are not authorised to do this.")
        self.win.setWindowTitle("NOT IN GAME")
        self.win.setIcon(QtWidgets.QMessageBox.Critical)
        self.win.show()

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow(appctxt)
    window.showFullScreen()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)