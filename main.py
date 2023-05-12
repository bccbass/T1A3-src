import json
import subprocess
from DiceClass import Dice
from funcs import game, create_user_instance, player_from_log, log_final_score, wrap_up_message, print_big_yahtzee, play_again_prompt
import colorama
from colorama import Fore
colorama.init()
from pyfiglet import Figlet
colorama.init()
# from playsound import playsound



def main():
    subprocess.call(['tput', 'reset'])
    f = Figlet(font='slant', justify='center')
    print_big_yahtzee()
    player = create_user_instance()
    # Initialize Dice object
    dice = Dice()
    with open('score-log.json', 'r') as f: # open json file and set contents to var log
        log = json.load(f)
    player_from_log(log, player)
    # playsound('./Yahtzee_Remix.mp3')
    # Call game function to start:
    game(player, dice)
    log = log_final_score(player, log)
    wrap_up_message(log, player)
    with open('score-log.json', 'w') as f:
        json.dump(log, f, indent=2)
    play_again_prompt(main)

if __name__ == "__main__":
    main()