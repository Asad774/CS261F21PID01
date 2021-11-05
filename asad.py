def getURlOfPage(link , arr):
    url=requests.get(link) 

    content = url.content
    soup = BeautifulSoup(content,'html.parser')
    for s in soup.findAll('div', attrs = {'class': '_4ddWXP'}):
        row=[]
        try:
            a=s.find('a',{'class': 's1Q9rs'},'title').text
        except:
            a=" "
        a=a.replace(",","")
        a=a.replace("-","")
        a=a.replace("(","")
        a=a.replace(")","")
        row.append(a)
        try:
            b=s.find('div',attrs = {'class': '_3Djpdu'}).text
        except:
            b=" "
        b=b.replace(",","")
        b=b.replace("-","")
        b=b.replace("(","")
        b=b.replace(")","")
        row.append(b)
        try:
            c=s.find('div',attrs = {'class': '_3I9_wc'}).text
            c_list=c.split("₹",2)
            c=c_list[1]
        except:
            c="0"
        c=c.replace(",","")
        c=c.replace("-","")
        c=c.replace("(","")
        c=c.replace(")","")
        row.append(c)
        try:
            d=s.find('div',attrs = {'class': '_30jeq3'}).text
            d_list=d.split("₹",2)
            d=d_list[1]
        except:
            d="0"
        d=d.replace(",","")
        d=d.replace("-","")
        d=d.replace("(","")
        d=d.replace(")","")
        row.append(d)
        try:
            e=s.find('div',attrs = {'class': '_3Ay6Sb'}).text
            e_list=e.split("%",2)
            e=e_list[0]
        except:
            e="0"
        e=e.replace(",","")
        e=e.replace("-","")
        e=e.replace("(","")
        e=e.replace(")","")
        row.append(e)
        try:
            f=s.find('div',attrs = {'class': '_3LWZlK'})
            f = f.text
        except:
            f="0"
        f=f.replace(",","")
        f=f.replace("-","")
        f=f.replace("(","")
        f=f.replace(")","")
        row.append(f)
        try:
            g=s.find('span',attrs = {'class': '_2_R_DZ'})
            g = g.text
        except:
            g="0"
        g=g.replace(",","")
        g=g.replace("-","")
        g=g.replace("(","")
        g=g.replace(")","")
        row.append(g)
        arr.append(row)


        

