# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_MagGridDialog.ui'
#
# Created: Tue Apr 03 17:23:34 2018
#      by: PyQt4 UI code generator 4.10
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

class Ui_AGTMagGridDialog(object):
    def setupUi(self, AGTMagGridDialog):
        AGTMagGridDialog.setObjectName(_fromUtf8("AGTMagGridDialog"))
        AGTMagGridDialog.resize(375, 465)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AGTMagGridDialog.sizePolicy().hasHeightForWidth())
        AGTMagGridDialog.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QtGui.QGridLayout(AGTMagGridDialog)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox_4 = QtGui.QGroupBox(AGTMagGridDialog)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.inFileLine = QtGui.QLineEdit(self.groupBox_4)
        self.inFileLine.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.inFileLine.setObjectName(_fromUtf8("inFileLine"))
        self.gridLayout_4.addWidget(self.inFileLine, 0, 1, 1, 1)
        self.ButtonBrowse = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonBrowse.sizePolicy().hasHeightForWidth())
        self.ButtonBrowse.setSizePolicy(sizePolicy)
        self.ButtonBrowse.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowse.setObjectName(_fromUtf8("ButtonBrowse"))
        self.gridLayout_4.addWidget(self.ButtonBrowse, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.gBox_Output = QtGui.QGroupBox(AGTMagGridDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gBox_Output.sizePolicy().hasHeightForWidth())
        self.gBox_Output.setSizePolicy(sizePolicy)
        self.gBox_Output.setObjectName(_fromUtf8("gBox_Output"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gBox_Output)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.coordFieldschk = QtGui.QCheckBox(self.gBox_Output)
        self.coordFieldschk.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.coordFieldschk.setObjectName(_fromUtf8("coordFieldschk"))
        self.gridLayout_3.addWidget(self.coordFieldschk, 1, 2, 1, 2)
        self.outputFilename = QtGui.QLineEdit(self.gBox_Output)
        self.outputFilename.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.outputFilename.setObjectName(_fromUtf8("outputFilename"))
        self.gridLayout_3.addWidget(self.outputFilename, 0, 1, 1, 2)
        self.ButtonBrowseShape = QtGui.QPushButton(self.gBox_Output)
        self.ButtonBrowseShape.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonBrowseShape.setObjectName(_fromUtf8("ButtonBrowseShape"))
        self.gridLayout_3.addWidget(self.ButtonBrowseShape, 0, 3, 1, 1)
        self.datFilechkbox = QtGui.QCheckBox(self.gBox_Output)
        self.datFilechkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.datFilechkbox.setObjectName(_fromUtf8("datFilechkbox"))
        self.gridLayout_3.addWidget(self.datFilechkbox, 1, 0, 1, 2)
        self.outputLabel = QtGui.QLabel(self.gBox_Output)
        self.outputLabel.setObjectName(_fromUtf8("outputLabel"))
        self.gridLayout_3.addWidget(self.outputLabel, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.gBox_Output, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(AGTMagGridDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        self.medchk = QtGui.QCheckBox(self.groupBox_2)
        self.medchk.setChecked(True)
        self.medchk.setObjectName(_fromUtf8("medchk"))
        self.gridLayout_5.addWidget(self.medchk, 0, 0, 1, 1)
        self.percentSpin = QtGui.QSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentSpin.sizePolicy().hasHeightForWidth())
        self.percentSpin.setSizePolicy(sizePolicy)
        self.percentSpin.setSuffix(_fromUtf8(""))
        self.percentSpin.setPrefix(_fromUtf8(""))
        self.percentSpin.setMinimum(0)
        self.percentSpin.setMaximum(100)
        self.percentSpin.setProperty("value", 25)
        self.percentSpin.setObjectName(_fromUtf8("percentSpin"))
        self.gridLayout_5.addWidget(self.percentSpin, 1, 2, 1, 1)
        self.percentilechk = QtGui.QCheckBox(self.groupBox_2)
        self.percentilechk.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentilechk.sizePolicy().hasHeightForWidth())
        self.percentilechk.setSizePolicy(sizePolicy)
        self.percentilechk.setObjectName(_fromUtf8("percentilechk"))
        self.gridLayout_5.addWidget(self.percentilechk, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(AGTMagGridDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        self.trendchk = QtGui.QCheckBox(self.groupBox_3)
        self.trendchk.setObjectName(_fromUtf8("trendchk"))
        self.gridLayout_6.addWidget(self.trendchk, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 1, 1, 1, 1)
        self.trendPercentileChk = QtGui.QCheckBox(self.groupBox_3)
        self.trendPercentileChk.setObjectName(_fromUtf8("trendPercentileChk"))
        self.gridLayout_6.addWidget(self.trendPercentileChk, 2, 1, 1, 1)
        self.polyOrdSpin = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polyOrdSpin.sizePolicy().hasHeightForWidth())
        self.polyOrdSpin.setSizePolicy(sizePolicy)
        self.polyOrdSpin.setSuffix(_fromUtf8(""))
        self.polyOrdSpin.setPrefix(_fromUtf8(""))
        self.polyOrdSpin.setMinimum(1)
        self.polyOrdSpin.setMaximum(3)
        self.polyOrdSpin.setProperty("value", 3)
        self.polyOrdSpin.setObjectName(_fromUtf8("polyOrdSpin"))
        self.gridLayout_6.addWidget(self.polyOrdSpin, 1, 2, 1, 1)
        self.trendPercentileSpinBox = QtGui.QSpinBox(self.groupBox_3)
        self.trendPercentileSpinBox.setMaximum(100)
        self.trendPercentileSpinBox.setProperty("value", 25)
        self.trendPercentileSpinBox.setObjectName(_fromUtf8("trendPercentileSpinBox"))
        self.gridLayout_6.addWidget(self.trendPercentileSpinBox, 2, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(AGTMagGridDialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox_geo = QtGui.QCheckBox(self.groupBox)
        self.checkBox_geo.setEnabled(True)
        self.checkBox_geo.setObjectName(_fromUtf8("checkBox_geo"))
        self.gridLayout_2.addWidget(self.checkBox_geo, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 4, 0, 1, 1)
        self.widget = QtGui.QWidget(AGTMagGridDialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.allProcess_button = QtGui.QPushButton(self.widget)
        self.allProcess_button.setObjectName(_fromUtf8("allProcess_button"))
        self.gridLayout.addWidget(self.allProcess_button, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.widget, 5, 0, 1, 1)

        self.retranslateUi(AGTMagGridDialog)
        QtCore.QMetaObject.connectSlotsByName(AGTMagGridDialog)

    def retranslateUi(self, AGTMagGridDialog):
        AGTMagGridDialog.setWindowTitle(_translate("AGTMagGridDialog", "MXPDA/GRAD601 processing - Grid survey", None))
        self.label.setText(_translate("AGTMagGridDialog", "Raw data (.dat)", None))
        self.ButtonBrowse.setText(_translate("AGTMagGridDialog", "browse", None))
        self.gBox_Output.setTitle(_translate("AGTMagGridDialog", "Output files", None))
        self.coordFieldschk.setText(_translate("AGTMagGridDialog", "Add coordinates fields", None))
        self.ButtonBrowseShape.setText(_translate("AGTMagGridDialog", "browse", None))
        self.datFilechkbox.setText(_translate("AGTMagGridDialog", "Export also as .DAT", None))
        self.outputLabel.setText(_translate("AGTMagGridDialog", "Shapefile", None))
        self.medchk.setText(_translate("AGTMagGridDialog", "Median removal", None))
        self.percentilechk.setText(_translate("AGTMagGridDialog", "Percentile threshold", None))
        self.trendchk.setText(_translate("AGTMagGridDialog", "Trend removal", None))
        self.label_2.setText(_translate("AGTMagGridDialog", "Polynomial order", None))
        self.trendPercentileChk.setText(_translate("AGTMagGridDialog", "Percentile threshold", None))
        self.checkBox_geo.setText(_translate("AGTMagGridDialog", "Georeferencing", None))
        self.allProcess_button.setText(_translate("AGTMagGridDialog", "run", None))

