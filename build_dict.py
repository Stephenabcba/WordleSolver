from words_list import WORDS
letters = "abcdefghijklmnopqrstuvwxyz"
word_dicts = [
    {},{},{},{},{}
]
letter_dict = {}
for letter in letters:
    letter_dict[letter] = []
    for index in range(5):
        word_dicts[index][letter] = []

for word in WORDS:
    for index in range(5):
        if word[index] in word_dicts[index]:
            word_dicts[index][word[index]].append(word)
        # else:
        #     word_dicts[index][word[index]] = [word]
        letter_dict[word[index]].append(word)

if __name__ == "__main__":
    # print(len(WORDS))
    # print(len(letter_dict["a"]))
    for index in range(5):
        for letter in word_dicts[index]:
            print(f"Index: {index} Letter: {letter}")
            print(len(word_dicts[index][letter]))

