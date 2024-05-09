import random
import os
from PyQt6 import QtWidgets, QtGui, QtCore
from countries_information import Country


class MainPlayWidget(QtWidgets.QWidget):
    """
    The main game mode. In it, a country is highlighted on the European map, and the player has four guesses to
    guess the country correctly. If the country cannot be guessed in those four guesses, the basic info is shown and
    another country to be guessed is rotated for the player.
    """
    def __init__(self):
        super().__init__()

        self.maps_folder = "GUI_items/interactive_map/countries"
        self.countries_paths = []
        self.country_widgets = []
        self.current_country = None  # The current country the player is guessing
        self.guess_counter = 0  # Counter to check how many guesses the player has taken
        self.points_counter = 0  # Count points for the player. Fewer points for more hints needed.

        self.create_country_widgets()  # Create the widgets to be shown

        # Shuffle widgets and the paths
        self.shuffled_widgets, self.shuffled_paths = self.shuffle_lists(self.country_widgets, self.countries_paths)

        self.label = QtWidgets.QLabel(self)  # A label for the picture
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Set alignment of the label
        font = QtGui.QFont("Courier", 12)  # Cool-ass font
        self.label.setFont(font)

        # Set up a timer for the player to be able to read some prompts
        self.timer = QtCore.QTimer()

        self.country_counter = 0  # Counter for changing the shown country outlines, check_answer method adds to it
        self.show_outlines()

    def create_country_widgets(self):
        # Paths to the outline files
        for file in os.listdir(self.maps_folder):
            country_path = os.path.join(self.maps_folder, file)
            if ".png" in country_path:  # MacOS can create a .DS_Store file into the directory. Ignore it
                self.countries_paths.append(country_path)

        # Create the image widgets from the files and add them to the list
        for country in self.countries_paths:
            image = QtGui.QPixmap(country)
            image = image.scaledToHeight(500)
            self.country_widgets.append(image)

    def shuffle_lists(self, widgets, paths):
        """
        Shuffles the widgets and paths lists so that the corresponding paths and widgets stay
        in the same positions.

        This is done so that the player doesn't always get the same countries in the same order to be
        guessed when he/she starts a new game.
        """
        # Generate a list of indices
        indices = list(range(len(widgets)))

        # Shuffle the indices
        random.shuffle(indices)

        # Use the shuffled indices to rearrange both lists similarly
        shuffled_widgets = [widgets[i] for i in indices]
        shuffled_paths = [paths[i] for i in indices]

        return shuffled_widgets, shuffled_paths

    def show_outlines(self):
        # Set a country to be highlighted
        self.guess_counter = 0  # Always reset the guess counter when a new country is to be guessed

        # Game over if no more countries to guess
        if self.country_counter == self.get_number_of_countries():
            self.game_over()
        else:
            self.label.setPixmap(self.shuffled_widgets[self.country_counter])

    def check_answer(self, guess):
        """ Check if the guess was correct or not. Show hints and update score accordingly. """
        self.current_country = self.get_current_country()
        self.guess_counter += 1

        # If the guess = current_country, the guess is correct. Otherwise, give another hint.
        if guess == self.current_country:
            self.round_points = 0  # For informing how many points the player got from a round

            if self.guess_counter == 1:
                self.points_counter += 6  # Most points for fewest number of guesses
                self.round_points = 6
            elif self.guess_counter == 2:
                self.points_counter += 4
                self.round_points = 4
            elif self.guess_counter == 3:
                self.points_counter += 2
                self.round_points = 2
            else:
                self.points_counter += 1
                self.round_points = 1

            self.country_counter += 1
            self.correct_answer()  # Show the player that the answer was correct, and how many points they got
            self.timer.singleShot(5000, self.show_outlines)  # Wait 5secs to congratulate the player and show the info
            return True
        elif guess != self.current_country and self.guess_counter == 1:
            self.label.setText("Incorrect!\nThe capital is " + Country(self.current_country).get_capital() + ".")
            return False
        elif guess != self.current_country and self.guess_counter == 2:
            self.label.setText("Incorrect!\nThe population is " + Country(self.current_country).get_population() + " million.")
            return False
        elif guess != self.current_country and self.guess_counter == 3:
            self.label.setText("Incorrect!\nThe neighboring countries are " + Country(self.current_country).get_neighbors() + ".")
            return False
        elif guess != self.current_country and self.guess_counter == 4:
            # Show the information of the country if the player cannot guess it in 4 guesses, and move on. No points.
            self.show_country_information()
            self.country_counter += 1
            self.timer.singleShot(7000, self.show_outlines)  # 7 seconds timer
            return True

    def correct_answer(self):
        self.label.setText(f"Correct! You scored {self.round_points} point(s)!\n" +
                           Country(self.current_country).__str__() +
                           f"\n\nRemaining countries to guess: {self.get_number_of_countries() - self.country_counter}")

    def show_country_information(self):
        """ After too many guesses, the country's information is given to the player. """
        self.label.setText("Out of guesses!\n" + Country(self.current_country).__str__() +
                           f"\n\nRemaining countries to guess: {self.get_number_of_countries() - self.country_counter}")

    def game_over(self):
        """ When there are no more countries to be guessed, end the game and show the scores to the player. """
        self.label.setText(f"End of the game.\nYou scored {self.get_score()} points!")

    def get_number_guesses(self):
        return self.guess_counter

    def get_score(self):
        return self.points_counter

    def get_current_path(self):
        return self.shuffled_paths[self.country_counter]

    def get_current_country(self):
        correct_answer_path = self.get_current_path()  # Get the correct current_country's path
        split_path = correct_answer_path.rsplit("/")  # 3rd item is the country name + file type (e.g. finland.png)
        current_country = split_path[3]
        current_country = current_country.rsplit(".")[0]
        return current_country

    def get_number_of_countries(self):
        return len(self.country_widgets)

