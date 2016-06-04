import xml.etree.ElementTree as ET
import webbrowser
import requests
import hashlib
import time
import os

ROOT_URL        = 'http://ws.audioscrobbler.com/2.0/'
AUTH_URL        = 'http://www.last.fm/api/auth/?api_key=a8a27d8d80f66d653d19e64dd16bee5a&token='

api_key         = 'a8a27d8d80f66d653d19e64dd16bee5a'
shared_secret   = 'af3d49a4107352174bb6fead328e82e1'
session_key     = None
username        = None


def generate_api_sig(params):
    signature = hashlib.md5()

    for key in sorted(params.keys()):
        signature.update((key + params[key]).encode('utf-8'))
    signature.update(shared_secret.encode('utf-8'))
    
    return signature.hexdigest()
    
def call_method(method, params={}):
    params['api_key']   = api_key
    params['method']    = method
    params['api_sig']   = generate_api_sig(params)
    
    post_req = requests.post(ROOT_URL, params=params)

    if post_req.status_code == 200:
        return ET.fromstring(post_req.text)

    else:
        print("Calling method", method, "failed")
        return False
        

def get_token():

    token_result = call_method('auth.getToken')
    if token_result is False:
        print("Failed to request authentication token")
        return False

    else:
        auth_token = token_result[0].text
        print("Received authentication token " + auth_token)
        return auth_token
        
def authenticate():
    global session_key

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


def scrobble(artist, name, album = None):
    params = {}
    
    params['artist']    = artist
    params['track']     = name
    params['timestamp'] = str(int(time.time()))
    if album != None:
        params['album'] = album
    params['sk']        = session_key
        
    call_method('track.scrobble', params)