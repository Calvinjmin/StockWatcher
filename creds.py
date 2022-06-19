import os
from dotenv import load_dotenv

# Using ENV Variables
load_dotenv()

# Credentials
gmail_user = os.environ.get('GOOGLE_ACCOUNT', 'example@gmail.com')
gmail_password = os.environ.get('GOOGLE_PASSWORD', 'NONE')


