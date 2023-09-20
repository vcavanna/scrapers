# bs_linkedin_src

<h1>One-off webscrapers</h1>

<h2>Project Description</h2>

This project is built to help me, a C.S. student, better understand and practice webscraping. This repo has several one-off, ready to run webscraping projects in the folder one-off-scrapers. Feel free to fork to get familiar with web scraping, as well as add more to the current projects based off of the todos.
<a href="https://beautiful-soup-4.readthedocs.io/en/latest/#" target="_blank"> Beautiful Soup </a> and <a href="https://docs.python-requests.org/en/latest/index.html">requests</a> libraries are used here.

I'm putting a special focus on the edmunds scraper, designed to scrape the site edmunds.com for cars and push those cars onto a redshift database, from which I can further model via <a href="https://docs.getdbt.com/quickstarts/redshift?step=1">dbt</a>. Based in AWS, so redshift, s3, iam, and lambda are all in the tech stack.

<h3>Project Backlog<h3>
<li>edmunds scraper: Additional data modeling via dbt select statements</li>
<li>edmunds scraper: Uploading the dataset to kaggle</li>
<li>edmunds scraper: Find a solution so running the data scrape doesn't have to happen locally</li>

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

<h3>For scraping additional info (most/all of the project todos are scraping more info)</h3>

1. Make sure the project runs after you've forked the repo. If not, contact me.
2. Downloading Postman to understand and search the website is strongly recommended. Otherwise, use inspect on your browser
3. Enter <a href="https://www.edmunds.com/inventory/srp.html?inventorytype=used%2Ccpo&make=toyota&model=toyota%7Ccorolla"> this link </a> in Postman to understand the structure of the page.
4. To write the web scrape, take a look at Beautiful Soup documentation for finding CSS classes and finding by tag in python
    1. By CSS class: e.g. "car_result.find(class_="[CLASS NAME]")
    2. By tag: e.g. "car_result.find("[TAG NAME]")
5. After solving (check with print statements) use an "assert" statement to protect against changes in the Edmunds websites.
6. Commit and push to your own forked repo, then enter a pull request. This can be a little touch and go, so contact me if you run into issues.

<h3>For accessing AWS and configuring appropriate files:</h3>

1. You might not need to. I'll be working on some basic developer tools like a postman mockup so that you don't need AWS credentials to make the program work in a way that makes sense. I'll update here for more as I learn more.
2. If you have to contribute to AWS, contact me and I'll set up a single sign on MFA account so you can add to Redshift and S3 aspects of the project.
3. See the tutorials and guides section below for more on what has been helpful to learn Redshift, S3, lambda, etc.

<h2>Tutorials and Guides</h2>
Credit to realpython.com's tutorial <a href="https://realpython.com/beautiful-soup-web-scraper-python/">Beautiful Soup: Build a Web Scraper With Python</a> for the introduction to webscraping.
Credit to the AWS tutorial <a href="https://docs.aws.amazon.com/redshift/latest/dg/tutorial-loading-data.html">Loading Data from Amazon S3</a> for the introduction to using the redshift database.
Credit to the AWS tutorial <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html">redshift python connect</a> for docs on the python-redshift interaction

Credit to <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#using-boto3"> the Boto3 quickstart</a> for introducing me to boto3, essential to the copying csv to s3 aspect of this project.
Credit to <a href="https://stackoverflow.com/a/65950645"> this stackoverflow answer</a> for explaining why the above quickstart needs to be configured differently for sso sessions and how to do that.

Credit to the <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html">AWS IAM Identity Center user guide</a> for how to set up IAM Identity Center and its users.
Credit to the <a href="https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html">AWS CLI configure with a Single Sign on Session</a> for how to programmatically make use of the above IAM Identity Center to make credentials.

Credit to <a href="https://github.com/aws-samples/getting-started-with-amazon-redshift-data-api/blob/main/quick-start/python/RedShiftServerlessDataAPI.py">this quick-start</a> for showing how to quickly process s3 uploads into the Redshift database.
Credit to <a href="https://repost.aws/knowledge-center/lambda-python-runtime-errors">this knowledge center article</a> for explaining how to fix issues caused by not using the latest boto3 version.
Credit to <a href="https://stackoverflow.com/a/37481851">this stack overflow answer</a> for pointing to lambda docs in AWS.

<h2>Open Source Datasets Used</h2>
This includes either sources currently in use, or sources that I really want to use to enhance the quality of the end project.
<a href="https://www.kaggle.com/datasets/CooperUnion/cardataset">Car Features and MSRP</a> by CopperUnion
<a href="https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset">Car Details Dataset</a> by AKSHAY DATTATRAY KHARE, from 'Car Dekho'.
<a href="https://www.kaggle.com/code/melikedilekci/eda-car-data-analysis">EDA Car Data Analysis</a> by MELIKE DILEKCI, from 'Car Dekho'.
<a href="https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data">Vehicle Listings from Craigslist.org</a>, a great resource from Austin Reese, also see <a href="https://github.com/AustinReese/UsedVehicleSearch">AustinReese's github</a>
<a href="https://www.kaggle.com/datasets/rkiattisak/car-ownership-predictionbeginner-intermediate">Ownership of Cars dataset</a> from Kiattisak Rattanaporn
<a href="https://www.kaggle.com/datasets/suraj520/car-sales-data">Car Sales database</a> by SURAJ. I don't know the source, but it's data on salespersons and commissions for a year by the car.