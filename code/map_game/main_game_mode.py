import sys
import random
import os
from PyQt6 import QtWidgets, QtGui, QtCore
from countries_information import Country


class MainPlayWidget(QtWidgets.QWidget):
    """
    The main mode of the map guessing game.

    """
    def __init__(self):
        super().__init__()

        self.maps_folder = "GUI_items/country_outlines"
        self.countries_paths = []
        self.country_widgets = []
        self.current_country = None  # The current country the player is guessing
        self.guess_counter = 0  # Counter to check how many guesses the player has taken
        self.points_counter = 0  # Count points for the player. Fewer points for more hints needed.

        self.create_country_widgets()  # Create the widgets to be shown

        # Shuffle widgets and the paths
        self.shuffled_widgets, self.shuffled_paths = self.shuffle_lists(self.country_widgets, self.countries_paths)

        self.label = QtWidgets.QLabel(self)  # A label for the picture
        self.label.setGeometry(0, 0, 420, 300)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Set alignment of the label

        # Set up a timer for the player to be able to read the info before moving onto the next country
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)

        self.country_counter = 0  # Counter for changing the shown country outlines, check_answer method adds to it
        self.show_outlines()

    def create_country_widgets(self):
        # Paths to the outline files
        for file in os.listdir(self.maps_folder):
            country_path = os.path.join(self.maps_folder, file)
            if ".png" in country_path:  # MacOS creates a .DS_Store file into the directory. Ignore it and other folders
                self.countries_paths.append(country_path)

        # Create the image widgets from the files and add them to the list
        for country in self.countries_paths:
            image = QtGui.QPixmap(country)
            image = image.scaledToHeight(250)
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
        self.guess_counter = 0  # Always reset the guess counter when a new country is to be guessed

        # Game over if no more countries to be guessed
        if self.country_counter == self.get_number_of_countries():
            self.game_over()
        else:
            self.label.setPixmap(self.shuffled_widgets[self.country_counter])

    def check_answer(self, guess):
        """ Check if the guess was correct or not. Show hints and update score accordingly. """

        correct_answer_path = self.get_current_path()  # Get the correct current_country's path
        split_path = correct_answer_path.rsplit("/")  # 3rd item is the country name + file type (e.g. finland.png)
        current_country = split_path[2]
        self.current_country = current_country.rsplit(".")[0]
        self.guess_counter += 1

        # If the guess = current_country, the guess is correct. Otherwise, give another hint.
        if guess == self.current_country:
            if self.country_counter <= len(self.country_widgets) - 1:  # Only add to the counter if countries to guess
                if self.guess_counter == 1:
                    self.points_counter += 5  # Most points for fewest number of guesses
                elif self.guess_counter == 2:
                    self.points_counter += 3
                elif self.guess_counter == 3:
                    self.points_counter += 1
                self.country_counter += 1
                self.show_outlines()
        elif guess != self.current_country and self.guess_counter == 1:
            self.label.setText("Incorrect!\nThe capital is " + Country(self.current_country).get_capital())
        elif guess != self.current_country and self.guess_counter == 2:
            self.label.setText("Incorrect!\nThe population is " + Country(self.current_country).get_population() + " million")
        elif guess != self.current_country and self.guess_counter == 3:
            self.label.setText("Incorrect!\nThe neighboring countries are " + Country(self.current_country).get_neighbors())
        elif self.guess_counter > 3:
            # Show the information of the country if the player cannot guess it in 3 guesses, and move on
            self.show_country_information()
            self.country_counter += 1

            self.timer.start(7000)  # 7 seconds timer
            self.timer.timeout.connect(self.show_outlines)  # Displays the next country after the time has passed

    def show_country_information(self):
        """ After too many guesses, the country's information is given to the player. """
        self.label.setText("Out of guesses!\n" + Country(self.current_country).__str__())

    def game_over(self):
        """ When there are no more countries to be guessed, end the game and show the scores to the player. """
        print("GAME OVER")
        self.label.setText(f"End of the game!\nYou scored {self.get_score()} points!")

    def get_guesses(self):
        return self.guess_counter

    def get_score(self):
        return self.points_counter

    def get_current_path(self):
        return self.shuffled_paths[self.country_counter]

    def get_current_country(self):
        return self.current_country

    def get_number_of_countries(self):
        return len(self.country_widgets)

