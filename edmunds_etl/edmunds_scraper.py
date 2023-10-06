"""Scrapes the edmunds used car sales for specific models."""

import functools
import re
import bs4
import csv
import datetime
from requester import Requester

config = {"make": "ford", "model": "mustang"}
fieldnames = ["VIN","year","make","model","trim","miles","offer","mpg_avg","mpg_city","mpg_highway", "driver_count", "accidents", "usage_type", "city", "state", "dist_from_car", "run_date"]

payload = {}
headers = {
    "Cookie": 'EdmundsYear="&zip=75019&dma=623:IP&city=Coppell&state=TX&lat=32.96451&lon=-96.984901"; ak_bmsc=E8A6B9608D960ED91DFF93C11D8987F7~000000000000000000000000000000~YAAQKjsvF8aZAm6KAQAASTDxbxXOyg4+PjwJN9BDhpc2J/QZLRfqTw5iA+ztHcXy35t4erI5sBq2nOloWZuF350Kja7AVlmy3bE7MkwsqHQRt0uRB3pIntjUPl0etQmTxJIaoQdGGOTvNj2cL/oXloKUQAE0JbQjgftpweb75Zx7uj9yrVNtf/Tb7X0vxQYQrWk+RJbwMUMl50vp3MFY42xOkRRvBG6MTo746P1+PkliWc2jPK/b+Pna7gZwqUgw3aTt3iyLft9FICr48YRoZG2vQpazoTzm7nlJB1LMcrfHI0YTaVPSupSzdTn5dC2ypp6besC3I58tocXSNPTRzcb9QLMCPPu3EGk+3AOEY2hyTmseQrlcbmhy2+cGHQ==; edmunds=da97a56c-761c-4483-b86e-f3c9b0ec6135; edw=471883652886893950; entry_page=new_used_car_inventory_srp; entry_url=www.edmunds.com%2Finventory%2Fsrp.html; entry_url_params=%7B%7D; location=j%3A%7B%22zipCode%22%3A%2275019%22%2C%22type%22%3A%22Standard%22%2C%22areaCode%22%3A%22940%22%2C%22timeZone%22%3A%22Central%22%2C%22gmtOffset%22%3A-6%2C%22dst%22%3A%221%22%2C%22latitude%22%3A32.96451%2C%22longitude%22%3A-96.984901%2C%22salesTax%22%3A0.0625%2C%22dma%22%3A%22623%22%2C%22dmaRank%22%3A5%2C%22stateCode%22%3A%22TX%22%2C%22city%22%3A%22Coppell%22%2C%22county%22%3A%22Dallas%22%2C%22inPilotDMA%22%3Atrue%2C%22state%22%3A%22Texas%22%2C%22ipDma%22%3A%22623%22%2C%22ipStateCode%22%3A%22TX%22%2C%22ipZipCode%22%3A%2275019%22%2C%22userIP%22%3A%2247.187.127.217%22%2C%22userSet%22%3Anull%7D; session-id=471883652886893950; usprivacy=1NNN; visitor-id=da97a56c-761c-4483-b86e-f3c9b0ec6135; content-targeting=US,TX,IRVING,623,-96.9488,32.8139,75014-75017+75038-75039+75060-75063; device-characterization=false,false; feature-flags=j%3A%7B%22speedcurve%22%3Afalse%2C%22sentry%22%3Afalse%7D',
    "Cache-Control": "no-cache",
    "User-Agent": "PostmanRuntime/7.32.3",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

base_url = "https://www.edmunds.com"
url = base_url + "/inventory/srp.html?inventorytype=used%2Ccpo&make={0}&model={0}%7C{1}".format(
    config["make"], config["model"]
)

requester_config = {"url": url,
                    "headers":headers,
                    "payload":payload}

totalCars = 0

run_date = datetime.date.today().strftime('%Y-%m-%d')

def extractYearMakeModelTrimTuple(src):
    """Takes the text src and returns a 4-tuple."""
    src = src.replace("Certified ", "")
    src_split = src.split(" ")
    year = src_split[0]
    make = src_split[1]
    model = src_split[2]
    if src_split[3:]:
        trim = functools.reduce((lambda x, y: str(x) + " " + str(y)), src_split[3:])
    else:
        trim = ""
    return (year, make, model, trim)


def create_car_id_key(src, iterator):
    """Takes src, replaces " " with "_" and appends "_[iterator], returns"""
    return src.replace(" ", "_") + "_" + str(iterator)


def get_neighbor_relative_to_title_tag(tag):
    """Used to get repeating edmunds tags with relevant information close by. Returns tag"""
    return tag.next_sibling.string


def cleanMiles(strM):
    """Cleans miles by converting to int"""
    return int(strM.replace(",", "").replace(" miles", "").replace(" mile",""))

def parseNumStringPair(strA):
    """Parses strings that comply with the regex '(No|no|[0-9]) \w+'"""
    assert(re.search('(No|no|[0-9]) \w+', strA)), "String {} does not fit regex: (No|no|[0-9]) \w+".format(strA)
    val = strA.split(" ")[0]
    if val == "No" or val == "no":
        return 0
    else:
        return int(val)

def parseHistoryString(strH):
    """Returns the tuple of number of accidents, number of owners, and use type"""
    listOfAttr = strH.split(", ")
    assert(len(listOfAttr) == 3), "historyString does not have all three attributes: {}".format(strH)
    numAccidents = parseNumStringPair(listOfAttr[0])
    numOwners = parseNumStringPair(listOfAttr[1])
    useType = listOfAttr[2]
    return (numOwners, numAccidents, useType)

def cleanOffer(offerTag):
    """Takes a tag object and returns"""
    offer_text = offerTag["aria-label"]
    assert (offer_text[0] == "$"), "var 'offer_text' must start with dollar sign. offer_text = {}".format(offer_text)
    # There is an offer visible
    val = offerTag["aria-label"].split(" ")[0]
    return int(re.sub(r"([$,])", "", val))

def getNextPage(soup):
    nextPageSuffix = soup.find(class_="pagination-btn rounded d-flex align-items-center justify-content-center text-blue-30 mx-1_5").next_sibling.next_sibling.get("href")
    assert nextPageSuffix, 'End of pages (nextPageSuffix = null)'
    return base_url + nextPageSuffix

def scrapeForCarMakeAndModel():
    csv_file = open('car_entries.csv', mode="w")
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    responseGetter = Requester(requester_config)

    getCarsOnPage(writer, responseGetter)

def getCarsOnPage(writer, responseGetter: Requester):
    global totalCars

    response = responseGetter.makePersistentRequest()

    soup = bs4.BeautifulSoup(response.content, "html.parser")
    results = soup.find_all(class_="d-flex mb-0_75 mb-md-1_5 col-12 col-md-6")
    for idx, car_result in enumerate(results):
        try:
            getCarOnPage(car_result, totalCars, writer)
        except RuntimeError as err:
            print("RuntimeError: Could not parse car_result for car_id = {0} due to {1}".format(totalCars, err))
        
        totalCars += 1
    
    try:
        nextPage = getNextPage(soup)
    except AssertionError:
        print("End of pages")
        return
    
    responseGetter.url = nextPage
    getCarsOnPage(writer, responseGetter)

def parseMPG(text):
    """Parses the text containing the MPG to return the MPG as an int"""
    """22 Combined MPG (20 City/26 Highway)"""
    mpgValues = re.findall("\d+",text)
    assert(len(mpgValues) == 3), "Expected only three integers in the given text string: found {0}\ntext: {1}".format(len(mpgValues),text)
    assert(mpgValues[1] < mpgValues[0] < mpgValues [2]), "Values are not in the combined - city - highway format: {}".format(mpgValues)
    mpgData = dict()
    mpgData = {"mpg_avg": mpgValues[0], "mpg_city": mpgValues[1], "mpg_highway": mpgValues[2]}
    return mpgData

def parseVIN(text):
    """Parses the text containing the VIN to return the VIN as an int"""
    LEN_VIN = 17
    START = text.find("VIN: ")
    PREFIX_LEN = 5 + START
    assert(re.match("VIN: [\w\d]{17}", text)), "Text does not match regex: 'VIN: [\w\d]{17}'\nText:{}".format(text)
    return text[PREFIX_LEN: PREFIX_LEN + LEN_VIN]

def getCarOnPage(rawCarSoup, car_id, writer):
    # get Year, Make, Model and Trim
    car_data = dict()
    yearMakeModelAndTrim = rawCarSoup.find("a", class_="usurp-inventory-card-vdp-link")[
        "aria-label"
    ]
    # print(yearMakeModelAndTrim)
    car_id_key = create_car_id_key(yearMakeModelAndTrim, car_id)
    year, make, model, trim = extractYearMakeModelTrimTuple(yearMakeModelAndTrim)
    car_data.update(
        {"year": year, "make": make, "model": model, "trim": trim}
    )

    # get Miles traveled
    updateWithMilesTraveled(rawCarSoup, car_data)

    # get Offer
    updateWithOffer(rawCarSoup, car_data)

    # Get # of drivers, # of crashes, type of use
    history = updateWithHistory(rawCarSoup, car_data)

    viewMore = rawCarSoup.find(class_="view-more")

    # TODO: Get Location (city), Location (state), distance from your location
    updateWithLocation(car_data, viewMore)

    # Get run date
    car_data.update({"run_date": run_date})

    # TODO: Get VIN
    xsmallClasses = viewMore.find_all(class_="xsmall mb-1")

    for tag in xsmallClasses:
        if "MPG" in tag.text:
            updateWithMPG(car_data, tag)
        if "VIN" in tag.text:
            updateWithVIN(car_data, tag)

    # TODO: Get dealership name

    # TODO: Get external color

    writer.writerow(car_data)

def updateWithVIN(car_data, tag):
    try:
        vin = parseVIN(tag.text)
        car_data.update({"VIN": vin})
    except AssertionError:
        raise RuntimeError("Failed to extract VIN from {}".format(tag.text)) from AssertionError

def updateWithMPG(car_data, tag):
    try:
        mpgData = parseMPG(tag.text)
        car_data.update(mpgData)
    except AssertionError:
        raise RuntimeError("Failed to extract mpg from {}".format(tag.text)) from AssertionError

def updateWithLocation(car_data, viewMore):
    try:
        locatedStr = viewMore.find(class_="small font-weight-bold").text
        pattern = "(Located in )[\w\s]+, " # TODO: FINISH LATER!
        assert(locatedStr.startswith("Located in ")), "The string '{0}' does not conform to the regex '{1}'".format(locatedStr, pattern)
        cityState, distFromCarStr = locatedStr.removeprefix("Located in ").split("/")
        try:
            city, state = [txt.strip() for txt in cityState.split(",")]
        except ValueError: 
            raise RuntimeError("Failed to extract car location due to city-state parse of the following: {}".format(cityState))
        distFromCar = int(distFromCarStr[0:distFromCarStr.find("miles")].replace(",", ""))
        car_data.update(
            {"city": city, "state": state, "dist_from_car": distFromCar}
        )
    except AssertionError:
        car_data.update(
            {"city": None, "state": None, "dist_from_car": None}
        )
        raise RuntimeError("Failed to extract car location from {}".format(locatedStr)) from ValueError

def updateWithHistory(rawCarSoup, car_data):
    try:
        historyIcon = rawCarSoup.find(title="Vehicle History")
        assert(historyIcon), "Expected a history attribute and found none"
        history = get_neighbor_relative_to_title_tag(historyIcon)
        numDrivers, numAccidents, usageType = parseHistoryString(history)
        car_data.update(
            {"driver_count": numDrivers, "accidents": numAccidents, "usage_type": usageType}
        )
    except ValueError:
        car_data.update(
            {"driver_count": None, "accidents": None, "usage_type": None}
        )
        raise RuntimeError("ValueError: Failed to extract car history from {}".format(history)) from ValueError
    except AssertionError:
        car_data.update(
            {"driver_count": None, "accidents": None, "usage_type": None}
        )
        raise RuntimeError("AssertionError: Failed to extract car history") from AssertionError
    return history

def updateWithOffer(rawCarSoup, car_data):
    vehicleInfoClass = rawCarSoup.find(class_="vehicle-info d-flex flex-column p-1")
    try:
        offerTag = vehicleInfoClass.find(class_="usurp-inventory-card-vdp-link")
        offerDollarAmount = cleanOffer(offerTag)
        car_data.update({"offer": offerDollarAmount})
    except AssertionError:
        car_data.update({"offer": None})
        raise RuntimeError("Failed to extract offer from {}".format(offerTag)) from AssertionError

def updateWithMilesTraveled(rawCarSoup, car_data):
    try:
        miles = get_neighbor_relative_to_title_tag(rawCarSoup.find(title="Car Mileage"))
        cleaned_miles = cleanMiles(miles)
        car_data.update({"miles": cleaned_miles})
    except ValueError:
        car_data.update({"miles": None})
        raise RuntimeError("Failed to extract miles from {}".format(miles)) from ValueError

scrapeForCarMakeAndModel()