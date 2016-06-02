from lf_communication import *

auth_token      = None
session_key     = None
username        = None

def authenticate():

    auth_token = get_token()
    webbrowser.open(AUTH_URL + auth_token)
    raw_input("Press enter after accepting the request...")
    
    sk_result = call_method('auth.getSession', {'token' : auth_token})
    username    = sk_result[0][0].text
    session_key = sk_result[0][1].text
    
    print('Authenticated user ' + username)
    
    with open('.user_data', 'w') as f:
        f.write(username + '\n' +
                session_key)
    
def initiate():
    
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