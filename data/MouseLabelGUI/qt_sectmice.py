# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_sectmice.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnLoad = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy)
        self.btnLoad.setMinimumSize(QtCore.QSize(150, 0))
        self.btnLoad.setObjectName("btnLoad")
        self.verticalLayout.addWidget(self.btnLoad)
        self.btnPrevImag = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrevImag.setObjectName("btnPrevImag")
        self.verticalLayout.addWidget(self.btnPrevImag)
        self.btnNextImag = QtWidgets.QPushButton(self.centralwidget)
        self.btnNextImag.setObjectName("btnNextImag")
        self.verticalLayout.addWidget(self.btnNextImag)
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout.addWidget(self.btnClear)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rdoMice1 = QtWidgets.QRadioButton(self.groupBox)
        self.rdoMice1.setObjectName("rdoMice1")
        self.verticalLayout_3.addWidget(self.rdoMice1)
        self.rdoMice2 = QtWidgets.QRadioButton(self.groupBox)
        self.rdoMice2.setObjectName("rdoMice2")
        self.verticalLayout_3.addWidget(self.rdoMice2)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnZoom = QtWidgets.QPushButton(self.centralwidget)
        self.btnZoom.setCheckable(True)
        self.btnZoom.setChecked(False)
        self.btnZoom.setObjectName("btnZoom")
        self.verticalLayout.addWidget(self.btnZoom)
        self.btnZoomReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnZoomReset.setObjectName("btnZoomReset")
        self.verticalLayout.addWidget(self.btnZoomReset)
        self.ckbZoomLock = QtWidgets.QCheckBox(self.centralwidget)
        self.ckbZoomLock.setChecked(True)
        self.ckbZoomLock.setObjectName("ckbZoomLock")
        self.verticalLayout.addWidget(self.ckbZoomLock)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 26))
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
        self.btnLoad.setText(_translate("MainWindow", "Load Images"))
        self.btnPrevImag.setText(_translate("MainWindow", "<=== Image"))
        self.btnNextImag.setText(_translate("MainWindow", " ===>"))
        self.btnClear.setText(_translate("MainWindow", "CLEAR"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.rdoMice1.setText(_translate("MainWindow", "Mice 1"))
        self.rdoMice2.setText(_translate("MainWindow", "Mice 2"))
        self.btnZoom.setText(_translate("MainWindow", "Zoom IN"))
        self.btnZoomReset.setText(_translate("MainWindow", "... Reset"))
        self.ckbZoomLock.setText(_translate("MainWindow", "... Lock"))
