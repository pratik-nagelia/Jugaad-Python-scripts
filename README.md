# Jugaad-scripts
These are my personal collection of few scripts in python, I wrote while learning, to solve some basic automation tasks.
I 'll be adding more and more scripts and updating documentation about them.

# Freecharge Bot
I have many accounts in freecharge.in , many of them occasionally have credits . This script in python , automated login into multiple accounts and then scrape the user account balance details. I order to use it,
  1. Download chromedriver https://sites.google.com/a/chromium.org/chromedriver/downloads
  2. Extract and copy the file to /usr/local/bin
  3. Install selenium python module
  4. Write all your username & passwords in the format "username" : "password" in a text file and save it with db.txt file.

In order to have a headless support , one can try headless browser, PhantomJs ,simply by initialising, webdriver.PhantomJS()

# Excel Automation 
The methodology used can be found here : https://automatetheboringstuff.com
