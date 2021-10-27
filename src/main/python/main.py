from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets, QtGui

import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self, appctxt):
        super().__init__()
        self.appctxt = appctxt
        self.g_layout = QtWidgets.QGridLayout(self)
        self.g_layout.setMargin(0)
        self.background = QtWidgets.QLabel()
        self.background.setPixmap(QtGui.QPixmap(self.appctxt.get_resource("back.PNG")))
        self.g_layout.addWidget(self.background, 1,1,100,100)
        self.btn_a = QtWidgets.QPushButton()
        self.btn_a.setFixedSize(80, 80)
        self.btn_a.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")

        self.btn_b = QtWidgets.QPushButton()
        self.btn_b.setFixedSize(80, 80)
        self.btn_b.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")

        self.btn_c = QtWidgets.QPushButton()
        self.btn_c.setFixedSize(80, 80)
        self.btn_c.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")

        self.btn_d = QtWidgets.QPushButton()
        self.btn_d.setFixedSize(80, 80)
        self.btn_d.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")

        self.btn_e = QtWidgets.QPushButton()
        self.btn_e.setFixedSize(80, 80)
        self.btn_e.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")

        self.btn_f = QtWidgets.QPushButton()
        self.btn_f.setFixedSize(80, 80)
        self.btn_f.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")

        self.btn_g = QtWidgets.QPushButton()
        self.btn_g.setFixedSize(80, 80)
        self.btn_g.setStyleSheet("QPushButton {border:none; background-color:rgba(0,0,0,0)} QPushButton:pressed {background-color: rgba(155,1,1,0.2);}")
        self.g_layout.addWidget(self.btn_a, 1,1,8,4)
        self.g_layout.addWidget(self.btn_b, 1,1,8,4)
        self.g_layout.addWidget(self.btn_c, 1,1,8,4)
        self.g_layout.addWidget(self.btn_d, 1,1,8,4)
        self.g_layout.addWidget(self.btn_e, 1,1,8,4)
        self.g_layout.addWidget(self.btn_f, 1,1,8,4)
        self.g_layout.addWidget(self.btn_g, 1,1,8,4)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow(appctxt)
    window.showFullScreen()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)