import requests
import base64
import datetime
from urllib.parse import urlencode
import random

client_id = '1eaf1a5f9c7447bdbbb14523f507aeaa'
client_secret = 'a354a0df358643e1884e3692593cb7a7'

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
    
    def get_client_credentials (self):
        """
        Returns a base64 encoded string 
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_secret == None :
            raise Exception("client_id and client_secret not found")
        client_cred = f"{client_id}:{client_secret}"
        client_cred_b64 = base64.b64encode(client_cred.encode())
        return client_cred_b64.decode()
    
    def get_token_headers (self):
        client_cred_b64 = self.get_client_credentials()
        return{
            "Authorization" : f"Basic {client_cred_b64}"
        }
        
    def get_token_data (self):
        return{
            "grant_type" : "client_credentials"
        }
        
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range (200, 299) :
                raise Exception("Authentication Failed")
        data = r.json()
        exp_now = datetime.datetime.now()
        access_token = data['access_token']
        expire_in = data['expires_in']
        expires = exp_now + datetime.timedelta(seconds=expire_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < exp_now
        return True
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token
    
    def search(self, query, search_type='track' ):
        access_token = self.get_access_token()
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
        endpoint = "https://api.spotify.com/v1/search"
        data = urlencode({"q": query, "type": search_type})
        lookup_url = f"{endpoint}?{data}"
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return print(r.json())
    
spotify = SpotifyAPI(client_id, client_secret) 

genre_tone_map = {
    'joy' : ['acoustic','dance','happy','party'],
    'sadness':[],
    'anger':[],
    'fear':[],
    'neutral':[]   
}

genre = random.choice(genre_tone_map['joy'])
print(genre)

spotify.search(f"genre:{genre}")
