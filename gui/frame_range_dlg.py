#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import os
import sys
from functools import partial

import xml.etree.ElementTree as ET
import lxml.etree as lxmlET

from gui import frame_range_dlg_ui


class FrameRangeDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(FrameRangeDialog, self).__init__(*args, **kwargs)

        self.ui = frame_range_dlg_ui.Ui_Dialog()
        self.ui.setupUi(self)

        # Handle findXML buttons
        self.sfs = [self.ui.sf_spinBox_488, self.ui.sf_spinBox_561,
                       self.ui.sf_spinBox_647, self.ui.sf_spinBox_750]
        self.efs = [self.ui.ef_spinBox_488, self.ui.ef_spinBox_561,
                        self.ui.ef_spinBox_647, self.ui.ef_spinBox_750]

        self.ui.okBtn.clicked.connect(self.send_params)
        self.ui.cancelBtn.clicked.connect(self.cancel)

    def send_params(self):

        sfs = []
        efs = []

        for sf, ef in zip(self.sfs, self.efs):
            sfs.append(sf.text())
            efs.append(ef.text())

        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText('Frame ranges are set!')
        msg.exec_()
        
        self.close() 

        return (sfs, efs)

    def cancel(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FrameRangeDialog()
    ex.show()
    app.exec_()
    sys.exit()
