import sys
import unittest
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtTest import QTest
from main_widget import MainWidget

app = QtWidgets.QApplication(sys.argv)  # Needed for the testing


class Tests(unittest.TestCase):

    def setUp(self):  # Sets up the main widget for testing
        self.stack_widget = MainWidget()

    def test_button_clicks(self):
        """ Tests that the buttons work for the main navigation. """
        if QTest.mouseClick(self.stack_widget.play_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 1)  # Play widget index = 1

        if QTest.mouseClick(self.stack_widget.map_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 2)  # Map widget index = 2

        if QTest.mouseClick(self.stack_widget.m_back_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 0)  # Main widget index = 0

        if QTest.mouseClick(self.stack_widget.p_back_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 0)  # Main widget index = 0


if __name__ == '__main__':
    unittest.main()
