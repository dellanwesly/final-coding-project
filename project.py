import sys
import random

def load_cards(filename):
    cards = []
    try:
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line != "":
                cards.append(int(line))
        file.close()
    except:
        print("error reading file.")
        sys.exit()
    return cards

def get_card_name(value):
    if value == 11:
        return "jack"
    elif value == 12:
        return "queen"
    elif value == 13:
        return "king"
    elif value == 14:
        return "ace"
    else:
        return str(value)

def draw_card(cards):
    return random.choice(cards)

def check_guess(current, next_card, guess):
    if guess == "h":
        return next_card > current
    elif guess == "l":
        return next_card < current
    else:
        return False

def show_rules():
    print("\nrules:")
    print("you will see a card.")
    print("guess if the next card is higher or lower.")
    print("type h for higher, l for lower.")
    print("type q to quit the round.")

def get_valid_guess():
    while True:
        guess = input("higher or lower? (h/l or q): ").lower()
        if guess == "h" or guess == "l" or guess == "q":
            return guess
        else:
            print("invalid input. try again.")

def play_game(cards):
    score = 0
    streak = 0
    playing = True

    current_card = draw_card(cards)

    while playing:
        print("\ncurrent card is:", get_card_name(current_card))
        print("value:", current_card)

        guess = get_valid_guess()

        if guess == "q":
            print("you quit the game.")
            break

        next_card = draw_card(cards)

        print("next card is:", get_card_name(next_card))
        print("value:", next_card)

        correct = check_guess(current_card, next_card, guess)

        if correct:
            print("correct!")
            score = score + 1
            streak = streak + 1
            print("score:", score)
            print("streak:", streak)
            current_card = next_card
        else:
            print("wrong!")
            print("streak ended at:", streak)
            playing = False

    print("game over your score was:", score)

def main():
    if len(sys.argv) < 2:
        print("usage: python project.py <filename>")
        return

    filename = sys.argv[1]

    cards = load_cards(filename)

    if len(cards) == 0:
        print("no cards loaded.")
        return

    print("play higher or lower!")

    show_rules()

    again = "yes"

    while again == "yes":
        play_game(cards)

        again = input("play again? (yes/no): ").lower()

        while again != "yes" and again != "no":
            print("please type yes or no.")
            again = input("play again? (yes/no): ").lower()

    print("thanks for playing!")

    print("program finished.")

if __name__ == "__main__":
    main()