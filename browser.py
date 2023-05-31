import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class HistoryWindow(QDialog):
    def __init__(self, history):
        super().__init__()
        self.setWindowTitle("Geçmiş")
        self.resize(512,384)

        self.history_list = QListView()
        self.history_list.setModel(history)

        layout = QVBoxLayout()
        layout.addWidget(self.history_list)
        self.setLayout(layout)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Piri Browser v1 source codes")
        self.resize(1280, 720)

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
        self.main_menu_button.clicked.connect(self.go_home)

        self.eba = QPushButton("Eba")
        self.eba.clicked.connect(self.ebago)

        self.eokul = QPushButton("E-Okul")
        self.eokul.clicked.connect(self.goeokul)

        self.history = QStandardItemModel()
        self.history_button = QPushButton("Geçmişi Göster")
        self.history_button.clicked.connect(self.show_history)


        layout = QVBoxLayout()
        layout.addWidget(self.search_bar)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.reload_button)
        button_layout.addWidget(self.main_menu_button)
        button_layout.addWidget(self.eba)
        button_layout.addWidget(self.eokul)
        button_layout.addWidget(self.history_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.browser)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.browser.urlChanged.connect(self.update_history)

    def search_keyword(self):
        url = self.search_bar.text()
        self.browser.load(QUrl(url))

    def update_history(self, url):
        item = QStandardItem(url.toString())
        self.history.appendRow(item)

    def show_history(self):
        dialog = HistoryWindow(self.history)
        dialog.exec_()
    def go_home(self):
       self.browser.load(QUrl("http://piribrowser.rf.gd/"))
    def ebago(self):
        self.browser.load(QUrl("http://eba.gov.tr/"))
    def goeokul(self):
        self.browser.load(QUrl("https://eokulyd.meb.gov.tr/"))
app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec_())
