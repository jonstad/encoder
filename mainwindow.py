# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 552)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-3)
        MainWindow.setStyleSheet("QTableWidget{\n"
"color:red;\n"
"background-color:black;\n"
"\n"
"}\n"
"QComboBox{\n"
"    background-color: black;\n"
"    border: 2px solid red;\n"
"    border-radius: 5px;\n"
"    color: red;\n"
"\n"
"}\n"
"QGroupBox{\n"
"    margin-top: 0.5em;\n"
"    font: 14px arial;\n"
"    color: black;\n"
"    border: 3px solid red;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(255, 0, 0);\n"
"    top: -6px;\n"
"    left: 15px;\n"
"}\n"
"QMenuBar{\n"
"    background-color: rgb(252, 221, 255);\n"
"}\n"
"QMainWindow{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid red;\n"
"}\n"
"\n"
"QPushButton {    \n"
"    color: rgb(255, 0, 0);\n"
"    background-color:black;\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color:red;\n"
"}\n"
"QLabel { \n"
"    background-color: black;\n"
"    color:red;\n"
"    border-style: inset ; \n"
"    border-width: 0px;\n"
"    border-color: rgb(127, 127, 127); \n"
"    border-radius: 5px}\n"
"QDoubleSpinBox{\n"
"    background-color: black;\n"
"    color:red;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    /*background-color: rgb(231, 198, 228);*/\n"
"    border-color:rgb(255, 230, 255);\n"
"    }\n"
"\n"
"QTabWidget { /* The tab widget frame */\n"
"    border-top: 2px solid green;\n"
"    background-color:black;\n"
"    border: 2px solid red;        \n"
"}\n"
"QTabBar{\n"
"    padding: -16px;\n"
"    qproperty-drawBase: 0;\n"
"    border: 2px solid red;        \n"
"    border-radius: 10px;\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));*/\n"
"    background-color:black;\n"
"    color: red;\n"
"    border-style: solid;\n"
"}\n"
"QTabBar::tab {\n"
"    border: 2px solid red;        \n"
"    border-radius: 8px;\n"
"    background-color: red;\n"
"    padding:2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: red;\n"
"    color:black;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    /*margin-top: 4px;  make non-selected tabs look smaller */\n"
"    background-color: black;\n"
"    color: red;\n"
"}\n"
"\n"
"QListWidget {\n"
"    color: rgb(255, 0, 0);\n"
"    /*border: 3px solid red;*/\n"
"    border-radius: 20px;\n"
"    background: black;\n"
"    selection-background-color: rgb(170, 255, 0);\n"
"    selection-color: rgb(255, 255, 0);\n"
"}")
        MainWindow.setAnimated(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(2, 11, 2, 11)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setContentsMargins(0, 5, 7, 5)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ComprtCombo = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComprtCombo.sizePolicy().hasHeightForWidth())
        self.ComprtCombo.setSizePolicy(sizePolicy)
        self.ComprtCombo.setObjectName("ComprtCombo")
        self.horizontalLayout_4.addWidget(self.ComprtCombo)
        self.btnSample = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSample.setObjectName("btnSample")
        self.horizontalLayout_4.addWidget(self.btnSample)
        self.lblTime = QtWidgets.QLabel(self.groupBox_3)
        self.lblTime.setObjectName("lblTime")
        self.horizontalLayout_4.addWidget(self.lblTime)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(0, 5, 7, 5)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblENC2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblENC2.sizePolicy().hasHeightForWidth())
        self.lblENC2.setSizePolicy(sizePolicy)
        self.lblENC2.setMinimumSize(QtCore.QSize(150, 0))
        self.lblENC2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblENC2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblENC2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblENC2.setObjectName("lblENC2")
        self.verticalLayout_3.addWidget(self.lblENC2)
        self.ddsbxENC2 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.ddsbxENC2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ddsbxENC2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ddsbxENC2.setProperty("showGroupSeparator", True)
        self.ddsbxENC2.setDecimals(6)
        self.ddsbxENC2.setProperty("value", 1.74)
        self.ddsbxENC2.setObjectName("ddsbxENC2")
        self.verticalLayout_3.addWidget(self.ddsbxENC2)
        self.btnStopAxial = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStopAxial.sizePolicy().hasHeightForWidth())
        self.btnStopAxial.setSizePolicy(sizePolicy)
        self.btnStopAxial.setObjectName("btnStopAxial")
        self.verticalLayout_3.addWidget(self.btnStopAxial)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lwdgENC2 = QtWidgets.QListWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lwdgENC2.sizePolicy().hasHeightForWidth())
        self.lwdgENC2.setSizePolicy(sizePolicy)
        self.lwdgENC2.setBaseSize(QtCore.QSize(0, 0))
        self.lwdgENC2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lwdgENC2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lwdgENC2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.lwdgENC2.setAutoScrollMargin(16)
        self.lwdgENC2.setAlternatingRowColors(False)
        self.lwdgENC2.setMovement(QtWidgets.QListView.Static)
        self.lwdgENC2.setResizeMode(QtWidgets.QListView.Adjust)
        self.lwdgENC2.setViewMode(QtWidgets.QListView.ListMode)
        self.lwdgENC2.setUniformItemSizes(True)
        self.lwdgENC2.setObjectName("lwdgENC2")
        self.gridLayout_7.addWidget(self.lwdgENC2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(0, 5, 7, 5)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblENC1 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblENC1.sizePolicy().hasHeightForWidth())
        self.lblENC1.setSizePolicy(sizePolicy)
        self.lblENC1.setMinimumSize(QtCore.QSize(150, 0))
        self.lblENC1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblENC1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblENC1.setObjectName("lblENC1")
        self.verticalLayout.addWidget(self.lblENC1)
        self.ddsbxENC1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.ddsbxENC1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ddsbxENC1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ddsbxENC1.setProperty("showGroupSeparator", True)
        self.ddsbxENC1.setPrefix("")
        self.ddsbxENC1.setDecimals(6)
        self.ddsbxENC1.setSingleStep(1e-06)
        self.ddsbxENC1.setProperty("value", 8.280556)
        self.ddsbxENC1.setObjectName("ddsbxENC1")
        self.verticalLayout.addWidget(self.ddsbxENC1)
        self.btnStopRotation = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStopRotation.sizePolicy().hasHeightForWidth())
        self.btnStopRotation.setSizePolicy(sizePolicy)
        self.btnStopRotation.setObjectName("btnStopRotation")
        self.verticalLayout.addWidget(self.btnStopRotation)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lwdgENC1 = QtWidgets.QListWidget(self.tab_3)
        self.lwdgENC1.setBaseSize(QtCore.QSize(0, 0))
        self.lwdgENC1.setAutoFillBackground(False)
        self.lwdgENC1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lwdgENC1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lwdgENC1.setLineWidth(0)
        self.lwdgENC1.setMidLineWidth(0)
        self.lwdgENC1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lwdgENC1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.lwdgENC1.setViewMode(QtWidgets.QListView.ListMode)
        self.lwdgENC1.setObjectName("lwdgENC1")
        self.gridLayout_6.addWidget(self.lwdgENC1, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.horizontalLayout.addWidget(self.tabWidget_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EncoderGenerator"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.btnSample.setText(_translate("MainWindow", "Run test"))
        self.lblTime.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Axial"))
        self.lblENC2.setText(_translate("MainWindow", "Pulses per mm    "))
        self.btnStopAxial.setText(_translate("MainWindow", "Stop axial"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "aux"))
        self.groupBox.setTitle(_translate("MainWindow", "Rotation"))
        self.lblENC1.setText(_translate("MainWindow", "Pulses per *"))
        self.ddsbxENC1.setSuffix(_translate("MainWindow", " pulses per *"))
        self.btnStopRotation.setText(_translate("MainWindow", "Stop rotation"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Speed"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "aux"))

