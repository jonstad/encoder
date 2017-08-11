# always seem to need this
import sys
import findserialport
import serial

import threading
import time
# This gets the Qt stuff
import PyQt5 
from PyQt5.QtWidgets import QMainWindow  # @NoMove

# This is our window from QtCreator
import mainwindow
from PyQt5.Qt import QApplication, QComboBox
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5 import QtCore
import test

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
### functions for the buttons to call

    #validchoicesENC1=[225,13,14,15,16,19]
    #validchoicesENC2=[400,500,600,700,800,900]
    def test(self):
        self.tabledata.append([1,1,1,1,1])
        self.table.model().layoutChanged.emit()
        print ('success')

    def initListview1(self):
        t=12
        print("ddsbxENC changed") 
        pulsesperdeg=self.ddsbxENC1.value()        
        
        for i in test.validchoicesENC1:
            F= 1000000/(4*t*i)
            # speed = F*4/(8.280556)
            speed = F*4/(pulsesperdeg)
            strm = '     Rot per second %.2f Frequency: %.2f changed text ' %  (speed/360, F)
            self.lwdgENC1.addItem(strm)
    
    
    def initListview2(self):    
        t=12
        pulsespermm=self.ddsbxENC2.value() 
        for i in test.validchoicesENC2:
            F= 1000000/(4*t*i)
            # speed = F*4/(8.280556)
            speed = F*4/(pulsespermm)
            strm = '    Speed -  %.2f mm/s --  %.2f m/min -- Frequency: %.2f --' %  (speed,(speed*60/1000), F)
            self.lwdgENC2.addItem(strm)
    def initTablewidget1(self):
            # https://pythonspot.com/en/pyqt5-table/
        #Create table
        self.tableWidget.setRowCount(len(test.validchoicesENC2))
        self.tableWidget.setColumnCount(3)
        t=12
        pulsespermm=self.ddsbxENC2.value() 
        count=0
        for i in test.validchoicesENC2:
            F= 1000000/(4*t*i)
            # speed = F*4/(8.280556)
            speed = F*4/(pulsespermm)
            strm = '    Speed -  %.2f mm/s --  %.2f m/min -- Frequency: %.2f --' %  (speed,(speed*60/1000), F)
            self.tableWidget.setItem(count,0, QTableWidgetItem(str(speed)))
            self.tableWidget.setItem(count,1, QTableWidgetItem(str(speed*60/1000)))
            self.tableWidget.setItem(count,2, QTableWidgetItem(str(F)))
            count=count+1

        #self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        #self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setHorizontalHeaderLabels(["mm/s","m/min","Freq"])
        self.tableWidget.move(0,0)
    
    
    def ddsbxENC1_valueChanged(self):
        self.lwdgENC1.clear()
        self.initListview1()    
        
    # Define a function for the thread
    def displayTime(self):
        currenttime= QtCore.QDateTime.currentDateTime()
        self.lblTime.setText(currenttime.toString())
    def threaded_delay(self):
        newcommand ="xB%05d" % (30001)
        self.sendCommand(newcommand.encode())   
    def pressedbtnSample(self):
        #stime = QtCore.QDateTime.currentDateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        t = threading.Timer(10, self.threaded_delay)
        newcommand ="xB%05d" % (900)
        self.sendCommand(newcommand.encode())
        t.start()
     
    def pressedbtnStopAxial(self):
        newcommand ="xB%05d" % (30001)
        self.sendCommand(newcommand.encode())
    def pressedbtnStopRotation(self):
        newcommand ="xA%05d" % (30001)
        self.sendCommand(newcommand.encode())        

    def sendCommand(self,command):
        try:
            ser.write(command)
            print(command)
        except :
            print("Port not open") 
    def pressedOffButton(self):
        print ("Pressed Off!")
        #self.txtName1.setText("Button 2 was pressed")
    def onActivated(self,index):
        print("activated")
        self.cmB1.addItem("test1")
        print(self.lineEdit_2.text())
        # access variables inside of the UI's file
    def handleActivated(self, index):
        print(self.cmB1.itemText(index))
    
    # Send command to Arduino
    def print_info1(self):
        print("")
        print(self.lwdgENC1.currentItem().text()) 
        print(test.validchoicesENC1[self.lwdgENC1.currentRow()])
        newcommand ="xA%05d" % (test.validchoicesENC1[self.lwdgENC1.currentRow()])
        self.sendCommand(newcommand.encode())
    def print_info2(self):
        print(self.lwdgENC2.currentItem().text()) 
        print(test.validchoicesENC2[self.lwdgENC2.currentRow()])
        newcommand ="xB%05d" % (test.validchoicesENC2[self.lwdgENC2.currentRow()])
        self.sendCommand(newcommand.encode())        
    def comportActivated(self,command):
        global ser
        print(command)
        try:
            ser = serial.Serial(command)        
        except :
            print("Not valid") 
    
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())        
    
    def createTable(self):
        # https://pythonspot.com/en/pyqt5-table/
        #Create table
        #self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        #validator = PyQt5.QtGui.QDoubleValidator()    

        ### Hooks to for buttons
        self.btnStopAxial.clicked.connect(lambda: self.pressedbtnStopAxial())
        self.btnStopRotation.clicked.connect(lambda: self.pressedbtnStopRotation())
        self.btnSample.clicked.connect(lambda: self.pressedbtnSample())
        ### Hooks for listwidget
        self.lwdgENC1.itemClicked.connect(self.print_info1)
        self.lwdgENC2.itemClicked.connect(self.print_info2)
        
        self.ddsbxENC1.valueChanged.connect(lambda: self.ddsbxENC1_valueChanged())
        ### Setup serial port stuff
        tekst = findserialport.serial_ports()
        print(tekst)
        #ComprtCombo = QComboBox(self)
        self.ComprtCombo.addItem("--Select port--")  
        for port in tekst:
            self.ComprtCombo.addItem(port)     

        self.ComprtCombo.activated[str].connect(self.comportActivated) 
        #self.pushButton.clicked.connect(lambda: self.pressedOnButton())
        #self.btnOK2.clicked.connect(lambda: self.pressedOffButton())
        self.initListview1()
        self.initListview2()
        
        #setButtonSymbols(QAbstractSpinBox::NoButtons)
        #self.createTable()
        self.initTablewidget1()
# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
