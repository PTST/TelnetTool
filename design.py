# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(502, 551)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.routerIPLabel = QtGui.QLabel(self.centralwidget)
        self.routerIPLabel.setObjectName(_fromUtf8("routerIPLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.routerIPLabel)
        self.RouterIP = QtGui.QLineEdit(self.centralwidget)
        self.RouterIP.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RouterIP.setObjectName(_fromUtf8("RouterIP"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.RouterIP)
        self.rootPasswordLabel = QtGui.QLabel(self.centralwidget)
        self.rootPasswordLabel.setObjectName(_fromUtf8("rootPasswordLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.rootPasswordLabel)
        self.rootPassword = QtGui.QLineEdit(self.centralwidget)
        self.rootPassword.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.rootPassword.setObjectName(_fromUtf8("rootPassword"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.rootPassword)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.helpbttn = QtGui.QPushButton(self.centralwidget)
        self.helpbttn.setObjectName(_fromUtf8("helpbttn"))
        self.verticalLayout.addWidget(self.helpbttn)
        self.pingbttn = QtGui.QPushButton(self.centralwidget)
        self.pingbttn.setObjectName(_fromUtf8("pingbttn"))
        self.verticalLayout.addWidget(self.pingbttn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.resetbttn = QtGui.QPushButton(self.centralwidget)
        self.resetbttn.setObjectName(_fromUtf8("resetbttn"))
        self.horizontalLayout_3.addWidget(self.resetbttn)
        self.acsbttn = QtGui.QPushButton(self.centralwidget)
        self.acsbttn.setMaximumSize(QtCore.QSize(141, 16777215))
        self.acsbttn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.acsbttn.setAutoDefault(False)
        self.acsbttn.setObjectName(_fromUtf8("acsbttn"))
        self.horizontalLayout_3.addWidget(self.acsbttn)
        self.cntbttn = QtGui.QPushButton(self.centralwidget)
        self.cntbttn.setMaximumSize(QtCore.QSize(140, 16777215))
        self.cntbttn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cntbttn.setObjectName(_fromUtf8("cntbttn"))
        self.horizontalLayout_3.addWidget(self.cntbttn)
        self.gipbttn = QtGui.QPushButton(self.centralwidget)
        self.gipbttn.setCheckable(False)
        self.gipbttn.setDefault(False)
        self.gipbttn.setFlat(False)
        self.gipbttn.setObjectName(_fromUtf8("gipbttn"))
        self.horizontalLayout_3.addWidget(self.gipbttn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setMaximumSize(QtCore.QSize(292, 16777215))
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.unitIP = QtGui.QLineEdit(self.centralwidget)
        self.unitIP.setObjectName(_fromUtf8("unitIP"))
        self.horizontalLayout.addWidget(self.unitIP)
        self.portbttn = QtGui.QPushButton(self.centralwidget)
        self.portbttn.setMaximumSize(QtCore.QSize(101, 16777215))
        self.portbttn.setObjectName(_fromUtf8("portbttn"))
        self.horizontalLayout.addWidget(self.portbttn)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(396, 0))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.routerIPLabel.setText(_translate("MainWindow", "Router IP", None))
        self.rootPasswordLabel.setText(_translate("MainWindow", "Root Password", None))
        self.helpbttn.setText(_translate("MainWindow", "Hjælp", None))
        self.pingbttn.setText(_translate("MainWindow", "Ping", None))
        self.resetbttn.setText(_translate("MainWindow", "Reset CPE", None))
        self.acsbttn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Wireless acs rescan og scanreport</p></body></html>", None))
        self.acsbttn.setText(_translate("MainWindow", "ACS", None))
        self.cntbttn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Connection Stats</p></body></html>", None))
        self.cntbttn.setText(_translate("MainWindow", "Connection Stats", None))
        self.gipbttn.setText(_translate("MainWindow", "GIP Tjek", None))
        self.unitIP.setText(_translate("MainWindow", "Enheds IP", None))
        self.portbttn.setText(_translate("MainWindow", "Sæt Porte", None))