def callingPage(scrap , arr):
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QProgressBar,QPushButton,QVBoxLayout
    from PyQt5.QtGui import QIcon
    from PyQt5.QtCore import pyqtSlot
    import sys

    class Ui_Dialog(object):
        global scrapControlNumber
        global RunPauseControl
        global scrap
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
            n=8400
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(n)
            
            #self.progressBar.setRange(0,n)
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
            self.pushButton_7.setGeometry(QtCore.QRect(150, 440, 111, 23))
            self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
    "background-color: rgb(255, 0, 0);\n"
    "font: 75 italic 12pt \"Arial\";")
            self.pushButton_7.setObjectName("pushButton_7")
            self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
            self.pushButton_8.setGeometry(QtCore.QRect(310, 440, 121, 23))
            self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);\n"
    "background-color: rgb(255, 0, 0);\n"
    "font: 75 italic 12pt \"Arial\";")
            self.pushButton_8.setObjectName("pushButton_8")
            self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
            self.pushButton_9.setGeometry(QtCore.QRect(480, 440, 131, 23))
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
            self.frame_3.setGeometry(QtCore.QRect(0, 0, 741, 541))
            self.frame_3.setStyleSheet("background-color: rgb(8, 143, 143);")
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.label_11 = QtWidgets.QLabel(self.frame_3)
            self.label_11.setGeometry(QtCore.QRect(80, 50, 141, 31))
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
            self.radioButton_5.setGeometry(QtCore.QRect(280, 50, 121, 31))
            self.radioButton_5.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
    "color: rgb(255, 255, 255);")
            self.radioButton_5.setObjectName("radioButton_5")
            self.radioButton_6 = QtWidgets.QRadioButton(self.frame_3)
            self.radioButton_6.setGeometry(QtCore.QRect(440, 50, 141, 31))
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
            self.textEdit.setGeometry(QtCore.QRect(300, 160, 181, 41))
            self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
    "color: rgb(8, 143, 143);\n"
    "font: 75 14pt \"Arial\";")
            self.textEdit.setObjectName("textEdit")
            self.tabWidget.addTab(self.tab_5, "")
            self.retranslateUi(Dialog)
            self.tabWidget.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(Dialog)
            
            
            #######################################################
            
            self.pushButton_11.clicked.connect(self.close)
            self.pushButton_10.clicked.connect(self.returnToMain)
            self.pushButton.clicked.connect(self.AllLinearSort)
            self.pushButton_2.clicked.connect(self.returnToMain)
            self.pushButton_7.clicked.connect(self.returnTolinear)
            self.pushButton_8.clicked.connect(self.returnToMultiple)
            self.pushButton_9.clicked.connect(self.returnTosearch)
            self.pushButton_5.clicked.connect(self.runFunctions)
            self.pushButton_4.clicked.connect(self.pauseFunctions)
            self.pushButton_6.clicked.connect(self.continueFunctions)
            
        def run(self, x):
            for i in range(x):
                b=x
                time.sleep(0.1)
                self.progressBar.setValue(b*400)
             
            
            
        def runFunctions(self):
            scrapControlNumber=0
            RunPauseControl=1
            for i in range(0,21):
                if(RunPauseControl==1):
                    self.scrapping(RunPauseControl, scrapControlNumber)
                    scrapControlNumber=scrapControlNumber+1
                    self.run(scrapControlNumber)
             
        def pauseFunctions(self):
            RunPauseControl=0
            self.run(scrapControlNumber)
            
            
        def continueFunctions(self):
            RunPauseControl=1
            self.scrapping(RunPauseControl, scrapControlNumber)
            self.run(scrapControlNumber)
            
        def insertIncrease(self,x):
            for i in range(1,len(scrap)):
                key=int(scrap[i][x])
                j=i-1
                while(j>=0 and int(scrap[j][x])>key):
                    scrap[j+1]=scrap[j]
                    j=j-1
                scrap[j+1][x]=key
        
        
        def insertdecrease(self,x):
            for i in range(1,len(scrap)):
                key=int(scrap[i][x])
                j=i-1
                while(j>=0 and int(scrap[j][x])<key):
                    scrap[j+1]=scrap[j]
                    j=j-1
                scrap[j+1][x]=key 

        
        def selectionDecrease(self,x):
            for i in range(len(scrap)-1):
                min=int(scrap[i][x])
                index=i
                for j in range(i+1, len(scrap)):
                    if(min<int(scrap[j][x])):
                        min=int(scrap[j][x])
                        index=j
                temp=scrap[i]
                scrap[i]=scrap[index]
                scrap[index]=temp


        def selectionIncrease(self,x):
            for i in range(len(scrap)-1):
                min=int(scrap[i][x])
                index=i
                for j in range(i+1, len(scrap)):
                    if(min>int(scrap[j][x])):
                        min=int(scrap[j][x])
                        index=j
                temp=scrap[i]
                scrap[i]=scrap[index]
                scrap[index]=temp


        def bubbleIncrease(self, push):
            for i in range(len(push)):
                flag=0
                for j in range(len(push)-1-i):
                    if(push[j][1]>push[j+1][1]):
                        temp=push[j]
                        push[j]=push[j+1]
                        push[j+1]=temp
                        flag=1
                if(flag==0):
                    break

            return push

        def showTable(self,tabledata):
            for i in range(len(tabledata)):
                print(tabledata[i])
            for i in range(len(tabledata)):
                self.tableWidget_2.setRowCount(len(tabledata))
                self.tableWidget_2.setColumnCount(7)
                self.tableWidget_2.setHorizontalHeaderLabels(["Name","Current P","Earlier P","Discount","Ratting","people","properties"])
                self.tableWidget_2.setItem( i , 0 ,QTableWidgetItem(tabledata[i][0]))
                self.tableWidget_2.setItem( i , 1 ,QTableWidgetItem(str(tabledata[i][3])))
                self.tableWidget_2.setItem( i , 2 ,QTableWidgetItem(str(tabledata[i][2])))
                self.tableWidget_2.setItem( i , 3 ,QTableWidgetItem(str(tabledata[i][4])))
                self.tableWidget_2.setItem( i , 4 ,QTableWidgetItem(str(tabledata[i][5])))
                self.tableWidget_2.setItem( i , 5 ,QTableWidgetItem(str(tabledata[i][6])))
                self.tableWidget_2.setItem( i , 6 ,QTableWidgetItem(str(tabledata[i][1])))
            self.tabWidget.setCurrentWidget(self.tab_2)


        def star(self ,a,b,c):
            push=[]
            for i in range(len(scrap)):
                temporary=[]
                temporary.append(i)
                temporary.append(int(scrap[i][a]))
                push.append(temporary)

            if(b==3):
                if(c==1):
                    push=self.bubbleIncrease(push)


            demo=[]
            for i in range(len(push)):
                demo.append(scrap[push[i][0]])
             
            self.showTable(demo)



        def AllLinearSort(self):
            #attribute,scrap
            x1=self.comboBox.currentIndex()
            #Alorithm
            x2=self.comboBox_8.currentIndex()
            #order
            if self.radioButton.isChecked():
                x3=1
            elif self.radioButton_2.isChecked():
                x3=2
            else:
                x3=1

            if(x2==0):
                print("Insertion Sort")
                if(x1==0):
                    print("Name")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.insertIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.insertdecrease(3)
                if(x1==1):
                    print("Current price")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.insertIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.insertdecrease(3)
                if(x1==2):
                    print("Earlier price")                    
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.insertIncrease(2)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.insertdecrease(2)
                if(x1==3):
                    print("Discount") 
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.insertIncrease(4)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.insertdecrease(4)
                if(x1==4):
                    print("Ratting")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.insertIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.insertdecrease(3)
                if(x1==5):
                    print("No. of people")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.insertIncrease(6)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.insertdecrease(6)
                if(x1==6):
                    print("Properties")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.insertIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.insertdecrease(3)


            if(x2==2):
                print("Selection Sort")
                if(x1==0):
                    print("Name")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.selectionIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.selectionDecrease(3)
                if(x1==1):
                    print("Current price")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.selectionIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.selectionDecrease(3)
                if(x1==2):
                    print("Earlier price")                    
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.selectionIncrease(2)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.selectionDecrease(2)
                if(x1==3):
                    print("Discount") 
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.selectionIncrease(4)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.selectionDecrease(4)
                if(x1==4):
                    print("Ratting")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.selectionIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.selectionDecrease(3)
                if(x1==5):
                    print("No. of people")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.selectionIncrease(6)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.selectionDecrease(6)
                if(x1==6):
                    print("Properties")
                    if(x3==1):
                        print("Increase")
                        ## Insert sort increase
                        self.selectionIncrease(3)
                    if(x3==2):
                        print("Decrease")
                        ## Insert sort decrease
                        self.selectionDecrease(3)

            if(x2==1):
                print("Merge Sort")

            if(x2==3):
                print("Bubble Sort")
                if(x1==0):
                    print("Name")
                    self.star(3,x2,x3)
                if(x1==1):
                    print("Current price")
                    self.star(3,x2,x3)
                if(x1==2):
                    print("Earlier price")                    
                    self.star(2,x2,x3)
                if(x1==3):
                    print("Discount") 
                    self.star(4,x2,x3)
                if(x1==4):
                    print("Ratting")
                    self.star(3,x2,x3)
                if(x1==5):
                    print("No. of people")
                    self.star(6,x2,x3)
                if(x1==6):
                    print("Properties")
                    self.star(3,x2,x3)
            if(x2==4):
                print("Quick Sort")
            if(x2==5):
                print("Counting Sort")
            if(x2==6):
                print("Radix Sort")
            if(x2==7):
                print("IBucket Sort")
            if(x2==8):
                print("Hybrid Sort")
            if(x2==9):
                print("Heap Sort")
            
            
            self.returnToMain()
            
        def returnTolinear(self):
            self.comboBox.clear()
            self.comboBox.addItem("Name")
            self.comboBox.addItem("Current price")
            self.comboBox.addItem("Earlier price")
            self.comboBox.addItem("Discount")
            self.comboBox.addItem("Ratting")
            self.comboBox.addItem("No. of people")
            self.comboBox.addItem("Properties")

            self.tabWidget.setCurrentWidget(self.tab_3)
            
        def returnToMultiple(self):
            self.comboBox_3.clear()
            self.comboBox_3.addItem("Name")
            self.comboBox_3.addItem("Current price")
            self.comboBox_3.addItem("Earlier price")
            self.comboBox_3.addItem("Discount")
            self.comboBox_3.addItem("Ratting")
            self.comboBox_3.addItem("No. of people")
            self.comboBox_3.addItem("Properties")


            self.comboBox_4.clear()
            self.comboBox_4.addItem("Name")
            self.comboBox_4.addItem("Current price")
            self.comboBox_4.addItem("Earlier price")
            self.comboBox_4.addItem("Discount")
            self.comboBox_4.addItem("Ratting")
            self.comboBox_4.addItem("No. of people")
            self.comboBox_4.addItem("Properties")


            self.comboBox_5.clear()
            self.comboBox_5.addItem("Name")
            self.comboBox_5.addItem("Current price")
            self.comboBox_5.addItem("Earlier price")
            self.comboBox_5.addItem("Discount")
            self.comboBox_5.addItem("Ratting")
            self.comboBox_5.addItem("No. of people")
            self.comboBox_5.addItem("Properties")

            self.tabWidget.setCurrentWidget(self.tab_4)
            
        def returnTosearch(self):

            self.comboBox_7.clear()
            self.comboBox_7.addItem("Name")
            self.comboBox_7.addItem("Current price")
            self.comboBox_7.addItem("Earlier price")
            self.comboBox_7.addItem("Discount")
            self.comboBox_7.addItem("Ratting")
            self.comboBox_7.addItem("No. of people")
            self.comboBox_7.addItem("Properties")


            self.tabWidget.setCurrentWidget(self.tab_5)   


        def returnToMain(self):
            for i in range(len(scrap)):
                self.tableWidget_2.setRowCount(len(scrap))
                self.tableWidget_2.setColumnCount(7)
                self.tableWidget_2.setHorizontalHeaderLabels(["Name","Current P","Earlier P","Discount","Ratting","people","properties"])
                self.tableWidget_2.setItem( i , 0 ,QTableWidgetItem(scrap[i][0]))
                self.tableWidget_2.setItem( i , 1 ,QTableWidgetItem(str(scrap[i][3])))
                self.tableWidget_2.setItem( i , 2 ,QTableWidgetItem(str(scrap[i][2])))
                self.tableWidget_2.setItem( i , 3 ,QTableWidgetItem(str(scrap[i][4])))
                self.tableWidget_2.setItem( i , 4 ,QTableWidgetItem(str(scrap[i][5])))
                self.tableWidget_2.setItem( i , 5 ,QTableWidgetItem(str(scrap[i][6])))
                self.tableWidget_2.setItem( i , 6 ,QTableWidgetItem(str(scrap[i][1])))
            self.tabWidget.setCurrentWidget(self.tab_2)
        
            
        def close(self):
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.hide()
            
               
        def scrapping(self, RunPauseControl, scrapControlNumber):
            if(RunPauseControl ==1 ):
                if(scrapControlNumber == 0):
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy,4mr,q2u&otracker=nmenu_sub_Electronics_0_Mobile%20Cases", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=10", arr)
                    y=open('Test.csv','w',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                if(scrapControlNumber == 1):
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy,4mr,fu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power%20Banks", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&page=10", arr)
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 2):
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy,4mr,lrv&otracker=nmenu_sub_Electronics_0_Screenguards", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/screen-guards/pr?sid=tyy%2C4mr%2Clrv&otracker=nmenu_sub_Electronics_0_Screenguards&page=10", arr)
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 3):
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy,4mr,zzf,7y7&otracker=nmenu_sub_Electronics_0_Memory%20Cards", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/memory-cards-readers/memory-cards/pr?sid=tyy%2C4mr%2Czzf%2C7y7&otracker=nmenu_sub_Electronics_0_Memory+Cards&page=10", arr)
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 4):
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy,vam&otracker=nmenu_sub_Electronics_0_Smart%20Headphones", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=10", arr)
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 5):
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy,4mr,3nu&otracker=nmenu_sub_Electronics_0_Mobile%20Cables", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/cables/pr?sid=tyy%2C4mr%2C3nu&otracker=nmenu_sub_Electronics_0_Mobile+Cables&page=10", arr)
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 6):
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy,4mr,tp2&otracker=nmenu_sub_Electronics_0_Mobile%20Chargers", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/chargers/pr?sid=tyy%2C4mr%2Ctp2&otracker=nmenu_sub_Electronics_0_Mobile+Chargers&page=10", arr)
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 7):
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy,4mr,vnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile%20Holders", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=2", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=3", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=4", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=5", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=6", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=7", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=8", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=9", arr)
                    getURlOfPage("https://www.flipkart.com/mobile-accessories/mobile-holders/pr?sid=tyy%2C4mr%2Cvnf&marketplace=FLIPKART&otracker=nmenu_sub_Electronics_0_Mobile+Holders&page=10", arr)
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 8):
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart%20Glasses%20(VR)")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=2")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=3")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=4")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=5")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=6")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=7")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=8")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=9")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-glasses/pr?sid=ajy%2Ctcy&otracker=nmenu_sub_Electronics_0_Smart+Glasses+%28VR%29&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 9):
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw,nyl,bvv,kbk&otracker=nmenu_sub_Electronics_0_Bp%20Monitors")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=2")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=3")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=4")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=5")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=6")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=7")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=8")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=9")
                    getURlOfPage("https://www.flipkart.com/health-personal-care-appliances/health-care/health-care-devices/blood-pressure-monitors/pr?sid=zlw%2Cnyl%2Cbvv%2Ckbk&otracker=nmenu_sub_Electronics_0_Bp+Monitors&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 10):
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06,nyl,bvv,o4o&otracker=nmenu_sub_Electronics_0_Weighing%20Scale")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=2")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=3")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=4")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=5")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=6")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=7")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=8")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=9")
                    getURlOfPage("https://www.flipkart.com/beauty-and-personal-care/health-care/health-care-devices/weighing-scales/pr?sid=t06%2Cnyl%2Cbvv%2Co4o&otracker=nmenu_sub_Electronics_0_Weighing+Scale&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 11):
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo,jdy,uar&otracker=nmenu_sub_Electronics_0_Pendrives")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=2")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=3")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=4")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=5")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=6")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=7")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=8")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=9")
                    getURlOfPage("https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 12):
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo,ai3,zvm&otracker=nmenu_sub_Electronics_0_Laptop%20Skins%20%26%20Decals")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=2")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=3")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=4")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=5")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=6")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=7")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=8")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=9")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-skins-decals/pr?sid=6bo%2Cai3%2Czvm&otracker=nmenu_sub_Electronics_0_Laptop+Skins+%26+Decals&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 13):
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop%20Bags")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=2")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=3")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=4")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=5")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=6")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=7")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=8")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=9")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/laptop-bags/pr?sid=6bo%2Cai3%2Cqq9&otracker=nmenu_sub_Electronics_0_Laptop+Bags&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                    
                if(scrapControlNumber == 14):
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo,ai3,2ay&otracker=nmenu_sub_Electronics_0_Mouse")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=2")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=3")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=4")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=5")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=6")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=7")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=8")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=9")
                    getURlOfPage("https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=nmenu_sub_Electronics_0_Mouse&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 15):
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home%20Audio%20Speakers")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=2")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=3")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=4")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=5")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=6")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=7")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=8")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=9")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?count=40&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BAudio%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DLaptop%252FDesktop%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&sid=0pm%2F0o7&otracker=nmenu_sub_Electronics_0_Home+Audio+Speakers&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                    
                if(scrapControlNumber == 16):
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home%20Theatres")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=2")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=3")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=4")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=5")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=6")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=7")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=8")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=9")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_Electronics_0_Home+Theatres&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                if(scrapControlNumber == 17):
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=2")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=3")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=4")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=5")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=6")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=7")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=8")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=9")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.type%255B%255D%3DSoundbar&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Electronics_0_Soundbars&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                    
                if(scrapControlNumber == 18):
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth%20Speakers")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=2")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=3")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=4")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=5")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=6")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=7")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=8")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=9")
                    getURlOfPage("https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&otracker=categorytree&p%5B%5D=facets.features%255B%255D%3DBluetooth&otracker=nmenu_sub_Electronics_0_Bluetooth+Speakers&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                    
                if(scrapControlNumber == 19):
                    getURlOfPage("https://www.flipkart.com/home-entertainment/dth/pr?count=40&otracker=categorytree&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sid=ckf%2F9wn&otracker=nmenu_sub_Electronics_0_DTH%20Set%20Top%20Box")
                    getURlOfPage("https://www.flipkart.com/home-entertainment/dth/pr?count=40&otracker=categorytree&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sid=ckf%2F9wn&otracker=nmenu_sub_Electronics_0_DTH+Set+Top+Box&page=2")
                    getURlOfPage("https://www.flipkart.com/home-entertainment/dth/pr?count=40&otracker=categorytree&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sid=ckf%2F9wn&otracker=nmenu_sub_Electronics_0_DTH+Set+Top+Box&page=3")
                    getURlOfPage("https://www.flipkart.com/home-entertainment/dth/pr?count=40&otracker=categorytree&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sid=ckf%2F9wn&otracker=nmenu_sub_Electronics_0_DTH+Set+Top+Box&page=4")
                    getURlOfPage("https://www.flipkart.com/home-entertainment/dth/pr?count=40&otracker=categorytree&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sid=ckf%2F9wn&otracker=nmenu_sub_Electronics_0_DTH+Set+Top+Box&page=5")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=2")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=3")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=4")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=5")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=6")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=7")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=8")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=9")
                    getURlOfPage("https://www.flipkart.com/computers/network-components/routers/pr?sid=6bo%2F70k%2F2a2&otracker=nmenu_sub_Electronics_0_Routers&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                    
                if(scrapControlNumber == 20):
                    getURlOfPage("https://www.flipkart.com/camera-accessories/camera-lenses/pr?uniqueBstoreparam1=val1&sid=jek%2C6l2%2Ce9y&otracker=nmenu_sub_Electronics_0_Lens")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/camera-lenses/pr?uniqueBstoreparam1=val1&sid=jek%2C6l2%2Ce9y&otracker=nmenu_sub_Electronics_0_Lens&page=2")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/camera-lenses/pr?uniqueBstoreparam1=val1&sid=jek%2C6l2%2Ce9y&otracker=nmenu_sub_Electronics_0_Lens&page=3")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/camera-lenses/pr?uniqueBstoreparam1=val1&sid=jek%2C6l2%2Ce9y&otracker=nmenu_sub_Electronics_0_Lens&page=4")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/camera-lenses/pr?uniqueBstoreparam1=val1&sid=jek%2C6l2%2Ce9y&otracker=nmenu_sub_Electronics_0_Lens&page=5")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=6")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=7")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=8")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=9")
                    getURlOfPage("https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                    
                    
                    
                if(scrapControlNumber == 21):
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=2")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=3")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=4")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=5")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=6")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=7")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=8")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=9")
                    getURlOfPage("https://www.flipkart.com/camera-accessories/tripods/pr?count=40&otracker=categorytree&p%5B%5D=sort%3Dpopularity&sid=jek%2F6l2%2Fce6&otracker=nmenu_sub_Electronics_0_Tripods&page=10")
                    y=open('Test.csv','a',newline="",encoding='utf-8')
                    writer=csv.writer(y)
                    writer.writerows(arr)
                    y.close()
                    arr.clear()
                    return 
                
         
            
            
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
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Searching"))
    import source1


    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())

        
##Main code of this file


###ALL Libararies
import pandas as pd
import sys
import time
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
import pandas as pd

###Lists one to scrap and write data to file other to get data from file
arr=[]
scrap=[]
#scrap=pd.read_csv('Test.csv')
file = open("Test.csv")
type(file)
myreader = csv.reader(file)
for row in myreader:
        scrap.append(row)
######showing GUI    
callingPage(scrap , arr)