from build_dict import word_dicts, letter_dict
from words_list import WORDS
class Solver:
    def __init__(self):
        self.correct = ["","","","",""]
        self.exist = [[],[],[],[],[]]
        self.incorrect = []
        self.guesses = 0
        self.possible_words = []
        self.min_index = -1

    def process_word(self,word,correct_indexes,exist_indexes):
        # print(correct_indexes)
        # print(exist_indexes)
        for index in range(5):
            if index in correct_indexes:
                self.correct[index] = word[index]
            elif index in exist_indexes:
                self.exist[index].append(word[index])
            else:
                if word[index] not in self.incorrect:
                    self.incorrect.append(word[index])
    
    def process_possible_words(self):
        if self.guesses == 0:
            unfiltered_words = self.initialize_words()
        else:
            unfiltered_words = self.possible_words[self.guesses-1]
        filtered_words = self.filterWords(unfiltered_words)
        self.possible_words.append(filtered_words)

    def initialize_words(self):
        words = self.get_shortest_words()
        if (not words):
            exist_is_empty = True
            for index in range(5):
                if (self.exist[index]):
                    exist_is_empty = False
            if (not exist_is_empty):
                words = self.get_shortest_all_places()
            else:
                words = WORDS
        return words


    # for guesses that contain letters in correct places
    def get_shortest_words(self):
        minLength = 5000
        for index in range(5):
            if (self.correct[index] != ""):
                curLetterFrequency = len(word_dicts[index][self.correct[index]])
                if (curLetterFrequency < minLength):
                    minLength = curLetterFrequency
                    self.min_index = index
        if (self.min_index >= 0):
            words = word_dicts[self.min_index][self.correct[self.min_index]]
            return words
        else:
            return None

    # for guesses that only contains letters in incorrect places
    def get_shortest_all_places(self):
        minLength = 5000
        min_exist_index = -1
        for index in range(5):
            for exist_index in range(len(self.exist[index])):
                if (self.exist[index][exist_index] != ""):
                    curLetterFrequency = len(letter_dict[self.exist[index][exist_index]])
                    if (curLetterFrequency < minLength):
                        minLength = curLetterFrequency
                        self.min_index = index
                        min_exist_index = exist_index
        words = letter_dict[self.exist[self.min_index][min_exist_index]]
        return words

    def filterWords(self,curWords):
        # print("************CURWORD**********")
        # print(len(curWords))
        correct_is_empty = True
        for index in range(5):
            if self.correct[index]:
                correct_is_empty = False
                break
        if correct_is_empty:
            # print("Correct is empty")
            correct_filtered_words = curWords
        else:
            correct_filtered_words = []
            for word in curWords:
                correct_valid = True
                for index in range(5):
                    if (self.correct[index] != ""):
                        if (self.correct[index] != word[index]):
                            correct_valid = False
                            break
                if (correct_valid):
                    if word not in correct_filtered_words:
                        correct_filtered_words.append(word)
        # print("************CORRECT**********")
        # print(len(correct_filtered_words))
        exist_filtered_words = []
        for word in correct_filtered_words:
            existence_valid = True
            for index in range(5):
                if not existence_valid:
                    break
                if word[index] in self.exist[index]:
                    existence_valid = False
                    break
                for letter in self.exist[index]:
                    if letter not in word:
                        existence_valid = False
                        break
            if existence_valid and word not in exist_filtered_words:
                exist_filtered_words.append(word)
        # print("************EXIST**********")
        # print(len(exist_filtered_words))
        # exist_filtered_words.sort()
        # print(exist_filtered_words)
        # for word in exist_filtered_words:
        #     for letter in self.incorrect:
        #         if letter 
        completed_filtered_words = []
        for word in exist_filtered_words:
            word_valid = True
            for wrong_letter in self.incorrect:
                if wrong_letter in word:
                    word_valid = False
                    break
            if word_valid:
                if word not in completed_filtered_words:
                    completed_filtered_words.append(word)
        # filtered = filter(lambda letter: False if (letter in self.incorrect) else True,exist_filtered_words)
        # completed_filtered_words = list(filtered)
        # print("************COMPLETED**********")
        # print(len(completed_filtered_words))
        return completed_filtered_words

    def printStatus(self):
        correct_word = ""
        for index in range(5):
            if (self.correct[index] != ""):
                correct_word += self.correct[index]
            else:
                correct_word += "?"
        print(f"Guess# {self.guesses}")
        print(f"Current known correct word: {correct_word}")
        for index in range(5):
            print(f"Index: {index} | Existing letters: {self.exist[index]}")
        print(f"Incorrect letters: {self.incorrect}")
        print(f"Currently, there are {len(self.possible_words[self.guesses-1])} possible words")

    def get_possible_words(self):
        if self.guesses < 1:
            return False
        else:
            return self.possible_words[self.guesses-1]

    @staticmethod
    def validate_word(word):
        if (len(word) != 5):
            return "Please enter a 5-letter word that you guessed."
        word = word.lower()
        letters = "abcdefghijklmnopqrstuvwxyz"
        for index in range(5):
            if (word[index] not in letters):
                return "Words can only contain letters A-Z!"
        return "valid"
