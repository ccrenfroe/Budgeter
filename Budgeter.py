import plaid
from dotenv import load_dotenv
import os
import json

from flask import Flask
app = Flask(__name__)

load_dotenv()

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')

PLAID_COUNTRY_CODES = [s.strip() for s in os.getenv('PLAID_COUNTRY_CODES').split(',')]
PORT=os.getenv('PORT')
PLAID_REDIRECT_URI= os.getenv('PLAID_REDIRECT_URI')
PLAID_PRODUCTS =[s.strip() for s in os.getenv('PLAID_PRODUCTS').split(',')]

client = plaid.Client(PLAID_CLIENT_ID, PLAID_SECRET, environment='development')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/create_link_token", methods=['GET','POST'])
def create_link_token():
    try:
        # TODO: Implement unique client_user_id
        client_user_id = "1234"
        # Create a link_token for the given user
        response = client.LinkToken.create({
        'client_id' : PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
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
        return
    except plaid.errors.PlaidError as e:
        print(str(e))
        return

# TODO: Do not use in deployment environment!
if __name__ == "__main__":
    print(PLAID_REDIRECT_URI)
    app.run(port=os.getenv('PORT',8000))