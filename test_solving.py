from words_list import WORDS
from solver import Solver
import time
# WORD1 = "adieu"
# WORD2 = "frost"
WORD1 = "pious"
WORD2 = "heart"

print("Starting test for all words")
start_time = time.time()
max_possible_words = 0
possible_words_sum = 0
large_list_count = 0

for word in WORDS:
    solver = Solver()
    correct = []
    exist = []
    for i in range(5):
        if WORD1[i] in word:
            if WORD1[i] == (word[i]):
                correct.append(i)
            else:
                exist.append(i)
    solver.process_word(WORD1,correct,exist)
    solver.process_possible_words()
    solver.guesses += 1

    correct = []
    exist = []
    for i in range(5):
        if WORD2[i] in word:
            if WORD2[i] == (word[i]):
                correct.append(i)
            else:
                exist.append(i)
    solver.process_word(WORD2,correct,exist)
    solver.process_possible_words()
    solver.guesses += 1
    possible_words = solver.get_possible_words()
    if word not in possible_words:
        print(f"{word} is not in words")
        print(possible_words)
        solver.printStatus()
        break
    # solver.printStatus()


    cur_possible_word_length = len(possible_words)
    if cur_possible_word_length > max_possible_words:
        max_possible_words = cur_possible_word_length
    possible_words_sum += cur_possible_word_length
    if (cur_possible_word_length >= 30):
        large_list_count += 1
        # print(f"This word has at least 30 possible words after 2 guesses: {word}")
        # print(possible_words)
        # solver.printStatus()
    del solver
print("DONE")
print(f"It took {time.time() - start_time} seconds")
print(f"Max possible words: {max_possible_words}")
print(f"Average possible words: {possible_words_sum / len(WORDS)}")
print(f"There are {large_list_count} words with large possible words list after 2 guesses")