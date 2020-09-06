import random
import json
import pprint
import sys
data = "data.json"
games = ["guess_the_number", "tic_tac_toe"]


def displayMenu():
    print("Menu".center(50, "="))
    print("""
1. Play Guess the Number
2. Leaderboard
3. Log out (WIP)
4. Quit
""")
def displayLeaderboard():
    print("Leaderboard".center(50, "="))
    with open(data,"r") as f:
        data_content = json.load(f) # stores file in memory
    leaderboard = pprint.pformat((data_content)) # pretty formats the leaderboard (wip)
    return leaderboard

def login():
    with open(data,"r") as f:
        data_content = json.load(f)
    username = input("What's your username\n")
    password = input("What is your password\n")
    try:
        if data_content[username]["password"] == password:
            print("Successfully logged in")
            return username
    except KeyError:
        while True:
            bool = input("Do you want to create an account? Enter yes or no\n")
            # Creating account
            if bool.lower() == "yes": # Makes "bool" lowercase so the player can say any case when saying yes or no (reduces errors)
                data_content[username] = {"password": password, games[0]:0, games[1]: 0} # Creates username and adds a dictionary which assigns the password and places the scores of the games and assigns them as 0
                with open(data, "w") as f:
                    json.dump(data_content, f, indent=2) # Writes over the data.json file then puts the rest of the file back and adds an indent for easier reading
                return username # Uses this to exit or continue with the game
                break
            # Player decided not to play by not creating account
            elif bool.lower() == "no": # Makes "bool" lowercase so the player can say any case when saying yes or no (reduces errors)
                choice = input("Are you sure? If you don't create an account you can't play.\n")
                if choice.lower() == "yes":
                    print("Rip\n")
                    return "not playing" # Uses this answer to exit or continue with the game
                    break
                # Creating account
                elif choice.lower() == "no":
                    data_content[username] = {"password": password, games[0]:0, games[1]: 0}
                    with open(data, "w") as f:
                        json.dump(data_content, f, indent=2) #
                    return username # Uses this answer to exit or continue with the game
                    break
            else:
                print("You didn't say yes or no")
                continue



def data_write(name, score, game):

    with open(data, "r") as f: 
        data_content = json.load(f) # stores file in memory

        player_score = data_content[name][game] # grabs score from data.json and assigns it to player_score
        player_score = player_score + score # reassigns playerscore by adding score earned to playerscore
        data_content[name][game] = player_score
        with open(data, "w") as f:
            json.dump(data_content, f, indent=4) # writes over previous score
        return player_score

def data_read(name, score, game):
    with open(data, "r") as f:
        data_content = json.load(f)

        player_score = data_content[name][game]
        player_score += score
        return player_score

def guess_the_number(name):
    game = "guess_the_number"
    score = 1
    print("Guess the Number".center(50, "-"))
    while True:
        correct_number = random.randint(1, 10)
        print(f"Ok {name}, The number is in between 1 and 10. You have 5 guesses.")
        guess = 0
        for guesses in range(1, 6):
            guess = int(input(f"Take a guess {name}\n"))
            if guess < correct_number:
                print("Your guess is too small")
            elif guess > correct_number:
                print("Your guess is too big")
            elif guess == correct_number:
                print("You got it right!")
                break
        if guess == correct_number:
            print(f"Congrats, you got the right answer {name}, you took {guesses} guesses.\n")
            new_score = data_write(name, score, game)
            print(f"Your score is: " + str(new_score))
            break
        else:
            new_score = data_read(name, score, game) - 1
            score = 0
            print(f"You got it wrong {name} lmao, you took {guesses} guesses.\n")
            print("Your score is: " + str(new_score))
            break



playing = login()
while True:
    with open(data,"r") as f:
        data_content = json.load(f)

    if playing == "not playing":
        continue
    elif playing in data_content:
        displayMenu()
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            guess_the_number(playing)
            continue
        if choice == "2":
            print(displayLeaderboard() + "\n")
            input("Press Enter to continue:")
            continue
        if choice == "3":
            print("WIP, try again later")
            continue
        if choice == "4":
            print("Goodbye")
            sys.exit()

