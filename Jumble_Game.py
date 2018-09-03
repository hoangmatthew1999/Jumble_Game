import random

source = open ("words.txt")
source_list = []
for word in source:
    source_list.append(word)
''.join(source_list)


while True:
    hat_picker= random.randint(0,113808)
    magic_word = (source_list[hat_picker] )
    magic_word = magic_word.strip('\n')
    print(magic_word)

    jumble = list(magic_word)
    random.shuffle(jumble)

    new_str = ''.join(jumble)
    print(new_str)

    prompt = input("What do you think the word is   ")

    if prompt == magic_word:
        print("You have correctly guessed the word")
    else:
        print("Try again. Your answer is not the correct word")

