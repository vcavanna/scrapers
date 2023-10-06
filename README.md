<h1>Edmunds Data Scraping and Analytics</h1>

<h2>Project Description</h2>

<h3>Scraping Edmunds Website to Redshift</h3>
This project scrapes the car sales aggregation website  <a href="edmunds.com"> edmunds.com</a> for cars and uploads those cars to an AWS Redshift Serverless data warehouse. The data load job is done in Python with the
<a href="https://beautiful-soup-4.readthedocs.io/en/latest/#" target="_blank"> Beautiful Soup </a>, <a href="https://docs.python-requests.org/en/latest/index.html">requests</a>, and <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html">Boto 3</a> libraries.

<h3>Analyzing Redshift Data to Advise Purchases</h3>
Analytics will provide some additional modeling via dbt in the warehouse to answer particular analytics questions:

1. What is the distribution of value for a particular `make`, `model`, `trim`, `history` and `miles driven`?
2. How long does it take for a great car at a great price to be sold by a dealer?
3. Given a particular `make`, `model`, and `trim`, can you alert a particular user when a car enters the market at the price point that they want?
4. More questions pending.

<h3>Web Portal for Generating Analytics</h3>
A web portal (soon to be developed) will include the ability to have users sign up and view personal analytics for cars that they are interested in (like answering question #3)

<h3>Project Backlog</h3>
<li>Additional data modeling via dbt select statements</li>
<li>Uploading the dataset to kaggle</li>
<li>Find a solution so running the data scrape doesn't have to happen locally</li>
<li>Replace this project backlog with individual issues on <a href="https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue">Github issues</a></li>
<li>Revise the CONTRIBUTING.md doc according to the <a href="https://opensource.guide/starting-a-project/">Open Source Guide</a>

<h2>Installation and Run Instructions</h2>

You can run the data scraping aspect of this project from your local Windows computer for a particular make and model here.

**Windows:**

1. Check that you have python version 3.11 or greater (for windows: type "`py`") and gh in commandline (for windows: type "`gh --version`")
2. From the command line, change directory to the location you want to include the repo: `cd /PATH/TO/REPO/`
3. Enter: "`gh repo clone vcavanna/bs_linkedin_src`"
4. From the root directory of the project, initialize the virtual environment: `py -m venv venv`
5. Activate the virtual environment: `.\venv\Scripts\activate`
6. If using Visual Studio Code: access the command palette with `ctrl + shift + p`, then type: "`python: select interpreter`"
7. Visual Studio Code: Select the venv directory located in the root directory ("`.\venv\Scripts\python.exe`")
8. `py -m pip install bs4, requests`
9. `cd edmunds_etl`
10. `py "edmunds_scraper.py"`
11. You should see a csv file appear in the root directory of the project with all of the used cars in the edmunds database for the make and model.
12. At this point, the workflow would continue with the `upload_to_s3.py` script. However, for that you would need AWS credentials.

<h2>Contributing</h2>

To understand how to contribute, please read the <a href="CONTRIBUTING.md">CONTRIBUTE</a> page.

<h3>Contributing to AWS</h3>

1. <b>You might not need to.</b> One to-do list item on this project is to dissociate Redshift database calls from the rest of the project (i.e. have an interface that has a redshift implementation and a local database implementation). So keep an eye out for contributing in that way.
2. <b>If you have to contribute to AWS, contact me</b>. I'll set up a single sign on MFA account so you can add to Redshift and S3 aspects of the project.
3. See the tutorials and guides section below for more on what has been helpful to learn Redshift, S3, lambda, etc.

<h2>Tutorials and Guides</h2>

### Web Scraping
<li>Credit to realpython.com's tutorial <a href="https://realpython.com/beautiful-soup-web-scraper-python/">Beautiful Soup: Build a Web Scraper With Python</a> for the introduction to webscraping.</li>

### AWS
<li> AWS Active Credit Application <a href="https://www.linkedin.com/pulse/how-receive-1000-aws-active-credit-your-side-project-startup-haque/">How to receive $1000 AWS Active Credit for your side project or startup</a> for getting free credits.</li> 

#### Redshift
<li>Credit to the AWS tutorial <a href="https://docs.aws.amazon.com/redshift/latest/dg/tutorial-loading-data.html">Loading Data from Amazon S3</a> for the introduction to using the redshift database.</li>
<li>Credit to the AWS tutorial <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html">redshift python connect</a> for docs on the python-redshift interaction</li>


#### Lambda
<li>Credit to <a href="https://github.com/aws-samples/getting-started-with-amazon-redshift-data-api/blob/main/quick-start/python/RedShiftServerlessDataAPI.py">this quick-start</a> for showing how to quickly process s3 uploads into the Redshift database.</li>
<li>Credit to <a href="https://repost.aws/knowledge-center/lambda-python-runtime-errors">this knowledge center article</a> for explaining how to fix issues caused by not using the latest boto3 version.</li>
<li>Credit to <a href="https://stackoverflow.com/a/37481851">this stack overflow answer</a> for pointing to lambda docs in AWS.</li>

#### S3
<li>Credit to <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#using-boto3"> the Boto3 quickstart</a> for introducing me to boto3, essential to the copying csv to s3 aspect of this project. </li>
<li> Credit to <a href="https://stackoverflow.com/a/65950645"> this stackoverflow answer</a> for explaining why the above quickstart needs to be configured differently for sso sessions and how to do that.</li>

#### IAM Identity Center
<li>Credit to the <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html">AWS IAM Identity Center user guide</a> for how to set up IAM Identity Center and its users.</li>
<li>Credit to the <a href="https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html">AWS CLI configure with a Single Sign on Session</a> for how to programmatically make use of the above IAM Identity Center to make credentials.</li>

#### Open Source / Git Guides
<li>Credit to the <a href="https://opensource.guide/starting-a-project/">Open Source Guide</a> for how to start this project as open source.</li>
<li>Credit to the <a href="https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue">Github issues</a> docs for helping me to understand how issues can enable team collaboration and to-do lists.</li> 


<h2>Open Source Datasets</h2>
This includes either sources currently in use, or sources that I really want to use to enhance the quality of the end project.
<li><a href="https://www.kaggle.com/datasets/CooperUnion/cardataset">Car Features and MSRP</a> by CopperUnion</li>
<li><a href="https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset">Car Details Dataset</a> by AKSHAY DATTATRAY KHARE, from 'Car Dekho'.</li>
<li><a href="https://www.kaggle.com/code/melikedilekci/eda-car-data-analysis">EDA Car Data Analysis</a> by MELIKE DILEKCI, from 'Car Dekho'.</li>
<li><a href="https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data">Vehicle Listings from Craigslist.org</a>, a great resource from Austin Reese, also see <a href="https://github.com/AustinReese/UsedVehicleSearch">AustinReese's github</a></li>
<li><a href="https://www.kaggle.com/datasets/rkiattisak/car-ownership-predictionbeginner-intermediate">Ownership of Cars dataset</a> from Kiattisak Rattanaporn</li>
<li><a href="https://www.kaggle.com/datasets/suraj520/car-sales-data">Car Sales database</a> by SURAJ. I don't know the source, but it's data on salespersons and commissions for a year by the car.</li>
