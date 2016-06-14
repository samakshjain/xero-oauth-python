# @Author: Samaksh Jain <ybl>
# @Date:   Monday, June 13th 2016, 1:12:37 pm(IST)
# @Email:  samakshjain@live.com
# @Project: Aplynk
# @Last modified by:   ybl
# @Last modified time: Monday, June 13th 2016, 4:35:48 pm(IST)
# @License: All rights reserved by Apora India.



from requests_oauthlib import OAuth1Session, OAuth1
import requests

from config import client_key, client_secret

request_token_url = 'https://api.xero.com/oauth/RequestToken'
oauth = OAuth1(client_key, client_secret=client_secret)

r = requests.post(url=request_token_url, auth=oauth)
# print(r.content)

from urlparse import parse_qs

credentials = parse_qs(r.content)
resource_owner_key = credentials.get('oauth_token')[0]
resource_owner_secret = credentials.get('oauth_token_secret')[0]

base_authorization_url = 'https://api.xero.com/oauth/Authorize'
authorize_url = base_authorization_url + '?oauth_token='
authorize_url = authorize_url + resource_owner_key
print 'Please go here and authorize,'
print authorize_url
verifier = raw_input('Please input the verifier')

access_token_url = 'https://api.xero.com/oauth/AccessToken'

oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

r = requests.post(url=access_token_url, auth=oauth)
credentials = parse_qs(r.content)
resource_owner_key = credentials.get('oauth_token')[0]
resource_owner_secret = credentials.get('oauth_token_secret')[0]

print "Token: " + resource_owner_key
print "Secret: " + resource_owner_secret

# # Example Request
# contacts = 'https://api.xero.com/api.xro/2.0/Contacts'
#
# oauth = OAuth1(client_key,
#                    client_secret=client_secret,
#                    resource_owner_key=resource_owner_key,
#                    resource_owner_secret=resource_owner_secret)
# headers = {
#     'Accept': 'application/json'
# }
#
# r = requests.get(url=contacts, auth=oauth, headers=headers)
#
# print r.text
#
# print r.content
