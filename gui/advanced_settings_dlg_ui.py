# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advanced_settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 296)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout750 = QtWidgets.QGridLayout()
        self.gridLayout750.setObjectName("gridLayout750")
        self.label_9 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{color: rgb(170, 0, 0)}")
        self.label_9.setObjectName("label_9")
        self.gridLayout750.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout750.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout750.addWidget(self.label, 1, 0, 1, 1)
        self.ef750 = QtWidgets.QSpinBox(Dialog)
        self.ef750.setObjectName("ef750")
        self.ef750.setMaximum(100000)
        self.gridLayout750.addWidget(self.ef750, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout750.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout750.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout750.addWidget(self.label_5, 5, 0, 1, 1)
        self.sf750 = QtWidgets.QSpinBox(Dialog)
        self.sf750.setObjectName("sf750")
        self.sf750.setMaximum(100000)
        self.gridLayout750.addWidget(self.sf750, 1, 1, 1, 1)
        self.bs750 = QtWidgets.QDoubleSpinBox(Dialog)
        self.bs750.setObjectName("bs750")
        self.gridLayout750.addWidget(self.bs750, 3, 1, 1, 1)
        self.fs750 = QtWidgets.QDoubleSpinBox(Dialog)
        self.fs750.setObjectName("fs750")
        self.gridLayout750.addWidget(self.fs750, 4, 1, 1, 1)
        self.pathLbl750 = QtWidgets.QLabel(Dialog)
        self.pathLbl750.setStyleSheet("QLabel{background-color: \'gray\'}")
        self.pathLbl750.setText("")
        self.pathLbl750.setObjectName("pathLbl750")
        self.gridLayout750.addWidget(self.pathLbl750, 9, 0, 1, 2)
        self.psf750 = QtWidgets.QDoubleSpinBox(Dialog)
        self.psf750.setObjectName("psf750")
        self.gridLayout750.addWidget(self.psf750, 6, 1, 1, 1)
        self.checkBox750 = QtWidgets.QCheckBox(Dialog)
        self.checkBox750.setObjectName("checkBox750")
        self.gridLayout750.addWidget(self.checkBox750, 7, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout750.addWidget(self.label_6, 6, 0, 1, 1)
        self.thresh750 = QtWidgets.QDoubleSpinBox(Dialog)
        self.thresh750.setObjectName("thresh750")
        self.gridLayout750.addWidget(self.thresh750, 5, 1, 1, 1)
        self.find750 = QtWidgets.QPushButton(Dialog)
        self.find750.setObjectName("find750")
        self.gridLayout750.addWidget(self.find750, 8, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout750, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 0, 1, 1, 1)
        self.gridLayout647 = QtWidgets.QGridLayout()
        self.gridLayout647.setObjectName("gridLayout647")
        self.label_10 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{color: rgb(255,85, 0)}")
        self.label_10.setObjectName("label_10")
        self.gridLayout647.addWidget(self.label_10, 0, 0, 1, 1)
        self.bs647 = QtWidgets.QDoubleSpinBox(Dialog)
        self.bs647.setObjectName("bs647")
        self.gridLayout647.addWidget(self.bs647, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.gridLayout647.addWidget(self.label_14, 4, 0, 1, 1)
        self.fs647 = QtWidgets.QDoubleSpinBox(Dialog)
        self.fs647.setObjectName("fs647")
        self.gridLayout647.addWidget(self.fs647, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setObjectName("label_16")
        self.gridLayout647.addWidget(self.label_16, 5, 0, 1, 1)
        self.thresh647 = QtWidgets.QDoubleSpinBox(Dialog)
        self.thresh647.setObjectName("thresh647")
        self.gridLayout647.addWidget(self.thresh647, 5, 1, 1, 1)
        self.sf647 = QtWidgets.QSpinBox(Dialog)
        self.sf647.setObjectName("sf647")
        self.sf647.setMaximum(100000)
        self.gridLayout647.addWidget(self.sf647, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self.gridLayout647.addWidget(self.label_18, 2, 0, 1, 1)
        self.ef647 = QtWidgets.QSpinBox(Dialog)
        self.ef647.setObjectName("ef647")
        self.ef647.setMaximum(100000)
        self.gridLayout647.addWidget(self.ef647, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setObjectName("label_17")
        self.gridLayout647.addWidget(self.label_17, 3, 0, 1, 1)
        self.pathLbl647 = QtWidgets.QLabel(Dialog)
        self.pathLbl647.setStyleSheet("QLabel{background-color: \'gray\'}")
        self.pathLbl647.setText("")
        self.pathLbl647.setObjectName("pathLbl647")
        self.gridLayout647.addWidget(self.pathLbl647, 9, 0, 1, 2)
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setObjectName("label_19")
        self.gridLayout647.addWidget(self.label_19, 6, 0, 1, 1)
        self.psf647 = QtWidgets.QDoubleSpinBox(Dialog)
        self.psf647.setObjectName("psf647")
        self.gridLayout647.addWidget(self.psf647, 6, 1, 1, 1)
        self.checkBox647 = QtWidgets.QCheckBox(Dialog)
        self.checkBox647.setObjectName("checkBox647")
        self.gridLayout647.addWidget(self.checkBox647, 7, 0, 1, 1)
        self.find647 = QtWidgets.QPushButton(Dialog)
        self.find647.setObjectName("find647")
        self.gridLayout647.addWidget(self.find647, 8, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.gridLayout647.addWidget(self.label_13, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout647, 0, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 0, 3, 1, 1)
        self.gridLayout561 = QtWidgets.QGridLayout()
        self.gridLayout561.setObjectName("gridLayout561")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setObjectName("label_24")
        self.gridLayout561.addWidget(self.label_24, 5, 0, 1, 1)
        self.bs561 = QtWidgets.QDoubleSpinBox(Dialog)
        self.bs561.setObjectName("bs561")
        self.gridLayout561.addWidget(self.bs561, 3, 1, 1, 1)
        self.sf561 = QtWidgets.QSpinBox(Dialog)
        self.sf561.setObjectName("sf561")
        self.sf561.setMaximum(100000)
        self.gridLayout561.addWidget(self.sf561, 1, 1, 1, 1)
        self.thresh561 = QtWidgets.QDoubleSpinBox(Dialog)
        self.thresh561.setObjectName("thresh561")
        self.gridLayout561.addWidget(self.thresh561, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel{color: rgb(255, 255, 0)}")
        self.label_11.setObjectName("label_11")
        self.gridLayout561.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setObjectName("label_25")
        self.gridLayout561.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setObjectName("label_27")
        self.gridLayout561.addWidget(self.label_27, 6, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setObjectName("label_26")
        self.gridLayout561.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setObjectName("label_15")
        self.gridLayout561.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setObjectName("label_22")
        self.gridLayout561.addWidget(self.label_22, 4, 0, 1, 1)
        self.ef561 = QtWidgets.QSpinBox(Dialog)
        self.ef561.setObjectName("ef561")
        self.ef561.setMaximum(100000)
        self.gridLayout561.addWidget(self.ef561, 2, 1, 1, 1)
        self.fs561 = QtWidgets.QDoubleSpinBox(Dialog)
        self.fs561.setObjectName("fs561")
        self.gridLayout561.addWidget(self.fs561, 4, 1, 1, 1)
        self.psf561 = QtWidgets.QDoubleSpinBox(Dialog)
        self.psf561.setObjectName("psf561")
        self.gridLayout561.addWidget(self.psf561, 6, 1, 1, 1)
        self.find561 = QtWidgets.QPushButton(Dialog)
        self.find561.setObjectName("find561")
        self.gridLayout561.addWidget(self.find561, 8, 0, 1, 1)
        self.pathLbl561 = QtWidgets.QLabel(Dialog)
        self.pathLbl561.setStyleSheet("QLabel{background-color: \'gray\'}")
        self.pathLbl561.setText("")
        self.pathLbl561.setObjectName("pathLbl561")
        self.gridLayout561.addWidget(self.pathLbl561, 9, 0, 1, 2)
        self.checkBox561 = QtWidgets.QCheckBox(Dialog)
        self.checkBox561.setObjectName("checkBox561")
        self.gridLayout561.addWidget(self.checkBox561, 7, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout561, 0, 4, 1, 1)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 0, 5, 1, 1)
        self.gridLayout488 = QtWidgets.QGridLayout()
        self.gridLayout488.setObjectName("gridLayout488")
        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setObjectName("label_34")
        self.gridLayout488.addWidget(self.label_34, 3, 0, 1, 1)
        self.bs488 = QtWidgets.QDoubleSpinBox(Dialog)
        self.bs488.setObjectName("bs488")
        self.gridLayout488.addWidget(self.bs488, 3, 1, 1, 1)
        self.thresh488 = QtWidgets.QDoubleSpinBox(Dialog)
        self.thresh488.setObjectName("thresh488")
        self.gridLayout488.addWidget(self.thresh488, 5, 1, 1, 1)
        self.checkBox488 = QtWidgets.QCheckBox(Dialog)
        self.checkBox488.setObjectName("checkBox488")
        self.gridLayout488.addWidget(self.checkBox488, 7, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setObjectName("label_31")
        self.gridLayout488.addWidget(self.label_31, 4, 0, 1, 1)
        self.find488 = QtWidgets.QPushButton(Dialog)
        self.find488.setObjectName("find488")
        self.gridLayout488.addWidget(self.find488, 8, 0, 1, 1)
        self.sf488 = QtWidgets.QSpinBox(Dialog)
        self.sf488.setObjectName("sf488")
        self.sf488.setMaximum(100000)
        self.gridLayout488.addWidget(self.sf488, 1, 1, 1, 1)
        self.fs488 = QtWidgets.QDoubleSpinBox(Dialog)
        self.fs488.setObjectName("fs488")
        self.gridLayout488.addWidget(self.fs488, 4, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setObjectName("label_36")
        self.gridLayout488.addWidget(self.label_36, 6, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setObjectName("label_35")
        self.gridLayout488.addWidget(self.label_35, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{color: \'blue\'}")
        self.label_12.setObjectName("label_12")
        self.gridLayout488.addWidget(self.label_12, 0, 0, 1, 1)
        self.ef488 = QtWidgets.QSpinBox(Dialog)
        self.ef488.setObjectName("ef488")
        self.ef488.setMaximum(100000)
        self.gridLayout488.addWidget(self.ef488, 2, 1, 1, 1)
        self.pathLbl488 = QtWidgets.QLabel(Dialog)
        self.pathLbl488.setStyleSheet("QLabel{background-color: \'gray\'}")
        self.pathLbl488.setText("")
        self.pathLbl488.setObjectName("pathLbl488")
        self.gridLayout488.addWidget(self.pathLbl488, 9, 0, 1, 2)
        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setObjectName("label_33")
        self.gridLayout488.addWidget(self.label_33, 5, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setObjectName("label_30")
        self.gridLayout488.addWidget(self.label_30, 1, 0, 1, 1)
        self.psf488 = QtWidgets.QDoubleSpinBox(Dialog)
        self.psf488.setObjectName("psf488")
        self.gridLayout488.addWidget(self.psf488, 6, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout488, 0, 6, 1, 1)
        self.updateBtn = QtWidgets.QPushButton(Dialog)
        self.updateBtn.setObjectName("updateBtn")
        self.gridLayout_5.addWidget(self.updateBtn, 1, 0, 1, 7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Advanced Settings"))
        self.label_9.setText(_translate("Dialog", "750"))
        self.label_2.setText(_translate("Dialog", "End Frame"))
        self.label.setText(_translate("Dialog", "Start Frame "))
        self.label_3.setText(_translate("Dialog", "Background Sigma"))
        self.label_4.setText(_translate("Dialog", "Foreground Sigma"))
        self.label_5.setText(_translate("Dialog", "Threshold"))
        self.checkBox750.setText(_translate("Dialog", "Drift Correction"))
        self.label_6.setText(_translate("Dialog", "Initial PSF"))
        self.find750.setText(_translate("Dialog", "Find XML"))
        self.label_10.setText(_translate("Dialog", "647"))
        self.label_14.setText(_translate("Dialog", "Foreground Sigma"))
        self.label_16.setText(_translate("Dialog", "Threshold"))
        self.label_18.setText(_translate("Dialog", "End Frame"))
        self.label_17.setText(_translate("Dialog", "Background Sigma"))
        self.label_19.setText(_translate("Dialog", "Initial PSF"))
        self.checkBox647.setText(_translate("Dialog", "Drift Correction"))
        self.find647.setText(_translate("Dialog", "Find XML"))
        self.label_13.setText(_translate("Dialog", "Start Frame "))
        self.label_24.setText(_translate("Dialog", "Threshold"))
        self.label_11.setText(_translate("Dialog", "561"))
        self.label_25.setText(_translate("Dialog", "Background Sigma"))
        self.label_27.setText(_translate("Dialog", "Initial PSF"))
        self.label_26.setText(_translate("Dialog", "End Frame"))
        self.label_15.setText(_translate("Dialog", "Start Frame "))
        self.label_22.setText(_translate("Dialog", "Foreground Sigma"))
        self.find561.setText(_translate("Dialog", "Find XML"))
        self.checkBox561.setText(_translate("Dialog", "Drift Correction"))
        self.label_34.setText(_translate("Dialog", "Background Sigma"))
        self.checkBox488.setText(_translate("Dialog", "Drift Correction"))
        self.label_31.setText(_translate("Dialog", "Foreground Sigma"))
        self.find488.setText(_translate("Dialog", "Find XML"))
        self.label_36.setText(_translate("Dialog", "Initial PSF"))
        self.label_35.setText(_translate("Dialog", "End Frame"))
        self.label_12.setText(_translate("Dialog", "488"))
        self.label_33.setText(_translate("Dialog", "Threshold"))
        self.label_30.setText(_translate("Dialog", "Start Frame "))
        self.updateBtn.setText(_translate("Dialog", "Update XMLs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

