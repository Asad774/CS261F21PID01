from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(737, 566)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 741, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 731, 541))
        self.label_15.setStyleSheet("image: url(:/newPrefix/2.png);\n"
"background-color: rgb(85, 0, 127);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 400, 121, 31))
        self.pushButton_10.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(470, 400, 121, 31))
        self.pushButton_11.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 741, 551))
        self.frame_4.setStyleSheet("background-color: rgb(8, 143, 143);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(60, 40, 131, 31))
        self.label_14.setStyleSheet("font: 75 italic 14pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.progressBar = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar.setGeometry(QtCore.QRect(100, 80, 481, 23))
        self.progressBar.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"background-color: rgb(0, 0, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 130, 75, 23))
        self.pushButton_4.setStyleSheet("font: 75 italic 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 130, 75, 23))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 130, 101, 23))
        self.pushButton_6.setStyleSheet("font: 75 italic 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 480, 111, 23))
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(310, 480, 121, 23))
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 480, 131, 23))
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 180, 701, 231))
        self.tableWidget_2.setStyleSheet("font: 75 11pt \"Arial\";")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(50, 430, 161, 16))
        self.label_17.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(230, 430, 151, 21))
        self.label_18.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 551))
        self.frame.setStyleSheet("background-color: rgb(8, 143, 143);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(196, 39, 141, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 101, 16))
        self.label_2.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 101, 31))
        self.label_3.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(100, 200, 71, 16))
        self.label_4.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(280, 280, 81, 23))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 italic 14pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(250, 90, 191, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(250, 210, 121, 21))
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 14pt \"Arial\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(390, 210, 131, 21))
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 14pt \"Arial\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setGeometry(QtCore.QRect(250, 150, 191, 31))
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frame_2 = QtWidgets.QFrame(self.tab_4)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 741, 551))
        self.frame_2.setStyleSheet("background-color: rgb(8, 143, 143);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(220, 30, 161, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(50, 100, 131, 21))
        self.label_6.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(50, 140, 141, 21))
        self.label_7.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(50, 180, 141, 21))
        self.label_8.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(60, 230, 111, 21))
        self.label_9.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(60, 280, 101, 21))
        self.label_10.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_6.setGeometry(QtCore.QRect(280, 231, 191, 31))
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(280, 290, 121, 21))
        self.radioButton_3.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setGeometry(QtCore.QRect(410, 290, 131, 21))
        self.radioButton_4.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 350, 101, 31))
        self.pushButton_2.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(280, 90, 191, 31))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(280, 140, 191, 31))
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_5.setGeometry(QtCore.QRect(280, 180, 191, 31))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.frame_3 = QtWidgets.QFrame(self.tab_5)
        self.frame_3.setGeometry(QtCore.QRect(10, 0, 741, 541))
        self.frame_3.setStyleSheet("background-color: rgb(8, 143, 143);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(80, 30, 141, 31))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 14pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(80, 120, 131, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 14pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(80, 170, 121, 31))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 14pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 220, 111, 31))
        self.pushButton_3.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_5.setGeometry(QtCore.QRect(280, 30, 121, 31))
        self.radioButton_5.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_6.setGeometry(QtCore.QRect(440, 30, 141, 31))
        self.radioButton_6.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_6.setObjectName("radioButton_6")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 270, 701, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_7.setGeometry(QtCore.QRect(300, 120, 181, 31))
        self.comboBox_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(300, 170, 181, 41))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.textEdit.setObjectName("textEdit")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(76, 69, 121, 31))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 14pt \"Arial\";")
        self.label_16.setObjectName("label_16")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 70, 181, 31))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(8, 143, 143);\n"
