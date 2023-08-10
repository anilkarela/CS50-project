# CS50x Project: URL Shortener

#### Video Demo: MAKE VIDEO
#### Live App: https://vinaycode7.pythonanywhere.com/

## Tech Stack
- Python
- Flask
- SQL (MySQL / SQLITE)
- Jinja
- JavaScript
- HTML
- Bootstrap

## Description
This is a simple URL shortener project built with Python and Flask. The application allows users to shorten long URLs into custom short URLs and stores the data on a SQLITE databse. It's a lightweight and easy-to-use solution for generating short links.

It uses Jinja as templating language for dynamic HTML pages. The project also uses CS50's own SQL library to interact with the database and perform queries.

### Some Features:
- Very easy to use and have minimal UI and styles.
- Create custom Short URLs for any link you want.
- Collection of all short URLs are displayed in a single page.
- Shows how many times a link has been visited using the custom URL.
- Shows how long ago the link was visited using the custom URL.

## How to install and setup

- Prerequisites: Python should be installed on the system and pip command should be availabe to use from anywhere.

1. Clone the repository using below command or download and extract the ZIP file.
    ```bash
    git clone https://github.com/your-username/url-shortener-app.git
    ```

2. Open the project folder containing **`app.py`** in your preferred code editor. Open the terminal and make sure your current directory is one the that contains all the files and folders such as `static`, `templates`, `app.py`, `helpers.py` etc.

3. Now create and activate a virtual environment using this command:

    For Windows,
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

    For Mac/Linux
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    #### Note: Make sure that you terminal prompt starts with something like `(.venv)`, this makes sure that your virtual environment is activated.

    Learn more about virtual environment here: [Virtual Environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

4. This project only requires two dependencies i.e. `Flask` and `cs50`. To install these dependencies, just use the following command:
    ```bash
    pip install Flask cs50
    ```
    To check if all dependencies are installed just use:
    ```bash
    pip list
    ```

5. Now everything is done and you can use the following command to run your app:
    ```bash
    python app.py  # For Windows
    python3 app.py  # For Mac/Linux
    ```
6. Your app now must be running on `127.0.0.1:5000` or `localhost:5000`.


## Files description

### 1. app.py

1. Import Statements: The code imports Flask and cs50 library for managing routes and database, also uses datetime module for getting current date and time. The helpers import statement imports a piece of code from helpers.py discussed later.

2. The Flask app is initialized with the name of the current module (__name__).

3. The code sets up a connection to an SQLite database named "shortUrls.db" using the cs50.SQL class.

4. Index Route (Home Page): This route ("/") handles both GET and
POST requests. On a GET request, it renders an HTML template called "index.html" and passes in data including the fullUrl, shortUrl, and message parameters.

    On a POST request, it retrieves the input full URL and short URL. If the short URL is not alphanumeric, it redirects back to the index page with an "invalid" message. If the short URL is already taken, it redirects back with a "taken" message. Otherwise, it inserts the URL data into the database and redirects back to the index page with a "success" message.

5. Database Route: This route ("/database") fetches all data from the database and orders it by the "lastClicked" timestamp in descending order. It then renders an HTML template called "database.html" and passes in the fetched data and a helper function time_ago.

6. Short URL Route: This dynamic route ("/<short_url>") is used to redirect users based on the provided short URL. It retrieves the corresponding data from the database. If no data is found, it displays a "URL Not Found" message. If the difference between the current time and the last clicked timestamp is greater than 2 seconds, it updates the click count and last clicked timestamp in the database. Finally, it performs a redirect to the original full URL associated with the provided short URL.

### 2. helpers.py

This file contains a single function `time_ago` which is used to calculate the time difference between the last click and current time of a short url.

### 3. shortUrls.db

This is a SQLite database used for storing the short url data. It contains a single table named `urlData` in the following form.

| shortUrl    |  fullUrl   | clickCount  | LastClicked   |
|-------------|------------|-------------|---------------|
| short Link1 | full Link1 | count value | date and time |
| short Link2 | full Link2 | count value | date and time |
| ...         | ...        | ...         | ...           |


### 4. static/script/js

This file provieds extra features added to the form in `index.html`, such as feedback messages for invalid or taken urls, automatically filling the short url. If user has selected some url and provided full url then filling it again for some change.
Also provied `copy` functionality to user.

### 5. templates/layout.html

This is a base file for creating dynamic html pages, this file is further used by `index.html` and `database.html` to provide the content that should be displayed.

### 6. templates/index.html

This is the main page (home page) that the user sees. It is styled using bootstrap and contains a form which makes a POST request to the server. It also contains \<script> tag to refer the `script.js` file for providing user friendly functions.

### 7. templates/database.html

This page contains a table and gets dynamic data from server which is then displayed to the user.


## Contribution
If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.


# THE END
Thanks for reading...
