import os
import time


def change_dir(path):
    while True:
        try:
            path = input("Enter new path ")
            os.chdir(path)
            return path
        except FileNotFoundError:
            print("path specified doesn't exist...")


def commandchoice(path):

    print("Pick a option")

    options = {
        1: "Print the current working directory",
        2: "Change the current working directory",
        3: "List all files in the current working directory",
        4: "Copy files",
        5: "delete a file",
        6: "Open python shell",
        7: "Exit program"
    }
    for key, value in options.items():
        print(key, ":", value)
        time.sleep(0.2)
    print("\n")
    user_choice = int(input("Pick a command: "))

    if user_choice == 1:
        print(path)
        time.sleep(3)
    elif user_choice == 2:
        change_dir(path)
    elif user_choice == 7:
        print("Thank you, und goodbye")
        exit()


def main():

    print("Welcome to PythonOs, this programm wil let you execute Os commands, and even a python shell")
    while True:
        path = os.getcwd()
        commandchoice(path)


main()