"font: 75 14pt \"Arial\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_10.setText(_translate("Dialog", "Start"))
        self.pushButton_11.setText(_translate("Dialog", "End"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Star page"))
        self.label_14.setText(_translate("Dialog", "Progress Bar"))
        self.pushButton_4.setText(_translate("Dialog", "Pause"))
        self.pushButton_5.setText(_translate("Dialog", "Run"))
        self.pushButton_6.setText(_translate("Dialog", "Continue"))
        self.pushButton_7.setText(_translate("Dialog", "Linear Sort"))
        self.pushButton_8.setText(_translate("Dialog", "Multiple Sort"))
        self.pushButton_9.setText(_translate("Dialog", "Searching Sort"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Current Price"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Discoount"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Ratting"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Properties"))
        self.label_17.setText(_translate("Dialog", "Time Taken"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Main page"))
        self.label.setText(_translate("Dialog", "Linear Sorting"))
        self.label_2.setText(_translate("Dialog", "Attribute"))
        self.label_3.setText(_translate("Dialog", "Algorithm"))
        self.label_4.setText(_translate("Dialog", "Order"))
        self.pushButton.setText(_translate("Dialog", "Sort"))
        self.comboBox.setItemText(0, _translate("Dialog", "Name"))
        self.comboBox.setItemText(1, _translate("Dialog", "Earlier price"))
        self.comboBox.setItemText(2, _translate("Dialog", "Past price"))
        self.comboBox.setItemText(3, _translate("Dialog", "Discount"))
        self.comboBox.setItemText(4, _translate("Dialog", "Ratting"))
        self.comboBox.setItemText(5, _translate("Dialog", "No. of people"))
        self.comboBox.setItemText(6, _translate("Dialog", "Properties"))
        self.radioButton.setText(_translate("Dialog", "Ascending"))
        self.radioButton_2.setText(_translate("Dialog", "Descending"))
        self.comboBox_8.setItemText(0, _translate("Dialog", "Insertion Sort"))
        self.comboBox_8.setItemText(1, _translate("Dialog", "Merge Sort"))
        self.comboBox_8.setItemText(2, _translate("Dialog", "Selection Sort"))
        self.comboBox_8.setItemText(3, _translate("Dialog", "Bubble Sort"))
        self.comboBox_8.setItemText(4, _translate("Dialog", "Quick Sort"))
        self.comboBox_8.setItemText(5, _translate("Dialog", "Counting Sort"))
        self.comboBox_8.setItemText(6, _translate("Dialog", "Radix Sort"))
        self.comboBox_8.setItemText(7, _translate("Dialog", "Bucket Sort"))
        self.comboBox_8.setItemText(8, _translate("Dialog", "Hybrid Sort"))
        self.comboBox_8.setItemText(9, _translate("Dialog", "Heap Sort"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Linear sorting"))
        self.label_5.setText(_translate("Dialog", "Multiple Sorting"))
        self.label_6.setText(_translate("Dialog", "First Sort By"))
        self.label_7.setText(_translate("Dialog", "Second Sort By"))
        self.label_8.setText(_translate("Dialog", "Third Sort By"))
        self.label_9.setText(_translate("Dialog", "Algorithm"))
        self.label_10.setText(_translate("Dialog", "Order"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "Insertion Sort"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "Merge Sort"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "Selection Sort"))
        self.comboBox_6.setItemText(3, _translate("Dialog", "Bubble Sort"))
        self.comboBox_6.setItemText(4, _translate("Dialog", "Quick Sort"))
        self.comboBox_6.setItemText(5, _translate("Dialog", "Counting Sort"))
        self.comboBox_6.setItemText(6, _translate("Dialog", "Radix Sort"))
        self.comboBox_6.setItemText(7, _translate("Dialog", "Bucket Sort"))
        self.comboBox_6.setItemText(8, _translate("Dialog", "Hybrid Sort"))
        self.comboBox_6.setItemText(9, _translate("Dialog", "Heap Sort"))
        self.radioButton_3.setText(_translate("Dialog", "Ascending"))
        self.radioButton_4.setText(_translate("Dialog", "Descending"))
        self.pushButton_2.setText(_translate("Dialog", "Sort"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Name"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Earlier price"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Past price"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Discount"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "Ratting"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "No. of people"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "Properties"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Name"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Earlier price"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Past price"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Discount"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "Ratting"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "No. of people"))
        self.comboBox_4.setItemText(6, _translate("Dialog", "Properties"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "Name"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Earlier price"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Past price"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "Discount"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "Ratting"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "No. of people"))
        self.comboBox_5.setItemText(6, _translate("Dialog", "Properties"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Multiple sorting"))
        self.label_11.setText(_translate("Dialog", "Type of Search"))
        self.label_12.setText(_translate("Dialog", "Attribute"))
        self.label_13.setText(_translate("Dialog", "Enter Text"))
        self.pushButton_3.setText(_translate("Dialog", "Search"))
        self.radioButton_5.setText(_translate("Dialog", "Linear"))
        self.radioButton_6.setText(_translate("Dialog", "Binaray"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Current Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Discoount"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Ratting"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "prperties"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "Name"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "Earlier price"))
        self.comboBox_7.setItemText(2, _translate("Dialog", "Past price"))
        self.comboBox_7.setItemText(3, _translate("Dialog", "Discount"))
        self.comboBox_7.setItemText(4, _translate("Dialog", "Ratting"))
        self.comboBox_7.setItemText(5, _translate("Dialog", "No. of people"))
        self.comboBox_7.setItemText(6, _translate("Dialog", "Properties"))
        self.label_16.setText(_translate("Dialog", "Comparison"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Greater"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Lesser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Searching"))


if __name__ == "__main__":
    import source1
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
