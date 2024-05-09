import sys
import random
import unittest
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtTest import QTest

from main_widget import MainWidget
from main_game_mode import MainPlayWidget
from interactive_map import InteractiveMap

app = QtWidgets.QApplication(sys.argv)  # Needed for the testing


class Tests(unittest.TestCase):

    def setUp(self):  # Sets up the modules/widgets for testing
        self.stack_widget = MainWidget()
        self.play_widget = MainPlayWidget()
        self.map = InteractiveMap()

    def test_main_nav(self):
        """ Tests that the buttons work for the main navigation. """
        if QTest.mouseClick(self.stack_widget.play_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 1)  # Play widget index = 1

        if QTest.mouseClick(self.stack_widget.map_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 2)  # Map widget index = 2

        if QTest.mouseClick(self.stack_widget.m_back_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 0)  # Main widget index = 0

        if QTest.mouseClick(self.stack_widget.p_back_button, QtCore.Qt.MouseButton.LeftButton):
            self.assertTrue(self.stack_widget.get_stack_index() == 0)  # Main widget index = 0

    def test_correct_answer_scoring(self):
        """ Test that the player gets the right number of points for his/her right answer. """
        answer = self.play_widget.get_current_country()  # The current country to be guessed

        # Simulate the number of the guess to check the scoring
        random_number = random.randint(0, 3)  # Running the function check_answer() adds one, so range = 0-3
        self.play_widget.guess_counter = random_number

        if self.play_widget.check_answer(answer):
            if self.play_widget.guess_counter == 1:
                self.assertTrue(self.play_widget.points_counter == 6)
            elif self.play_widget.guess_counter == 2:
                self.assertTrue(self.play_widget.points_counter == 4)
            elif self.play_widget.guess_counter == 3:
                self.assertTrue(self.play_widget.points_counter == 2)
            else:
                self.assertTrue(self.play_widget.points_counter == 1)

    def test_incorrect_answer_scoring(self):
        """ Test that the player gets no points for his/her wrong answer. """
        if self.play_widget.check_answer("Not a country"):
            self.assertTrue(self.play_widget.points_counter == 0)

    def test_interactive_map(self):
        """ Test that the correct info is displayed in the interactive map. """
        regions = ["denmark", "russia", "finland", "sweden", "poland", "spain", "portugal"]  # Subset of the countries
        random_region = random.choice(regions)
        message_box = self.map.info_box

        self.map.display_region_info(random_region)  # Run the display_region_info() function with the random region

        # Check if the message box contains the country in question
        self.assertEqual(message_box.text(), random_region.capitalize())


if __name__ == '__main__':
    unittest.main()
