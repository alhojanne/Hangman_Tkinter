"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
13.10 Projekti: Graafinen käyttöliittymä
Student Id: 1902430
Name:       Janne Alho
Email:      janne.alho@tuni.fi

How to use:
The program is very simple. To play the game you:
1. Press 'Get a new word'-button
2. Try to guess the word by choosing letters 1 by 1
3. After 5 wrong guesses you lose
4. Repeat from 1
"""
# Import:
# Everything from tkinter to make a GUI.
# randrange from random to get a random integer needed in the game.
# ascii_uppercase from string to easily make a list of alphabets.
from tkinter import *
from random import randrange
from string import ascii_uppercase

# List of uppercase alphabets:
ALPHABETS = list(ascii_uppercase)


class HangmanGame:
    def __init__(self):
        """
        init-method for the HangmanGame-class. Method initializes
        necessary attributes and creates a virtual keyboard for
        the inputs in the game.
        """
        self.__main_window = Tk()
        self.__main_window.title("Hangman")
        self.__word_to_guess = ""
        self.__wrong_answers = 0

        # Lists for storing the buttons and their commands used
        # in the virtual keyboard.
        self.__letter_buttons = []
        self.__letter_commands = []

        # Virtual keyboard and the commands are created in a loop
        # and placed on a grid. They are also stored to corresponding
        # lists.
        for i in range(len(ALPHABETS)):

            def button_command(index=i):
                self.enter_character(index)

            self.__letter_commands.append(button_command)

            new_button = Button(
                self.__main_window, text=ALPHABETS[i], command=button_command
            )
            if i < 9:
                button_row = 4
                column = i
            elif i < 18:
                button_row = 5
                column = i - 9
            else:
                button_row = 6
                column = i - 18
            new_button.grid(column=column, row=button_row)

            self.__letter_buttons.append(new_button)

        # Buttons for getting a new word and a label
        # where the word is presented
        self.__get_word_button = Button(command=self.get_word, text="Get a new word")
        self.__get_word_button.grid(column=0, columnspan=30, row=0)

        self.__word_to_guess_label = Label(text="")
        self.__word_to_guess_label.grid(column=0, columnspan=12, row=1)

        self.__wrong_answer_label = Label(text=f"{5-self.__wrong_answers} tries left")
        self.__wrong_answer_label.grid(column=0, columnspan=30, row=2)

        self.__main_window.mainloop()

    def enter_character(self, index):
        """
        Method is used to enter the letter from the virtual keyboard

        :param index: int, has a default value of 0-25 depending on which key is pressed on the virtual keyboard.
        """
        letters_found = 0
        # Check if the entered key is in the word being guessed.
        # if key is found, it is placed on the corresponding position
        # in the word_placeholder_list.
        for i in range(len(self.__word_to_guess)):
            if self.__word_to_guess[i] == ALPHABETS[index]:
                letters_found += 1
                # place_holder_list contains underscores representing a letter
                # they are joined together with a space between each one
                # for representation purposes.
                self.__word_placeholder_list[i] = ALPHABETS[index]

                self.__word_placeholder = " ".join(self.__word_placeholder_list)

                self.__word_to_guess_label.configure(text=self.__word_placeholder)

        # If the player guesses wrong 5 times, the guessed word is removed and
        # they player is told that they lost and what the answer was.

        if letters_found == 0:
            self.__wrong_answers += 1
            self.__wrong_answer_label.configure(
                text=f"{5- self.__wrong_answers} tries left"
            )

        if self.__wrong_answers == 5:
            self.__word_to_guess_label.configure(
                text=f"You lost! The word was {self.__word_to_guess}"
            )
            self.__word_to_guess = ""

    def get_word(self):
        """
        Method is used to generate a word for the player to guess.
        """
        # get a list of words and pick a random word using functions
        # described later in the code.
        list_of_words = create_word_list()
        word = random_word(list_of_words)

        # The word we got above is placed to an attribute.
        # Then a list of underscores is created and joined together
        # with spaces in between to represent the word.
        self.__word_to_guess = word

        self.__word_placeholder_list = list("_" * len(word))
        self.__word_placeholder = " ".join(self.__word_placeholder_list)

        self.__word_to_guess_label.configure(text=self.__word_placeholder)

        # Getting a new word resets the count of wrong answers
        self.__wrong_answers = 0
        self.__wrong_answer_label.configure(text="5 tries left")


def create_word_list():
    """
    Function creates a list of uppercased common English words found in the text file
    wordlist.txt and returns the list

    :return list_of_words: list, a list containing all the words in the wordlist.txt file in uppercase
    """
    list_of_words = []

    file = open("wordlist.txt", mode="r")

    for row in file:
        row = row.strip()
        row = row.upper()
        list_of_words.append(row)

    return list_of_words


def random_word(list_of_words):
    """
    function picks a word from the param <list_of_words> randomly
    and returns it.

    :param list_of_words: list, a list of words
    :return random_word: string, randomly chosen word
    """
    # Random integer within the indexes of the list
    # to choose a word from the list
    key = randrange(len(list_of_words))
    random_word = list_of_words[key]

    return random_word


def main():
    Game = HangmanGame()


if __name__ == "__main__":
    main()
