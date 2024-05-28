
import re

########################################################
##        Change logic accoding to your file          ##
########################################################

def extract_credentials(filename):
    credentials = []
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Pattern to match the email and password
            pattern = r"(\b[\w.%+-]+@[\w-]+\.[\w]+\b):([^\s]+)"
            matches = re.findall(pattern, content)
            for match in matches:
                username, password = match
                credentials.append({"username": username, "password": password})
    except IOError:
        print("Error reading file: ", filename)
    return credentials
