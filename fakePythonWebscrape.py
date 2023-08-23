import requests
import bs4

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = bs4.BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title is-5")
    company_element = job_element.find("h3", class_="subtitle is-6 company")
    location_element = job_element.find("p", class_="location")
    apply_element = job_element.find("a", class_="card-footer-item", string = "Apply")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(apply_element.get('href'))
    print()
