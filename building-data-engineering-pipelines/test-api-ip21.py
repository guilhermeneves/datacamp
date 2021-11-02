import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

CLIENT_ID=''
CLIENT_SECRET=''
OAUTH2_URL='https://login.microsoftonline.com/fcb2b37b-5da0-466b-9b83-0014b67a7c78/oauth2/v2.0/token'

# Get Azure Token
client_args = {
                'client_id': CLIENT_ID,
                'scope' : f"{CLIENT_ID}/.default"
              }

client = BackendApplicationClient(**client_args)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(
            token_url = OAUTH2_URL,
            client_id = CLIENT_ID,
            client_secret = CLIENT_SECRET
        )

## Get Ip21 data
url = "https://api-t.monsanto.com:443/api938505live/ip21"

querystring = {"ipSite":"10.246.189.92",
               "sqlQuery":"SELECT * FROM nf_tank_level('06-OCT-20 14:00:00','06-OCT-20 14:10:00');",
               "hostname":"SJCWSQLIP2PRD02",
               "useAD":"true"}

payload = {}
headers = {"Authorization": f"Bearer {token}"}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

print(response.text)