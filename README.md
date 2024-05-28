# Netflix Login Exploder

Netflix Login Exploder is an unofficial CLI application for checking correct credentials in real-time on the Netflix application. It recursively extracts data (username & password) from another file (e.g., a text file) containing multiple sets of credentials in a predictable format.

## Why is it needed? 🤔

This tool comes in handy when you have a file with numerous Netflix account credentials in a predictable format. It extracts these credentials and checks if they are valid by attempting to log in to the Netflix application.

## Usage

1. Install the required dependencies using the following commands:
    - ```pip install requests``` or ```pip3 install requests```
    - ```pip install lxml``` or ```pip3 install lxml```
2. Optionally, modify the file and logic for extracting credentials, ensuring the correct format.
3. Run the `index.py` file.
4. The application will output the result for each extracted credential, indicating success or failure.
5. Correct credentials will be allowed for login on the Netflix website.

## Output Example

    email1@example.com
    Email: email1@example.com
    Password: password1
    
    email2@example.com
    Attempt 1 failed.
    email2@example.com
    Attempt 2 failed.
    Max retries reached. Moving to the next credential.
    
    email3@example.com
    Email: email3@example.com
    Password: password3
    
    Successful logins:
    Email: email1@example.com, Password: password1
    Email: email3@example.com, Password: password3
    
    Count completed: 3

This example illustrates the output of the application, showing the attempt status for each credential and the final successful logins along with the count of completed attempts.

## Credits

This project was inspired by [This repo](https://github.com/GooogIe/Netflix-login-API), a similar tool developed by [GooogIe](https://github.com/GooogIe/). We thank them for their contribution to the community.

## Thank for reading 💙
Feel free to contribute to this project and enhance the code to support other file formats such as Excel or CSV.