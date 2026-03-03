import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox,
                               QCommandLinkButton, QDateTimeEdit, QDial,
                               QDialog, QDialogButtonBox, QFileSystemModel,
                               QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                               QLineEdit, QListView, QMenu, QPlainTextEdit,
                               QProgressBar, QPushButton, QRadioButton,
                               QScrollBar, QSizePolicy, QSlider, QSpinBox,
                               QStyleFactory, QTableWidget, QTabWidget,
                               QTextBrowser, QTextEdit, QToolBox, QToolButton,
                               QTreeView, QVBoxLayout, QWidget)

# fonctions utile pour gérer les widgets

def class_name(o):

    return o.metaObject().className()


def init_widget(w, name):

    w.setObjectName(name)
    w.setToolTip(class_name(w))


def style_names():

    default_style_name = QApplication.style().objectName().lower()
    result = []
    for style in QStyleFactory.keys():
        if style.lower() == default_style_name:
            result.insert(0, style)
        else:
            result.append(style)
    return result

def init_widget(w, name):

    w.setObjectName(name)
    w.setToolTip(class_name(w))





## classe qui contient tous les widgets

class WidgetGallery(QDialog):

   ##initie la fonction pour appeler soi-même

    def __init__(self):
        super().__init__()

        ##test combobox
        self._style_combobox = QComboBox()
        init_widget(self._style_combobox,"Ceci est une combobox")



    ## ajouter au layout
    top_layout.addWidget(self._style_combobox)
   #