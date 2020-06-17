import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        # self.setGeometry(QApplication.desktop().screenGeometry())
        self.resize(800,480)
        self.setWindowTitle("传感器控制")
        self.view = View(self)
        self.setCentralWidget(self.view)



class View(QWebEngineView):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.load(QUrl("http://127.0.0.1:8123"))
        self.setWindowTitle("New Page")
        self.show()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
