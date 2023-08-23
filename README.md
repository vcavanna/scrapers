# bs_linkedin_src

<h1>Webscraping Linkedin for Job Searches</h1>

<h2>Project Description</h2>

This project is built to help me, a C.S. student, better understand and practice webscraping. The long-range goal of the project is an end-to-end working demo of scraping Linkedin data and put it into a Snowflake database, where I can do ad-hoc queries on it.

This repo has several one-off, ready to run webscraping projects in the folder one-off-scrapers. Feel free to fork to get familiar with web scraping, as well as add more 
Why you used the technologies you used, <a href="https://beautiful-soup-4.readthedocs.io/en/latest/#" target="_blank"> Beautiful Soup </a> and <a href="https://docs.python-requests.org/en/latest/index.html">requests</a> libraries are used here.

Since the Linkedin page isn't static, I need to do some more reading and practice to make sure that I'm getting the data right.

<h2>How to Install and Run the One-off Scrapers</h2>

For Windows:

1. Check that you have python version 3.11 or greater (for windows: type "py") and gh in commandline (for windows: type "gh --version")
2. From the command line, change directory to the location you want to include the repo: cd /PATH/TO/REPO/
3. Enter: "gh repo clone vcavanna/bs_linkedin_src"
4. From the root directory of the project, initialize the virtual environment: py -m venv venv
5. Activate the virtual environment: .\venv\Scripts\activate
6. If using Visual Studio Code: access the command palette with ctrl + shift + p, then type: "python: select interpreter"
7. Visual Studio Code: Select the venv directory located in the root directory (".\venv\Scripts\python.exe")
8. py -m pip install bs4, requests
9. cd one-off-scrapers
10. py "[INSERT FILE NAME]"

<h2>Credits</h2>
Credit to realpython.com's tutorial <a href="https://realpython.com/beautiful-soup-web-scraper-python/">Beautiful Soup: Build a Web Scraper With Python</a> for the introduction to webscraping.
