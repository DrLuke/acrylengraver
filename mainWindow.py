# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
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
        MainWindow.resize(806, 723)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 564, 657))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.imageLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.gridLayout_2.addWidget(self.imageLabel, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(-1, 6, -1, -1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.checkBoxAspect = QtGui.QCheckBox(self.groupBox)
        self.checkBoxAspect.setChecked(True)
        self.checkBoxAspect.setTristate(False)
        self.checkBoxAspect.setObjectName(_fromUtf8("checkBoxAspect"))
        self.gridLayout_5.addWidget(self.checkBoxAspect, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.buttonResetAspect = QtGui.QPushButton(self.groupBox)
        self.buttonResetAspect.setObjectName(_fromUtf8("buttonResetAspect"))
        self.gridLayout_5.addWidget(self.buttonResetAspect, 4, 1, 1, 1)
        self.doubleSpinBoxWidth = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxWidth.setDecimals(2)
        self.doubleSpinBoxWidth.setMaximum(999999999.0)
        self.doubleSpinBoxWidth.setProperty("value", 0.0)
        self.doubleSpinBoxWidth.setObjectName(_fromUtf8("doubleSpinBoxWidth"))
        self.gridLayout_5.addWidget(self.doubleSpinBoxWidth, 0, 1, 1, 1)
        self.doubleSpinBoxHeight = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxHeight.setPrefix(_fromUtf8(""))
        self.doubleSpinBoxHeight.setDecimals(2)
        self.doubleSpinBoxHeight.setMaximum(999999999.0)
        self.doubleSpinBoxHeight.setObjectName(_fromUtf8("doubleSpinBoxHeight"))
        self.gridLayout_5.addWidget(self.doubleSpinBoxHeight, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox, QtCore.Qt.AlignTop)
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.doubleSpinBoxSafez = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBoxSafez.setDecimals(1)
        self.doubleSpinBoxSafez.setProperty("value", 1.0)
        self.doubleSpinBoxSafez.setObjectName(_fromUtf8("doubleSpinBoxSafez"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxSafez, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.doubleSpinBoxDepth = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBoxDepth.setSingleStep(0.1)
        self.doubleSpinBoxDepth.setProperty("value", 0.1)
        self.doubleSpinBoxDepth.setObjectName(_fromUtf8("doubleSpinBoxDepth"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxDepth, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.spinBoxLoweringspeed = QtGui.QSpinBox(self.groupBox_3)
        self.spinBoxLoweringspeed.setProperty("value", 20)
        self.spinBoxLoweringspeed.setObjectName(_fromUtf8("spinBoxLoweringspeed"))
        self.gridLayout_4.addWidget(self.spinBoxLoweringspeed, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.frame_4)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.radioButtonB = QtGui.QRadioButton(self.groupBox_4)
        self.radioButtonB.setObjectName(_fromUtf8("radioButtonB"))
        self.gridLayout_6.addWidget(self.radioButtonB, 3, 0, 1, 1)
        self.radioButtonR = QtGui.QRadioButton(self.groupBox_4)
        self.radioButtonR.setObjectName(_fromUtf8("radioButtonR"))
        self.gridLayout_6.addWidget(self.radioButtonR, 1, 0, 1, 1)
        self.radioButtonG = QtGui.QRadioButton(self.groupBox_4)
        self.radioButtonG.setObjectName(_fromUtf8("radioButtonG"))
        self.gridLayout_6.addWidget(self.radioButtonG, 2, 0, 1, 1)
        self.radioButtonOrig = QtGui.QRadioButton(self.groupBox_4)
        self.radioButtonOrig.setChecked(True)
        self.radioButtonOrig.setObjectName(_fromUtf8("radioButtonOrig"))
        self.gridLayout_6.addWidget(self.radioButtonOrig, 0, 0, 1, 1)
        self.checkBoxDither = QtGui.QCheckBox(self.groupBox_4)
        self.checkBoxDither.setCheckable(True)
        self.checkBoxDither.setObjectName(_fromUtf8("checkBoxDither"))
        self.gridLayout_6.addWidget(self.checkBoxDither, 4, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.buttonLoad = QtGui.QPushButton(self.frame_3)
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.verticalLayout_3.addWidget(self.buttonLoad)
        self.progressBar = QtGui.QProgressBar(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_3.addWidget(self.progressBar)
        self.buttonGenerate = QtGui.QPushButton(self.frame_3)
        self.buttonGenerate.setEnabled(False)
        self.buttonGenerate.setObjectName(_fromUtf8("buttonGenerate"))
        self.verticalLayout_3.addWidget(self.buttonGenerate)
        self.verticalLayout.addWidget(self.frame_3, QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Size (mm)", None))
        self.checkBoxAspect.setToolTip(_translate("MainWindow", "Keep the current aspect ratio", None))
        self.checkBoxAspect.setText(_translate("MainWindow", "Keep aspect ratio", None))
        self.label_7.setToolTip(_translate("MainWindow", "The height of the engraved image after engraving.", None))
        self.label_7.setText(_translate("MainWindow", "Heigth", None))
        self.label_6.setToolTip(_translate("MainWindow", "The width of the engraved image after engraving.", None))
        self.label_6.setText(_translate("MainWindow", "Width", None))
        self.buttonResetAspect.setToolTip(_translate("MainWindow", "Sets the image height so that the aspect ratio is identical to the image\'s aspect ratio.", None))
        self.buttonResetAspect.setText(_translate("MainWindow", "Reset Aspect Ratio", None))
        self.doubleSpinBoxWidth.setToolTip(_translate("MainWindow", "The width of the engraved image after engraving.", None))
        self.doubleSpinBoxHeight.setToolTip(_translate("MainWindow", "The height of the engraved image after engraving.", None))
        self.doubleSpinBoxHeight.setSuffix(_translate("MainWindow", " ", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Z-Settings (mm)", None))
        self.doubleSpinBoxSafez.setToolTip(_translate("MainWindow", "The height above the acrylic at which translations in the horizontal Plane will be performed.", None))
        self.label_2.setToolTip(_translate("MainWindow", "The height above the acrylic at which translations in the horizontal Plane will be performed.", None))
        self.label_2.setText(_translate("MainWindow", "Safe Z", None))
        self.doubleSpinBoxDepth.setToolTip(_translate("MainWindow", "The depth to which the tool will be lowered to perform the engraving.", None))
        self.label_5.setToolTip(_translate("MainWindow", "The depth to which the tool will be lowered to perform the engraving.", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Engraving<br>depth</p></body></html>", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Feeds and Speeds (mm/s)", None))
        self.spinBoxLoweringspeed.setToolTip(_translate("MainWindow", "Speed at which the lowering into the acrylic happens.", None))
        self.label_3.setToolTip(_translate("MainWindow", "Speed at which the lowering into the acrylic happens.", None))
        self.label_3.setText(_translate("MainWindow", "Lowering Speed", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "View Settings", None))
        self.radioButtonB.setText(_translate("MainWindow", "B", None))
        self.radioButtonR.setText(_translate("MainWindow", "R", None))
        self.radioButtonG.setText(_translate("MainWindow", "G", None))
        self.radioButtonOrig.setText(_translate("MainWindow", "Original", None))
        self.checkBoxDither.setText(_translate("MainWindow", "Dithered", None))
        self.buttonLoad.setText(_translate("MainWindow", "Load image", None))
        self.buttonGenerate.setText(_translate("MainWindow", "Generate G-Code", None))

