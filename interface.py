# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system_crawl.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1513, 1012)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 60))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../DC_VideoTools_v01/DC_VideoTools_V01/img/redrum_beeldmerk_280-280.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 30, 100, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_zoekfolder = QtWidgets.QLabel(self.centralwidget)
        self.label_zoekfolder.setObjectName("label_zoekfolder")
        self.horizontalLayout.addWidget(self.label_zoekfolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_resultaat = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_resultaat.setObjectName("tableWidget_resultaat")
        self.tableWidget_resultaat.setColumnCount(3)
        self.tableWidget_resultaat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultaat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultaat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_resultaat.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget_resultaat)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1513, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "Stel crawl folder in:"))
        self.label_2.setText(_translate("MainWindow", "Crawl folder is:"))
        self.label_zoekfolder.setText(_translate("MainWindow", "..."))
        self.tableWidget_resultaat.setSortingEnabled(True)
        item = self.tableWidget_resultaat.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Folder"))
        item = self.tableWidget_resultaat.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sequence"))
        item = self.tableWidget_resultaat.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
