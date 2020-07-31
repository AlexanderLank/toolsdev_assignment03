import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

import mayabuilder

def maya_main_window():
	"""Return the maya main window widget"""
	main_window = omui.MQtUtil.mainWindow()
	return wrapInstance(long(main_window), QtWidgets.QWidget)


class RoomMakerUi(QtWidgets.QDialog):
	""" room maker ui class """

	def __init__(self):
		"""Constructor"""
		super(RoomMakerUi, self).__init__(parent=maya_main_window())
		self.scene = mayabuilder.BuildFile()

		self.setWindowTitle("Room Maker UI ")
		self.resize(500,200)
		self.setWindowFlags(self.windowFlags() ^
							QtCore.Qt.WindowContextHelpButtonHint)
		self.create_widgets()
		self.create_layout()
		self.create_connections()

	def create_widgets(self):
		"""Create widgets for our UI"""
		self.title_lbl = QtWidgets.QLabel("Build A Room")
		self.title_lbl.setStyleSheet("font: bold 40px")

		self.pln_lbl = QtWidgets.QLabel("Floor Size. x,y")
		self.plnx_le = QtWidgets.QLineEdit()
		self.plny_le = QtWidgets.QLineEdit()

		self.cancel_btn = QtWidgets.QPushButton("Cancel")
		self.generate_btn = QtWidgets.QPushButton("Generate")

	def create_layout(self):
		"""Lay out our widgets in the UI"""

		self.plane_lay = QtWidgets.QHBoxLayout()
		self.plane_lay.addWidget(self.pln_lbl)
		self.plane_lay.addWidget(self.plnx_le)
		self.plane_lay.addWidget(self.plny_le)

		self.bottom_btn_lay = QtWidgets.QHBoxLayout()
		self.bottom_btn_lay.addWidget(self.generate_btn)
		self.bottom_btn_lay.addWidget(self.cancel_btn)

		self.main_layout = QtWidgets.QVBoxLayout()
		self.main_layout.addWidget(self.title_lbl)
		self.main_layout.addLayout(self.plane_lay)

		self.scene.uibuilder(self.main_layout)

		self.main_layout.addStretch()
		self.main_layout.addLayout(self.bottom_btn_lay)


		self.setLayout(self.main_layout)

	def create_connections(self):
		"""Connect our widgets signals to slots"""
		self.cancel_btn.clicked.connect(self.cancel)
		self.generate_btn.clicked.connect(self.generate)
		"""self.generate_btn.clicked.connect(self.generate)"""

	def _populate_buildfile_properties(self):
		"""Populates the SceneFile object's properties from the UI"""


	@QtCore.Slot()
	def cancel(self):
		"""Quits the dialog"""
		self.close()

	def generate(self):
		self.scene.furnish(self.plnx_le.text(), self.plny_le.text())
		self.close()