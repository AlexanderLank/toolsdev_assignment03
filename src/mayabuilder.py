import logging

import os
import pymel.core as pmc
from pymel.core.system import Path
import sys
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.cmds as cmds




sys.path.append( "C:/Users/Alexander/Desktop/Assets" )
log = logging.getLogger(__name__)


class BuildFile(object):
    """Class used to to represent a DCC software scene file
    The class will be a convenient object that we can use to manipulate our 
    scene files. Examples features include the ability to predefine our naming 
    conventions and automatically increment our versions.
    Attributes:
    dir (Path, optional): Directory to the scene file. Defaults to ''.
    descriptor (str, optional): Short descriptor of the scene file. 
    Defaults to "main".
    version (int, optional): Version number. Defaults to 1.
    ext (str, optional): Extension. Defaults to "ma"
    """

    def __init__(self, furnlist=[], numlist={}):
        """Initialises our attributes when class is instantiated.
        If the scene has not been saved, initialise the attributes based on 
        the defaults. Otherwise, if the scene is already saved, initialise 
        attributes based on the file name of the opened scene.
        """
        self.furnlist = furnlist
        self.numlist = numlist



    def uibuilder(self,layout):
        """does the work for the UI buttons"""

        self.filesearch()
        for item in self.furnlist:
            self.object_lay = QtWidgets.QHBoxLayout()

            self.numlist["Type{0}".format(self.furnlist.index(item))] = QtWidgets.QLineEdit()

            self.object_lay.addWidget(QtWidgets.QLabel(item))
            self.object_lay.addWidget(self.numlist["Type{0}".format(self.furnlist.index(item))])

            layout.addLayout(self.object_lay)



    def filesearch(self):
        """runs through the file to see how many furniture types we have, then put them in the list"""
        asset_folder = os.listdir('C:/Users/Alexander/Desktop/Assets')

        for file in asset_folder:
            # change the extension from '.mp3' to
            # the one of your choice.
            if file.endswith('.ma'):
                self.furnlist.append(file)





    def furnish(self, x, y):
        """Populates the room"""
        cmds.plane(p=(0, 0, 0), l=int(y)*2, w=int(x)*2, r=('90deg', '0deg', '0deg'))

        for item in self.furnlist:
            x = 0
            while x < int(self.numlist["Type{0}".format(self.furnlist.index(item))].text()):
                file_path = 'C:/Users/Alexander/Desktop/Assets/' + item
                cmds.file(file_path, i=True)

                x = x+1

        objectList = cmds.ls(geometry=True)
        for a in objectList:
            if a.find("controller") != -1:
                cmds.transform(randint(int(x)*-1,int(x)), randint(int(y)*-1, int(y)), a)