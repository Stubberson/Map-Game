import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from main_game_mode import MainPlayWidget
from interactive_map import InteractiveMap


class MainWidget(QtWidgets.QWidget):
    """
    Basic navigation and functionality of the game.
    The player can move onto playing one of the game modes or see the statistics
    of previous games.
    """
    def __init__(self):
        super().__init__()

        # Create the main layout for the stacked widgets
        main_layout = QtWidgets.QVBoxLayout()

        # Create the stacked widget
        self.stack = QtWidgets.QStackedWidget()

        # Create the widgets that will be stacked onto the stack
        self.main = QtWidgets.QWidget()
        self.play = QtWidgets.QWidget()
        self.interactive_map = QtWidgets.QWidget()

        # Create the layouts for the widgets to be added to the stack
        self.main_widget()
        self.play_widget()
        self.interactive_map_widget()

        # Add the created widgets to the stack
        self.stack.addWidget(self.main)
        self.stack.addWidget(self.play)
        self.stack.addWidget(self.interactive_map)

        # Add the stack into the main layout and set it as the layout
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

        # Timer for disabling a button
        self.main_timer = QtCore.QTimer()

        # Additional parameters for the main widget
        self.setWindowTitle("Map Guessing Game")
        self.setFixedHeight(700)  # Locks the height of the window for it to look ok

    def main_widget(self):
        """
        Adds the main widget, from which the player can choose to play the game
        or view the interactive map, to the stacked widget.
        """
        layout = QtWidgets.QVBoxLayout()

        # Basic info about the game
        info_label = QtWidgets.QLabel("Welcome!\n"
                                      "In the Play tab you can test your knowledge on European countries.\n"
                                      "Guess the country highlighted with its flag on the map.\n\n"
                                      "In the Interactive Map you can check the basic info of the countries by"
                                      " clicking a country.")
        info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Buttons for the main widget
        self.play_button = QtWidgets.QPushButton("Play", self)
        self.map_button = QtWidgets.QPushButton("Interactive Map", self)

        # Connections for the buttons
        self.play_button.clicked.connect(self.show_play)
        self.map_button.clicked.connect(self.show_map)

        # Add the buttons to the layout
        layout.addWidget(info_label)
        layout.addWidget(self.play_button)
        layout.addWidget(self.map_button)

        self.main.setLayout(layout)

    def play_widget(self):
        """ Creates and adds the play widget to the stack. """

        layout = QtWidgets.QVBoxLayout()
        info_layout = QtWidgets.QHBoxLayout()
        submit_layout = QtWidgets.QHBoxLayout()

        # Button to get back to the main widget
        self.p_back_button = QtWidgets.QPushButton(self)
        self.p_back_button.clicked.connect(self.back_from_play)
        # Set an arrow icon as the back button
        img = QtGui.QPixmap("GUI_items/back_arrow.png")
        icon = QtGui.QIcon(img)
        self.p_back_button.setIcon(icon)

        # Set a smaller size for the back button, so that it isn't in the way of the player
        self.p_back_button.setFixedSize(40, 40)
        self.p_back_button.setStyleSheet("background-color: rgba(0,0,0,0)")  # Background of the button is transparent

        # Add an input box for the user to guess the country and a submit button to submit the answer
        self.input_field = QtWidgets.QLineEdit()
        self.input_field.setPlaceholderText("Write your answer here...")
        self.submit_button = QtWidgets.QPushButton("Submit", self)
        submit_layout.addWidget(self.input_field)
        submit_layout.addWidget(self.submit_button)

        # Create the main mode object
        self.main_mode = MainPlayWidget()

        # Set a score label, so that the player sees how many points he has acquired
        self.score_label = QtWidgets.QLabel("Score: 0")
        self.score_label.setFixedSize(80, 20)
        info_layout.addWidget(self.score_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

        # Set an info label for possible warnings etc.
        self.info_label = QtWidgets.QLabel("")
        self.info_label.setFixedSize(150, 20)
        info_layout.addWidget(self.info_label, 0, QtCore.Qt.AlignmentFlag.AlignRight)

        self.submit_button.clicked.connect(self.get_input)

        # Add the widgets to the layout in the correct order
        layout.addWidget(self.p_back_button)
        layout.addLayout(info_layout)
        layout.addWidget(self.main_mode)
        layout.addLayout(submit_layout)

        self.play.setLayout(layout)

    def interactive_map_widget(self):
        """ Creates and adds the interactive map widget to the stack. """

        layout = QtWidgets.QVBoxLayout()

        # Button to get back to the main widget
        self.m_back_button = QtWidgets.QPushButton(self)
        self.m_back_button.clicked.connect(self.back_from_map)

        # Set an arrow icon as the back button
        img = QtGui.QPixmap("GUI_items/back_arrow.png")
        icon = QtGui.QIcon(img)
        self.m_back_button.setIcon(icon)

        self.m_back_button.setFixedSize(40, 40)
        self.m_back_button.setStyleSheet("background-color: rgba(0,0,0,0)")

        # Create the interactive map object
        self.map_object = InteractiveMap()

        # Add the widgets to the layout
        layout.addWidget(self.m_back_button)
        layout.addWidget(self.map_object)

        self.interactive_map.setLayout(layout)

    def show_play(self):
        """
        These "show_something" are for navigating the stack widget (to change between the welcoming widget,
        play widget, and map widget).
        """
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)

    def show_map(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 2)

    def back_from_play(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() - 1)

    def back_from_map(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() - 2)

    def get_stack_index(self):
        return self.stack.currentIndex()

    def get_input(self):
        """
        Get the player's guess for a country and check whether the answer was right or wrong.
        """
        guess = self.input_field.text()

        if guess != "":  # Only count a guess if it contains text, otherwise it's probably a misclick
            guesses = self.main_mode.get_number_guesses()  # Number of guesses the player has made

            self.info_label.setText(f"Guesses left: {3 - guesses}")

            guess = guess.lower()  # Lowercase for easier checking for the right answer
            self.input_field.clear()  # After the submit button has been clicked, clear the input field to guess again

            # Check if the input is the correct answer for the country
            answer = self.main_mode.check_answer(guess)
            if answer is True:
                self.info_label.setText("")  # Reset the info label if a right answer is given, or the guesses run out

            # Tie the score update to the pressing of the button
            self.update_score()

            # Disable the submit button when there are no more guesses left, and enable it again after that.
            countries_to_guess = self.main_mode.get_number_of_countries()
            country_count = self.main_mode.country_counter
            if guesses > 3 and country_count != countries_to_guess:
                self.submit_button.setEnabled(False)
                self.main_timer.singleShot(7000, self.enable_submit)

            # Disable the button for good when the game is over
            if country_count == countries_to_guess:
                self.submit_button.setEnabled(False)
        else:
            self.info_label.setText("Please make a guess!")

    def update_score(self):
        # Update the score and show it to the player
        score = self.main_mode.get_score()
        self.score_label.setText(f"Score: {score}")

    def enable_submit(self):
        self.submit_button.setEnabled(True)

