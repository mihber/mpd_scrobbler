from lf_communication import *

if os.path.exists('.user_data'):
    with open('.user_data', 'r') as f:
        username = f.readline()
        answer = raw_input(('User ' + username[:-1] + 
        ' seems to be previously logged in. Continue using this account? (Y/N) '))
        
        if answer[0].lower() == 'n':
            authenticate()
        else:
            print('Continuing as ' + username)
            session_key = f.readline()
else:
    authenticate()
    
scrobble('Ghost Town DJs', 'My Boo - Hitman\'s Club Mix')

while True:
    pass