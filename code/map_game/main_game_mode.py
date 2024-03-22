import sys
import random
import os
from PyQt6 import QtWidgets, QtGui, QtCore


class CountryOutlines(QtWidgets.QWidget):
    """
    A randomizer for the country outlines to show in the basic game mode.

    """
    def __init__(self):
        super().__init__()

        self.maps_folder = "GUI_items/country_outlines"
        self.countries_paths = []
        self.country_widgets = []
        self.current_country = None  # The current country the player is guessing

        self.create_country_widgets()

        # Shuffle widgets and the paths
        self.shuffled_widgets, self.shuffled_paths = self.shuffle_lists(self.country_widgets, self.countries_paths)

        self.label = QtWidgets.QLabel(self)  # A label for the picture
        self.label.setGeometry(125, 0, 500, 300)

        self.i = 0  # Counter for changing the shown country outlines, check_answer function adds to it
        self.show_outlines()

    def create_country_widgets(self):
        # Paths to the outline files
        for file in os.listdir(self.maps_folder):
            country_path = os.path.join(self.maps_folder, file)
            if ".png" in country_path:  # MacOS creates a .DS_Store file into a directory automatically. Ignore it.
                self.countries_paths.append(country_path)

        # Create the image widgets from the files and add them to the list
        for country in self.countries_paths:
            image = QtGui.QPixmap(country)
            image = image.scaledToHeight(300)
            self.country_widgets.append(image)

    def shuffle_lists(self, widgets, paths):
        """
        Shuffles the widgets and paths lists so that the corresponding paths and widgets stay
        in the same positions.

        This is done so that the player doesn't always get the same countries in the same order to be
        guessed when he/she starts a new game.

        This way it's also possible to check if the guess of the player has been correct or not.
        """
        # Generate a list of indices
        indices = list(range(len(widgets)))

        # Shuffle the indices
        random.shuffle(indices)

        # Use the shuffled indices to rearrange both lists simultaneously
        shuffled_widgets = [widgets[i] for i in indices]
        shuffled_paths = [paths[i] for i in indices]

        return shuffled_widgets, shuffled_paths

    def show_outlines(self):
        # Set a country's outlines as the picture to be shown
        self.label.setPixmap(self.shuffled_widgets[self.i])

    def check_answer(self, guess):
        """Check if the guess was correct or not"""

        correct_answer_path = self.get_current_path()  # Get the correct current_country's path
        split_path = correct_answer_path.rsplit("/")  # 3rd item is the country name + file type (e.g. finland.png)
        current_country = split_path[2]
        self.current_country = current_country.rsplit(".")[0]

        # If the guess = current_country, the guess is correct. Next country can be shown.
        if guess == self.current_country:
            print("CORRECT!", len(self.shuffled_widgets), self.i)
            if self.i < len(self.shuffled_widgets) - 1:  # Only add to the counter if there are countries left to guess
                self.i += 1
                self.show_outlines()
        else:
            print("INCORRECT!")
            self.label.setText("Incorrect!\n" + self.get_capital())

    def get_capital(self):
        """ If the first guess for the country goes wrong, gives the country's capital as hint. """

        capitals_list = ["Helsinki", "Stockholm", "Oslo"]
        string = "This country's capital is "

        if self.current_country == "finland":
            return string + capitals_list[0] + "."
        elif self.current_country == "sweden":
            return string + capitals_list[1] + "."
        elif self.current_country == "norway":
            return string + capitals_list[2] + "."

    def get_current_path(self):
        return self.shuffled_paths[self.i]

    def get_current_country(self):
        return self.current_country

