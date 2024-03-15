import sys
from PyQt6 import QtWidgets, QtGui, QtCore


class CountryOutlines(QtWidgets.QWidget):
    """
    A randomizer for which country's outlines to show in the basic game mode.
    *** AT THE MOMENT JUST A TEST

    """
    def __init__(self):
        super().__init__()

        suomi = QtGui.QPixmap("GUI_items/suomi.png")
        suomi = suomi.scaledToHeight(300)
        label_picture = QtWidgets.QLabel(self)  # creating a label for the picture
        label_picture.move(150, 20)
        label_picture.setPixmap(suomi)  # setting the picture to the label

