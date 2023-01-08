import random
from time import sleep
from os import system, name
from constants import *


def clear(sleep_time):
    sleep(sleep_time)
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_index(visited):
    max_range = len(questions)-1
    index = random.randint(0, max_range)

    # print(index, visited)
    if index not in visited:
        visited.append(index)
        return index
    else:
        return get_index(visited)


def main():
    count = 0
    visited = []

    while (True):
        index = get_index(visited)
        # print("index", index)

        if index != None:
            print(f"Question {count+1}\n")
            print(questions[index])

            for key, value in options[index].items():
                print(f"{key}\t{value}")

            while True:
                try:
                    user_ans = input("\nAnswer: ")
                    if user_ans not in values:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid values. The anwser should be a or b or c or d or q")

            if user_ans == 'q':
                print(
                    f"You Quit the Game.\nCongratulations You won! Rs {amount[count]}")
                break

            if user_ans == answers[index]:
                count += 1
                if count != total_questions:
                    print(f"You won! Rs {amount[count]}")
                    clear(2)
                else:
                    print(
                        f"Congratulations !!! KBC Winner\nYou won! Rs {amount[count]}")
                    break
            else:
                print(f"Wrong answer\nGame Over\nYou won! Rs {amount[count]}")
                break
        else:
            break


clear(1)
print("KBC Game")
print("This is similar to Indian verion of Kaun Banega Crorepati")
print("\nLet's play the game")
clear(1)
main()
