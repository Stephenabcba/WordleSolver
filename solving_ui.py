from solver import Solver
solver = Solver()

def get_word():
    print("Please enter the word that you guessed!")
    curWord = input(">")
    valid = Solver.validate_word(curWord)
    while valid != "valid":
        print(valid)
        print("Please enter the word that you guessed!")
        curWord = input(">")
        valid = Solver.validate_word(curWord)

    correct = []
    print("Please enter the places where the letters were correct (Green)")
    print("Type 'cont' to continue to the next step")
    correct_index = input(">")
    while (correct_index != "cont"):
        correct.append(int(correct_index))
        correct_index = input(">")

    exist = []
    print("Please enter the places where the letters were in incorrect places (Yellow)")
    print("Type 'cont' to continue to the next step")
    exist_index = input(">")
    while (exist_index != "cont"):
        exist.append(int(exist_index))
        exist_index = input(">")

    solver.process_word(curWord,correct,exist)
    solver.process_possible_words()
    solver.guesses += 1


def start_solver():
    print("Welcome to Wordle Solver!")
    while(solver.guesses < 6):
        print("Please select what you want to do:")
        print("1. Enter a word that you have guessed")
        print("2. View current game status")
        print("3. See possible words")
        print("Type q to quit")
        choice = input(">")
        if (choice == '1'):
            get_word()
        elif (choice == '2'):
            solver.printStatus()
        elif (choice == '3'):
            possible_words = solver.get_possible_words()
            if type(possible_words) == list:
                print(f"There are {len(possible_words)} possible words:")
                print(possible_words)
            else:
                print("You must make a guess first!")
        elif (choice == 'q'):
            break

start_solver()