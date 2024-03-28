import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from main_game_mode import MainPlayWidget


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
        self.stats = QtWidgets.QWidget()

        # Create the layouts for the widgets to be added to the stack
        self.main_widget()
        self.play_widget()
        self.stats_widget()

        # Add the created widgets to the stack
        self.stack.addWidget(self.main)
        self.stack.addWidget(self.play)
        self.stack.addWidget(self.stats)

        # Add the stack into the main layout and set it as the layout
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

        # Timer for disabling a button
        self.main_timer = QtCore.QTimer()

        # Additional parameters for the main widget
        self.setGeometry(300, 500, 500, 500)
        self.setWindowTitle("Map Guessing Game")

    def main_widget(self):
        """
        Adds the main widget, from which the player can choose to play the game
        or view the stats, to the stacked widget.
        """
        layout = QtWidgets.QVBoxLayout()

        # Buttons for the main widget
        play_button = QtWidgets.QPushButton("Play", self)
        stats_button = QtWidgets.QPushButton("Stats", self)

        # Connections for the buttons
        play_button.clicked.connect(self.show_play)
        stats_button.clicked.connect(self.show_stats)

        # Add the buttons to the layout
        layout.addWidget(play_button)
        layout.addWidget(stats_button)

        self.main.setLayout(layout)

    def play_widget(self):
        """ Creates and adds the play widget to the stack. """

        layout = QtWidgets.QVBoxLayout()

        # Button to get back to the main widget
        back_button = QtWidgets.QPushButton(self)
        back_button.clicked.connect(self.back_from_play)
        # Set an arrow icon as the back button
        img = QtGui.QPixmap("GUI_items/back_arrow.png")
        icon = QtGui.QIcon(img)
        back_button.setIcon(icon)

        # Set a smaller size for the back button, so that it isn't in the way of the player
        back_button.setFixedSize(40, 40)
        back_button.setStyleSheet("background-color: rgba(0,0,0,0)")  # Background of the button is transparent

        # Add an input box for the user to guess the country and a submit button to submit the answer
        self.input_field = QtWidgets.QLineEdit()
        self.submit_button = QtWidgets.QPushButton("Submit", self)

        # Create the main mode object
        self.main_mode = MainPlayWidget()

        # Set a score label, so that the player sees how many points he has acquired
        self.score_label = QtWidgets.QLabel(f"Score: 0")
        self.score_label.setFixedSize(60, 20)
        self.score_label.move(250, 50)

        self.submit_button.clicked.connect(self.get_input)

        # Add the widgets to the layout in the correct order
        layout.addWidget(back_button)
        layout.addWidget(self.score_label)
        layout.addWidget(self.main_mode)
        layout.addWidget(self.input_field)
        layout.addWidget(self.submit_button)

        self.play.setLayout(layout)

    def stats_widget(self):
        """ Creates and adds the stats widget to the stack. """

        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("STATS!")

        # Button to get back to the main widget
        back_button = QtWidgets.QPushButton(self)
        back_button.clicked.connect(self.back_from_stats)

        # Set an arrow icon as the back button
        img = QtGui.QPixmap("GUI_items/back_arrow.png")
        icon = QtGui.QIcon(img)
        back_button.setIcon(icon)

        back_button.setFixedSize(40, 40)
        back_button.setStyleSheet("background-color: rgba(0,0,0,0)")

        # Add the widgets to the layout
        layout.addWidget(back_button)
        layout.addWidget(label)

        self.stats.setLayout(layout)

    def show_play(self):
        """
        These "show_something" are for navigating the stack widget (to change between the welcoming widget,
        play widget, and stats widget).
        """
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)

    def show_stats(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 2)

    def back_from_play(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() - 1)

    def back_from_stats(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() - 2)

    def get_input(self):
        """
        Get the player's guess for a country and store it in a variable for checking whether the answer was
        right or wrong.
        """
        # The guess for the country
        guess = self.input_field.text()
        guess = guess.lower()  # Lowercase for easier checking for the right answer
        self.input_field.clear()  # After the submit button has been clicked, clear the input field to guess again

        # Check if the input is the correct answer for the country
        self.main_mode.check_answer(guess)

        # Tie the score update to the pressing of the button to make it recursive
        self.update_score()

        # Disable the submit button when there are no more guesses left, and enable it again after that.
        self.main_timer.timeout.connect(self.enable_submit)
        duration = self.main_mode.timer.remainingTime()  # The remaining time of the timer in MainWidget
        guesses = self.main_mode.get_guesses()
        if guesses > 3:
            self.submit_button.setEnabled(False)
            self.main_timer.start(duration)
        elif self.main_mode.country_counter == self.main_mode.get_number_of_countries():  # Disable the button for good
            self.submit_button.setEnabled(False)

    def update_score(self):
        # Update the score and show it to the player
        score = self.main_mode.get_score()
        self.score_label.setText(f"Score: {score}")

    def enable_submit(self):
        self.submit_button.setEnabled(True)

