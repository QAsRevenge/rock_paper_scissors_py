from threading import Thread
from datetime import datetime
from network import connect, send
import os

# convert timestamp to iso date time format


def timestamp_to_iso(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)\
        .isoformat().replace('T', ' ').split('.')[0]


def send_message():
    print(f"\nTo start a game of rock - paper - scissors, write one alternative.")
    print("Or just keep chatting!")
    while True:
        send(input())


choices = {}


def react_on_messages(timestamp, user, message):
    global choices
    time = timestamp_to_iso(timestamp)
    print(f'\n{time} {user}\n{message}\n')
    if message in ['paper', 'rock', 'scissors']:
        os.system('cls')
        print(
            f'{user} has chosen to start a game of rock - paper - scissors.\nWaiting for your turn!')
        choices[user] = message
    if len(choices) >= 2:
        if 'rock' in choices.values() and 'paper' in choices.values():
            print(list(choices.keys())[
                list(choices.values()).index('paper')] + ' wins!')
            print(choices)
            choices.clear()
        elif 'paper' in choices.values() and 'scissors' in choices.values():
            print(list(choices.keys())[
                list(choices.values()).index('scissors')] + ' wins!')
            print(choices)
            choices.clear()
        elif 'scissors' in choices.values() and 'rock' in choices.values():
            print(list(choices.keys())[
                list(choices.values()).index('rock')] + ' wins!')
            print(choices)
            choices.clear()
        else:
            print('Tie!')
            print(choices)
            choices.clear()


user = input('Your name: ')
channel = input('Channel to join or create: ')
# connect to (or create) a channel, with a user name
connect(channel, user, react_on_messages)
# start non-blocking thread to input and send messages

Thread(target=send_message).start()
