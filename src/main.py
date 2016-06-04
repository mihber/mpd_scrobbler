import lf_communication as lfc
import os

help_message = """This is the help. Commands:
    scrobble    - must be followed by a string in the form of "artist ~ trackname ~ album";  
                you can ommit the album (and, thus, the second squiggly line);
    help        - displays this (as you already know);
    quit        - quits (surprisingly)."""

if os.path.exists('.user_data'):
    with open('.user_data', 'r') as f:
        lfc.username = f.readline()
        answer = raw_input(('User ' + lfc.username[:-1] + 
        ' seems to be previously logged in. Continue using this account? (Y/N) '))
        
        if answer[0].lower() == 'n':
            lfc.authenticate()
        else:
            print('Continuing as ' + lfc.username)
            lfc.session_key = f.readline()
else:
    lfc.authenticate()

print('Welcome to mpd_scrobbler. Right now it\'s pretty much just a scrobbler and it has practically nothing to do with mpd. Have fun')
print('Type help to find out about the commands.')


# Main loop
while True:
    answer = raw_input('> ')
    command = answer.split(' ')[0]
    argument = answer[(len(command) + 1):]
    
    if command == 'help':
        print(help_message)
    elif command == 'quit':
        break
    elif command == 'scrobble':
        if argument.count('~') == 1:
            (artist, track) = argument.split('~')
            lfc.scrobble(artist, track)
        elif argument.count('~') == 2:
            (artist, track, album) = argument.split('~')
            lfc.scrobble(artist, track, album)
        else:
            print((help_message.split('\n')[1] + '\n' + help_message.split('\n')[2]).lstrip())
    