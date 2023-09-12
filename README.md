# bs_linkedin_src

<h1>Webscraping Linkedin for Job Searches</h1>

<h2>Project Description</h2>

This project is built to help me, a C.S. student, better understand and practice webscraping. This repo has several one-off, ready to run webscraping projects in the folder one-off-scrapers. Feel free to fork to get familiar with web scraping, as well as add more to the current projects based off of the todos.
<a href="https://beautiful-soup-4.readthedocs.io/en/latest/#" target="_blank"> Beautiful Soup </a> and <a href="https://docs.python-requests.org/en/latest/index.html">requests</a> libraries are used here.

I'm putting a special focus on the edmunds scraper, designed to scrape the site edmunds.com for cars and push those cars onto a redshift database, from which I can further model via <a href="https://docs.getdbt.com/quickstarts/redshift?step=1">dbt</a>. Keep a focus on the 

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

<h2>Contributing to the Edmunds scraper</h2>

For scraping additional info (most/all of the project todos are scraping more info)

1. Make sure the project runs after you've forked the repo. If not, contact me.
2. Downloading Postman to understand and search the website is strongly recommended. Otherwise, use inspect on your browser
3. Enter <a href="https://www.edmunds.com/inventory/srp.html?inventorytype=used%2Ccpo&make=toyota&model=toyota%7Ccorolla"> this link </a> in Postman to understand the structure of the page.
4. To write the web scrape, take a look at Beautiful Soup documentation for finding CSS classes and finding by tag in python
    1. By CSS class: e.g. "car_result.find(class_="[CLASS NAME]")
    2. By tag: e.g. "car_result.find("[TAG NAME]")
5. After solving (check with print statements) use an "assert" statement to protect against changes in the Edmunds websites.
6. Commit and push to your own forked repo, then enter a pull request. This can be a little touch and go, so contact me if you run into issues.

<h2>Tutorials and Guides</h2>
Credit to realpython.com's tutorial <a href="https://realpython.com/beautiful-soup-web-scraper-python/">Beautiful Soup: Build a Web Scraper With Python</a> for the introduction to webscraping.
Credit to the AWS tutorial <a href="https://docs.aws.amazon.com/redshift/latest/dg/tutorial-loading-data.html">Loading Data from Amazon S3</a> for the introduction to using the redshift database.
Credit to the AWS tutorial <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html">