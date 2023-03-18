# This is a python script for http://www.gbbs.cc website's automatic sign-in
import requests
import os

# Get the username and password from environment variables
username = os.environ.get("username")
password = os.environ.get("password")

# Create a session object to store cookies
session = requests.Session()

# Login to the website with username and password
login_url = "http://www.gbbs.cc/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
login_data = {
    "username": username,
    "password": password,
    "quickforward": "yes",
    "handlekey": "ls"
}
login_response = session.post(login_url, data=login_data)
if login_response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")

# Sign in to the website with a GET request
sign_in_url = "http://www.gbbs.cc/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1"
sign_in_response = session.get(sign_in_url)
if sign_in_response.status_code == 200:
    print("Sign in successful")
else:
    print("Sign in failed")
