import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QToolButton, QLineEdit, QApplication, QPushButton
import loi_physique as loi



##crée une classe widget

##class MyWidget(QtWidgets.QWidget):

    ##def __init__(self):
        ##super().__init__()

        ##self.button = QtWidgets.QPushButton("Click me!")
     ##self.text = QtWidgets.QLabel("Hello World",
                                 ##alignment=QtCore.Qt.AlignCenter)

       ## boutton_demarree = QToolButton()
       ## line_edit = QLineEdit()
      ##  boutton_demarree.clicked.connect(line_edit.clear)



      ##  self.layout = QtWidgets.QVBoxLayout(self)
       ## self.layout.addWidget(self.text)
      ##  self.layout.addWidget(self.button)



##if __name__=="__main__":
   ## app = QtWidgets.QApplication([])
   ## widget = MyWidget()
  ##  widget.resize(800, 600)
##widget.show()

   ## sys.exit(app.exec())



## boutton démarrer

boutton_demarree = QPushButton("Démarrer la simulation!")
if boutton_demarree.clicked :

   résultat = loi.equation(r=3,p=5,d=4,h=3)
   affichage_resultat_equation =



app = QApplication()
button = QPushButton("Call function")
button.clicked.connect(function)
button.show()
boutton_demarree.show()
sys.exit(app.exec())
#