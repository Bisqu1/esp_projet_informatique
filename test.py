# Example file showing a circle moving on screen
#import pygame

import random
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MainWindow(QWidget):
   def __init__(self):
      super().__init__()

      self.setWindowTitle('PyQt Label Widget')
      self.setGeometry(100, 100, 320, 210)

      label = QLabel('This is a QLabel widget')

      layout = QVBoxLayout()
      layout.addWidget(label)
      self.setLayout(layout)

      self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   sys.exit(app.exec())

#from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
#import sys
#
#app = QApplication(sys.argv)
#window = QMainWindow()
#window.setGeometry(100, 100, 600, 400) # Sets main window position and dimension
#
#spin_box = QSpinBox(window) # Parent is the main window
#spin_box.setGeometry(50, 50, 1500, 300) # Sets the spin box at x=50, y=50 with width=150, height=30
#
#window.show()
#sys.exit(app.exec_())



#################TEST-INI-PYQT###############################
#class MyWidget(QtWidgets.QWidget):
#    def __init__(self):
#        super().__init__()
#
#        #self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#        #self.button = QtWidgets.QPushButton("Click me!")
#        #self.text = QtWidgets.QLabel("Hello World",
#        #                             alignment=QtCore.Qt.AlignCenter)
#        #self.butotn= QtWidgets.QSpinBox()
#
#        #self.layout = QtWidgets.QVBoxLayout(self)
#        #self.layout.addWidget(self.text)
#        #self.layout.addWidget(self.button)
#        #self.layout.addWidget(self.butotn)
#        #self.button.clicked.connect(self.magic)
#
#    @QtCore.Slot()
#    def magic(self):
#        self.text.setText(random.choice(self.hello))
#
#
#if __name__ == "__main__":
#    app = QtWidgets.QApplication([])
#
#    widget = MyWidget()
#    widget.resize(800, 600)
#    widget.show()
#
#    sys.exit(app.exec())


######################PYGAME###################################
#
## pygame setup
#pygame.init()
#screen = pygame.display.set_mode((1280, 720))
#clock = pygame.time.Clock()
#running = True
#dt = 0
#
#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
#while running:
#    # poll for events
#    # pygame.QUIT event means the user clicked X to close your window
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#
#    # fill the screen with a color to wipe away anything from last frame
#    screen.fill("green")
#
#    pygame.draw.circle(screen, "red", player_pos, 40)
#
#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_w]:
#        player_pos.y -= 300 * dt
#    if keys[pygame.K_s]:
#        player_pos.y += 300 * dt
#    if keys[pygame.K_a]:
#        player_pos.x -= 300 * dt
#    if keys[pygame.K_d]:
#        player_pos.x += 300 * dt
#
#    # flip() the display to put your work on screen
#    pygame.display.flip()
#
#    # limits FPS to 60
#    # dt is delta time in seconds since last frame, used for framerate-
#    # independent physics.
#    dt = clock.tick(60) / 1000
#
#pygame.quit()