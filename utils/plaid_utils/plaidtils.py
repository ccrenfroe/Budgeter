import plaid
from dotenv import load_dotenv
import os
import json

load_dotenv('../.env')

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')

PLAID_COUNTRY_CODES = [s.strip() for s in os.getenv('PLAID_COUNTRY_CODES').split(',')]
PORT=os.getenv('PORT')
PLAID_REDIRECT_URI= os.getenv('PLAID_REDIRECT_URI')
PLAID_PRODUCTS =[s.strip() for s in os.getenv('PLAID_PRODUCTS').split(',')]

PLAID_CLIENT = plaid.Client(PLAID_CLIENT_ID, PLAID_SECRET, environment='development')

def create_link_token():
    try:
        print(PLAID_REDIRECT_URI)
        print(PLAID_CLIENT_ID)
        print(PLAID_SECRET)
        # TODO: Implement unique client_user_id
        client_user_id = "1234"
        # Create a link_token for the given user
        response = PLAID_CLIENT.LinkToken.create({
        'user': {
            'client_user_id': client_user_id,
        },
        'products': PLAID_PRODUCTS,
        'client_name': 'Budgeter',
        'country_codes': PLAID_COUNTRY_CODES,
        'language': 'en',
        })
        link_token = response['link_token']
        # Send the data to the client
        print(json.dumps(response))
        print("Completed the link token creation.")
        return
    except plaid.errors.PlaidError as e:
        print(str(e))
        return