# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mgao/Code/frds/frds/gui/ui_components/ui_files/MeasureSelectionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Measures(object):
    def setupUi(self, Measures):
        Measures.setObjectName("Measures")
        Measures.resize(909, 522)
        self.gridLayout_2 = QtWidgets.QGridLayout(Measures)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Measures)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxMeasures = QtWidgets.QGroupBox(Measures)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMeasures.sizePolicy().hasHeightForWidth())
        self.groupBoxMeasures.setSizePolicy(sizePolicy)
        self.groupBoxMeasures.setObjectName("groupBoxMeasures")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxMeasures)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutMeasures = QtWidgets.QVBoxLayout()
        self.verticalLayoutMeasures.setObjectName("verticalLayoutMeasures")
        self.checkBoxSelectAll = QtWidgets.QCheckBox(self.groupBoxMeasures)
        self.checkBoxSelectAll.setObjectName("checkBoxSelectAll")
        self.verticalLayoutMeasures.addWidget(self.checkBoxSelectAll)
        self.listWidgetMeasures = QtWidgets.QListWidget(self.groupBoxMeasures)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetMeasures.sizePolicy().hasHeightForWidth())
        self.listWidgetMeasures.setSizePolicy(sizePolicy)
        self.listWidgetMeasures.setObjectName("listWidgetMeasures")
        self.verticalLayoutMeasures.addWidget(self.listWidgetMeasures)
        self.verticalLayout.addLayout(self.verticalLayoutMeasures)
        self.gridLayout.addWidget(self.groupBoxMeasures, 0, 0, 1, 1)
        self.groupBoxDocumentation = QtWidgets.QGroupBox(Measures)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxDocumentation.sizePolicy().hasHeightForWidth())
        self.groupBoxDocumentation.setSizePolicy(sizePolicy)
        self.groupBoxDocumentation.setObjectName("groupBoxDocumentation")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxDocumentation)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBoxDocumentation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setMinimumSize(QtCore.QSize(400, 0))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setZoomFactor(0.85)
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout_4.addWidget(self.webEngineView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxDocumentation, 0, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Measures)
        self.buttonBox.rejected.connect(Measures.close)
        QtCore.QMetaObject.connectSlotsByName(Measures)

    def retranslateUi(self, Measures):
        _translate = QtCore.QCoreApplication.translate
        Measures.setWindowTitle(_translate("Measures", "Measures"))
        self.groupBoxMeasures.setTitle(_translate("Measures", "Measures"))
        self.checkBoxSelectAll.setText(_translate("Measures", "Select all"))
        self.groupBoxDocumentation.setTitle(_translate("Measures", "Documentation"))
from PyQt5 import QtWebEngineWidgets