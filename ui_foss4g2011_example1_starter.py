# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foss4g2011_example1_starter.ui'
#
# Created: Sun Sep 11 13:52:22 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_foss4g2011_example1_starter(object):
    def setupUi(self, foss4g2011_example1_starter):
        foss4g2011_example1_starter.setObjectName("foss4g2011_example1_starter")
        foss4g2011_example1_starter.resize(461, 514)
        self.buttonBox = QtGui.QDialogButtonBox(foss4g2011_example1_starter)
        self.buttonBox.setGeometry(QtCore.QRect(-30, 470, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.txtFeedback = QtGui.QTextBrowser(foss4g2011_example1_starter)
        self.txtFeedback.setGeometry(QtCore.QRect(10, 20, 441, 441))
        self.txtFeedback.setObjectName("txtFeedback")

        self.retranslateUi(foss4g2011_example1_starter)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), foss4g2011_example1_starter.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), foss4g2011_example1_starter.reject)
        QtCore.QMetaObject.connectSlotsByName(foss4g2011_example1_starter)

    def retranslateUi(self, foss4g2011_example1_starter):
        foss4g2011_example1_starter.setWindowTitle(QtGui.QApplication.translate("foss4g2011_example1_starter", "foss4g2011_example1_starter", None, QtGui.QApplication.UnicodeUTF8))

