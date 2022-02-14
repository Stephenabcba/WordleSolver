# Wordle Solver
## About
- This is a text-based assistant to help you solve the recently popular game Wordle.
- This version is written in Python.
- There are currently 2309 words that could be possible solutions as of 2/14/2022
  - The words are pulled from the Wordle website's javascript file
    - The words are saved in `words_list.py`
- With each "guess" you enter (along with the hit/miss response from Wordle), the program filters through the words list, providing you with a list of all possible words that could be the answer (target word)
- With two good initial guesses, there are at most 45 choices left in the word list after two guesses.
- Have fun!

## How to use it
1. Download/Clone the project.
2. in terminal/command prompt, run `python solving_ui.py` in the root folder
3. follow the text prompts