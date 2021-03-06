from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets, QtGui, QtCore

import sys


HACKED = False

class MainWindow(QtWidgets.QWidget):
    def __init__(self, appctxt):
        super().__init__()
        self.canc = False
        self.appctxt = appctxt
        self.g_layout = QtWidgets.QGridLayout(self)
        self.g_layout.setMargin(0)
        self.g_layout.setContentsMargins(0,0,0,0)
        self.background = QtWidgets.QLabel()
        self.background.setPixmap(QtGui.QPixmap(self.appctxt.get_resource("back.PNG")))
        self.background.setAlignment(QtCore.Qt.AlignTop)
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
        self.btn_f.clicked.connect(self.pidgin)

        self.btn_g = QtWidgets.QPushButton()
        self.btn_g.setFixedSize(80, 80)
        self.btn_g.clicked.connect(self.access_denied)

        self.winbtn = QtWidgets.QPushButton()
        self.winbtn.setFixedSize(40,40)

        self.g_layout.addWidget(self.btn_a, 1,0,8,4)
        self.g_layout.addWidget(self.btn_b, 47,0,8,4)
        self.g_layout.addWidget(self.btn_c, 97,0,8,4)
        self.g_layout.addWidget(self.btn_d, 145,0,8,4)
        self.g_layout.addWidget(self.btn_e, 188,0,8,4)
        self.g_layout.addWidget(self.btn_f, 230,0,8,4)
        self.g_layout.addWidget(self.btn_g, 280,0,8,4)
        self.g_layout.addWidget(self.winbtn, 484,2,9,4)

        self.pidwin = None

        self.winmenu = QtWidgets.QMenu()

        self.hack = QtWidgets.QAction("LHuilh??_??t????7887")
        self.hack.triggered.connect(self.hacker)
        self.cclean = QtWidgets.QAction("CCleaner")
        self.cclean.triggered.connect(self.access_denied)
        self.gc = QtWidgets.QAction("Google Chrome")
        self.gc.triggered.connect(self.access_denied)
        self.malw = QtWidgets.QAction("Malwarebyte - Anti-Malware")
        self.malw.triggered.connect(self.access_denied)
        self.mozi = QtWidgets.QAction("Mozilla Firefox")
        self.mozi.triggered.connect(self.access_denied)
        self.pid = QtWidgets.QAction("Pidgin")
        self.pid.triggered.connect(self.pidgin)
        self.inter = QtWidgets.QAction("Internet Explorer")
        self.inter.triggered.connect(self.access_denied)
        self.fileex = QtWidgets.QAction("File Explorer")
        self.fileex.triggered.connect(self.access_denied)
        self.winmed = QtWidgets.QAction("Windows Media Player")
        self.winmed.triggered.connect(self.access_denied)
        self.snip = QtWidgets.QAction("Snipping Tool")
        self.snip.triggered.connect(self.access_denied)

        self.winmenu.addActions([self.cclean, self.fileex, self.gc, self.inter, self.hack, self.malw, self.mozi, self.pid, self.snip, self.winmed])

        self.winbtn.setMenu(self.winmenu)
        self.winbtn.setStyleSheet("QPushButton:menu-indicator {width:0px;}")
    
    def access_denied(self):
        self.win = QtWidgets.QMessageBox()
        self.win.setText("Acess Denied.")
        self.win.setWindowTitle("Error")
        self.win.setIcon(QtWidgets.QMessageBox.Critical)
        self.win.show()

    def closeEvent(self, event: QtGui.QCloseEvent):
        self.canclo = Exit()
        self.canclo.show()
        self.canclo.code.textChanged.connect(self.canclose)
        if self.canc:
            return event.accept()
        return event.ignore()
    
    def nono(self):
        self.win = QtWidgets.QMessageBox()
        self.win.setText("I'm afraid you are not authorised to do this.")
        self.win.setWindowTitle("NOT IN GAME")
        self.win.setIcon(QtWidgets.QMessageBox.Critical)
        self.win.show()

    def pidgin(self):
        if self.pidwin == None:
            self.pidwin = Pidgin()
        self.pidwin.showNormal()
        self.pidwin.activateWindow()

    def hacker(self):
        global HACKED
        HACKED = True
        self.ww = Ww()
        self.ww.showNormal()
        if not self.pidwin == None:
            self.pidwin.menu_files.addAction(self.pidwin.action_code)

    def canclose(self):
        if self.canclo.code.text() == "AdminPro5690":
            self.canc = True
            self.close()

class Pidgin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pidgin - New File")
        self.setWindowFlag(QtGui.Qt.WindowStaysOnTopHint)
        self.text = QtWidgets.QPlainTextEdit()
        self.menu = QtWidgets.QMenuBar()
        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.vlayout.addWidget(self.menu)
        self.vlayout.addWidget(self.text)

        self.action_save = QtWidgets.QAction("Save as")
        self.action_save.triggered.connect(self.nono)
        self.action_open = QtWidgets.QAction("Open")
        self.action_open.triggered.connect(self.nono)
        self.action_exit = QtWidgets.QAction("Exit")
        self.action_exit.triggered.connect(self.close)
        self.action_code = QtWidgets.QAction("huilH??_ty??")
        self.action_code.triggered.connect(self.code)

        self.menu_files = self.menu.addMenu("Files")

        if HACKED == True:
            self.menu_files.addActions([self.action_open, self.action_save, self.action_exit, self.action_code])
        else:
            self.menu_files.addActions([self.action_open, self.action_save, self.action_exit])

    def nono(self):
        self.win = QtWidgets.QMessageBox()
        self.win.setText("Acess Denied.")
        self.win.setWindowTitle("Error")
        self.win.setIcon(QtWidgets.QMessageBox.Critical)
        self.win.show()

    def code(self):
        self.pop = QtWidgets.QMessageBox()
        self.pop.setWindowTitle("YEAAAAAAAAH!")
        self.pop.setText("CONGRATS YOU FOUND ME!")  #ADD THE THINGY THAT NEEDS TO BE ADDED!!!!
        self.pop.setIcon(QtWidgets.QMessageBox.Information)
        self.pop.show()
        self.close()

class Ww(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,75)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.wtfha = QtWidgets.QLabel("What just happenned????")
        self.wtfha.setFont(QtGui.QFont("Bell MT", 25))
        self.wtfha.setStyleSheet("QLabel {color: white;}")
        self.wtfha.setAlignment(QtCore.Qt.AlignCenter)
        self.vl = QtWidgets.QVBoxLayout(self)
        self.vl.addWidget(self.wtfha)
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.bottomLeft())
        self.timer = QtCore.QTimer()
        self.timer.setInterval(3500)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.close)
        self.timer.start()

class Exit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quit? Give admin password")
        self.code = QtWidgets.QLineEdit()
        self.la = QtWidgets.QVBoxLayout(self)
        self.la.addWidget(self.code)
        self.code.setEchoMode(QtWidgets.QLineEdit.Password)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow(appctxt)
    window.showFullScreen()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)