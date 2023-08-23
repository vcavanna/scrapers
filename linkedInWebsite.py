import requests
import bs4

page = open("associateDataEngineer.html")
bs = bs4.BeautifulSoup(page, "html.parser")

job_list = bs.find_all(class_="flex-grow-1 artdeco-entity-lockup__content ember-view")
for job in job_list:
    title_and_link = job.find("a")
    title = title_and_link.get("aria-label")
    link = title_and_link.get("href")
    metadata = job.find_all("li", class_="job-card-container__metadata-item")
    print(title)
    print(link)
    [print(data.text.strip()) for data in metadata]
    print()