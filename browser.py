import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Piri Browser v1 source codes")
        self.resize(1024, 768)
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search_keyword)
        self.browser = QWebEngineView()
        self.browser.load(QUrl("http://piribrowser.rf.gd/"))
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.browser.forward)
        self.reload_button = QPushButton("Yenile")
        self.reload_button.clicked.connect(self.browser.reload)
        self.main_menu_button = QPushButton("Ana sayfa")
        self.eba = QPushButton("Eba")
        self.eba.clicked.connect(self.ebago)
        self.main_menu_button.clicked.connect(self.go_home)
        self.eokul=QPushButton("E-Okul")
        self.eokul.clicked.connect(self.goeokul)
        layout = QVBoxLayout()
        layout.addWidget(self.search_bar)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.reload_button)
        button_layout.addWidget(self.main_menu_button)
        button_layout.addWidget(self.eba)
        button_layout.addWidget(self.eokul)
        layout.addLayout(button_layout)
        layout.addWidget(self.browser)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def search_keyword(self):
        search_query = self.search_bar.text().replace(" ", "+")
        if "http" in self.search_bar.text() or "www" in self.search_bar.text():
            url = self.search_bar.text()
        else:
            url = f"https://cse.google.com/cse?cx=845a07a7a23a248a5#gsc.tab=0&gsc.q={search_query}"
        self.browser.load(QUrl(url))
    def anasayfa(self):
        self.browserload(QUrl("http://piribrowser.rf.gd/"))
    def ebago(self):
        self.browser.load(QUrl("https://www.eba.gov.tr"))
    def go_home(self):
        self.browser.load(QUrl("http://piribrowser.rf.gd/"))
    def goeokul(self):
        self.browser.load(QUrl("https://e-okul.meb.gov.tr"))
app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec_())
