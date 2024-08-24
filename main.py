from PyQt6 import QtCore, QtGui, QtWidgets
from module import change_music, connect_play_button, main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(600, 400)
        MainWindow.setStyleSheet("background-color: #414833")
        MainWindow.setWindowIcon(QtGui.QIcon("icons/icon.jpg"))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label for music name
        self.music_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.music_name_label.setGeometry(QtCore.QRect(100, 100, 400, 50))
        font = QtGui.QFont("Arial", 15)
        self.music_name_label.setFont(font)
        self.music_name_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.music_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.music_name_label.setStyleSheet("background-color: black")

        # create header title for project
        self.header_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(0, 10, 600, 30))
        font = QtGui.QFont("Arial", 15)
        font.setBold(True)
        self.header_label.setFont(font)
        self.header_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("background-color: red")

        # create button for play and pause music
        self.music_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.music_pushButton.setGeometry(QtCore.QRect(240, 285, 100, 50))
        self.music_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.music_pushButton.setStyleSheet("border: null")
        self.music_pushButton.setIcon(QtGui.QIcon("icons/pause.png"))
        self.music_pushButton.setIconSize(QtCore.QSize(100, 50))
        self.music_pushButton.setObjectName("play")
        self.music_pushButton.clicked.connect(lambda: connect_play_button(self))

        # create button for play and last music
        self.last_music_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.last_music_pushButton.setGeometry(QtCore.QRect(100, 285, 100, 50))
        self.last_music_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.last_music_pushButton.setStyleSheet("border: null")
        self.last_music_pushButton.setIcon(QtGui.QIcon("icons/last.png"))
        self.last_music_pushButton.setIconSize(QtCore.QSize(100, 50))
        self.last_music_pushButton.setObjectName("last_music")
        self.last_music_pushButton.clicked.connect(lambda: change_music(self, "last"))

        # create button for play and next music
        self.next_music_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_music_pushButton.setGeometry(QtCore.QRect(380, 285, 100, 50))
        self.next_music_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.next_music_pushButton.setStyleSheet("border: null")
        self.next_music_pushButton.setIcon(QtGui.QIcon("icons/next.png"))
        self.next_music_pushButton.setIconSize(QtCore.QSize(100, 50))
        self.next_music_pushButton.setObjectName("next_music")
        self.next_music_pushButton.clicked.connect(lambda: change_music(self, "next"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.music_name_label.setText(_translate("MainWindow", "**music name**"))
        self.header_label.setText(_translate("MainWindow", "Music Player"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec())
