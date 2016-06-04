import lf_communication as lfc
import os

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
    
lfc.scrobble('Ghost Town DJs', 'My Boo - Hitman\'s Club Mix')

while True:
    pass