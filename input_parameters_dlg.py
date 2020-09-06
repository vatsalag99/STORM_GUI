from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import os 
import sys
from functools import partial

import xml.etree.ElementTree as ET
import lxml.etree as lxmlET	

import input_parameters_dlg_ui

class InputParametersDialog(QDialog):
	def __init__(self, *args, **kwargs):
		super(InputParametersDialog, self).__init__(*args, **kwargs)
		

		self.ui = input_parameters_dlg_ui.Ui_Dialog()
		self.ui.setupUi(self)
		
		''' Add functionality '''
		# Handle findXML buttons 
		self.ui.find488.clicked.connect(partial(self.findXML, self.ui.pathLbl488))
		self.ui.find647.clicked.connect(partial(self.findXML, self.ui.pathLbl647))
		self.ui.find750.clicked.connect(partial(self.findXML, self.ui.pathLbl750))
		self.ui.find561.clicked.connect(partial(self.findXML, self.ui.pathLbl561))
		
		self.ui.updateBtn.clicked.connect(self.updateXML)
		
		self.labels = [self.ui.pathLbl488, self.ui.pathLbl561, self.ui.pathLbl647, self.ui.pathLbl750]
		self.threshs = [self.ui.thresh488, self.ui.thresh561, self.ui.thresh647, self.ui.thresh750]
	
	def findXML(self, label):
		options = QFileDialog.Options()
		options |=  QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", 
												  "","XML Files (*.xml)", 
												  options=options)
		if fileName:
			label.setText(fileName)
			print(label.text())

	def updateXML(self):
		
		for label, thresh in zip(self.labels, self.threshs):
		
			if label.text() is None:
				continue 
				
			print("Updating XML ", label.text())
			
			QMessageBox.about(self, "Success", "".format(label.text()))

			file_path = os.path.normpath(label.text())
			# Load in the XML file 
			if os.path.exists(file_path):
				tree = lxmlET.parse(file_path)
				root = tree.getroot()
			else:
				self.error_dialog = QErrorMessage()
				self.error_dialog.setWindowTitle("Error")
				self.error_dialog.showMessage('Please enter valid file path!')
				return

			# Second need to find necessary variables of interest that will be edited for each XML file
			for child in root:
				if child.tag == "start_frame":
					child.text = str(self.ui.sf.value())
					
				if child.tag == "end_frame":
					child.text = str(self.ui.ef.value())
					
				if child.tag == "threshold":
					child.text = str(thresh.value())

		tree.write(file_path)
		QMessageBox.about(self, "Success", "XMLs were succesfully updated!")
		self.close()

	
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = InputParametersDialog()
	ex.show()
	app.exec_()
	app.deleteLater()
	sys.exit()