import random as rand

guess_count = 0
guess_limit = 10
out_of_guesses = False
guess = " "
number = rand.randint(1, 66)
word_list_source = ["earth", "no", "sound", "made",
"none", "could", "hear", "the", "birches", "creak",
"for", "no", "breeze", "stirred",
"no", "tapping", "from", "the", "evergreen",
"not", "one", "bird", "moved",
"none", "could", "hear", "the", "voice", "of", "snow",
"for", "no", "beast", "roamed",
"and", "all", "was", "cold", "and", "still",
"Locked", "in", "reverent", "tone", "strange", "quiet", "So", "quietly", "strange",
"no", "scene", "heard", "but", "sound", "saw",
"for", "it", "is", "during", "times", "as", "this",
"gods", "voice", "speaks",
"his", "awe"
]
word_list = [word.lower() for word in word_list_source]
secret_word = word_list[int(number)]


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("pick a letter: ")
        guess_count += 1
    else:
        out_of_guesses = True
    if guess in secret_word:
        print("closer")
    else:
        print("nah")
if guess == secret_word:
    print("you won!")
else:
    print("you lost!")
    print("the word was " + secret_word)