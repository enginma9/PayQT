import sys
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from datetime import datetime

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Set theme
        self.my_palette = QPalette()
        self.my_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.my_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.my_palette.setColor(QPalette.Base, QColor(53, 53, 53))
        self.my_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.my_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        self.my_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        self.my_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        self.my_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.my_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        self.my_palette.setColor(QPalette.BrightText, QColor(200, 0, 0))
        self.my_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        self.my_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.my_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        app.setPalette(self.my_palette)
        self.Main_Layout  = QVBoxLayout()
        self.setWindowTitle("PayQT")
        self.Main_Layout.setContentsMargins(0,0,0,0)
        self.setWindowOpacity(0.95)
        self.LE = QLineEdit()
        self.Main_Layout.addWidget(self.LE)
        self.Go_Button = QPushButton("Go")
        self.Main_Layout.addWidget(self.Go_Button)
        self.Go_Button.clicked.connect(self.Go_Button_clicked)

        self.H_Layout  = QHBoxLayout()
        self.H_Radio = QRadioButton("Hour")
        self.H_Layout.addWidget(self.H_Radio)
        self.Hour_Label = QLabel("0.00")
        self.H_Layout.addWidget(self.Hour_Label)

        self.D_Layout  = QHBoxLayout()
        self.D_Radio = QRadioButton("Day")
        self.D_Layout.addWidget(self.D_Radio)
        self.Day_Label = QLabel("0.00")
        self.D_Layout.addWidget(self.Day_Label)

        self.W_Layout  = QHBoxLayout()
        self.W_Radio = QRadioButton("Week")
        self.W_Layout.addWidget(self.W_Radio)
        self.Week_Label = QLabel("0.00")
        self.W_Layout.addWidget(self.Week_Label)

        self.M_Layout  = QHBoxLayout()
        self.M_Radio = QRadioButton("Month")
        self.M_Layout.addWidget(self.M_Radio)
        self.Month_Label = QLabel("0.00")
        self.M_Layout.addWidget(self.Month_Label)

        self.Y_Layout  = QHBoxLayout()
        self.Y_Radio = QRadioButton("Year")
        self.Y_Layout.addWidget(self.Y_Radio)
        self.Year_Label = QLabel("0.00")
        self.Y_Layout.addWidget(self.Year_Label)

        self.Main_Layout.addLayout(self.H_Layout)
        self.Main_Layout.addLayout(self.D_Layout)
        self.Main_Layout.addLayout(self.W_Layout)
        self.Main_Layout.addLayout(self.M_Layout)
        self.Main_Layout.addLayout(self.Y_Layout)

        self.widget = QWidget()
        self.widget.setLayout(self.Main_Layout)
        self.setCentralWidget(self.widget)

    def Go_Button_clicked(self):
        try:
            amount = float(self.LE.text())
        except:
            amount = 0
        if self.H_Radio.isChecked():
            iHourly = amount
        elif self.D_Radio.isChecked():
            iHourly = amount / 40
        elif self.W_Radio.isChecked():
            iHourly = amount / 40
        elif self.M_Radio.isChecked():
            iHourly = amount / 160
        elif self.Y_Radio.isChecked():
            iHourly = amount / 2080
        else:
            iHourly = 0

        hourly = str(round(iHourly, 2))
        daily = str(round(iHourly * 8, 2))
        weekly = str(round(iHourly * 40, 2))
        monthly = str(round(iHourly * 160, 2))
        yearly = str(round(iHourly * 2080, 2))

        self.Hour_Label.setText(hourly)
        self.Day_Label.setText(daily)
        self.Week_Label.setText(weekly)
        self.Month_Label.setText(monthly)
        self.Year_Label.setText(yearly)

window = MainWindow()
window.show()
sys.exit(app.exec())
