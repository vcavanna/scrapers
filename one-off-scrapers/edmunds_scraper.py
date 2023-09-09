"""Scrapes the edmunds used car sales for specific models."""

import requests
import bs4
import functools
import re


def extractYearMakeModelTrimTuple(src):
    """Takes the text src and returns a 4-tuple."""
    src = src.replace("Certified ", "")
    src_split = src.split(" ")
    year = src_split[0]
    make = src_split[1]
    model = src_split[2]
    trim = functools.reduce((lambda x, y: str(x) + " " + str(y)), src_split[3:])
    return (year, make, model, trim)


def create_car_id_key(src, iterator):
    """Takes src, replaces " " with "_" and appends "_[iterator], returns"""
    return src.replace(" ", "_") + "_" + str(iterator)


def get_neighbor_relative_to_title_tag(tag):
    """Used to get repeating edmunds tags with relevant information close by. Returns tag"""
    return tag.next_sibling.string


def cleanMiles(strM):
    """Cleans miles by converting to int"""
    return int(strM.replace(",", "").replace(" miles", ""))


def cleanOffer(offerTag):
    """Takes a tag object and returns"""
    offer_text = offerTag["aria-label"]
    print(offer_text)
    assert (offer_text[0] == "$"), "var 'offer_text' must start with dollar sign. offer_text = {}".format(offer_text)
    # There is an offer visible
    val = offerTag["aria-label"].split(" ")[0]
    return (int(re.sub(r"([$,])", "", val)), True)

config = {"make": "toyota", "model": "corolla"}

url = "https://www.edmunds.com/inventory/srp.html?inventorytype=used%2Ccpo&make={0}&model={0}%7C{1}".format(
    config["make"], config["model"]
)

payload = {}
headers = {
    "Cookie": 'EdmundsYear="&zip=75019&dma=623:IP&city=Coppell&state=TX&lat=32.96451&lon=-96.984901"; ak_bmsc=E8A6B9608D960ED91DFF93C11D8987F7~000000000000000000000000000000~YAAQKjsvF8aZAm6KAQAASTDxbxXOyg4+PjwJN9BDhpc2J/QZLRfqTw5iA+ztHcXy35t4erI5sBq2nOloWZuF350Kja7AVlmy3bE7MkwsqHQRt0uRB3pIntjUPl0etQmTxJIaoQdGGOTvNj2cL/oXloKUQAE0JbQjgftpweb75Zx7uj9yrVNtf/Tb7X0vxQYQrWk+RJbwMUMl50vp3MFY42xOkRRvBG6MTo746P1+PkliWc2jPK/b+Pna7gZwqUgw3aTt3iyLft9FICr48YRoZG2vQpazoTzm7nlJB1LMcrfHI0YTaVPSupSzdTn5dC2ypp6besC3I58tocXSNPTRzcb9QLMCPPu3EGk+3AOEY2hyTmseQrlcbmhy2+cGHQ==; edmunds=da97a56c-761c-4483-b86e-f3c9b0ec6135; edw=471883652886893950; entry_page=new_used_car_inventory_srp; entry_url=www.edmunds.com%2Finventory%2Fsrp.html; entry_url_params=%7B%7D; location=j%3A%7B%22zipCode%22%3A%2275019%22%2C%22type%22%3A%22Standard%22%2C%22areaCode%22%3A%22940%22%2C%22timeZone%22%3A%22Central%22%2C%22gmtOffset%22%3A-6%2C%22dst%22%3A%221%22%2C%22latitude%22%3A32.96451%2C%22longitude%22%3A-96.984901%2C%22salesTax%22%3A0.0625%2C%22dma%22%3A%22623%22%2C%22dmaRank%22%3A5%2C%22stateCode%22%3A%22TX%22%2C%22city%22%3A%22Coppell%22%2C%22county%22%3A%22Dallas%22%2C%22inPilotDMA%22%3Atrue%2C%22state%22%3A%22Texas%22%2C%22ipDma%22%3A%22623%22%2C%22ipStateCode%22%3A%22TX%22%2C%22ipZipCode%22%3A%2275019%22%2C%22userIP%22%3A%2247.187.127.217%22%2C%22userSet%22%3Anull%7D; session-id=471883652886893950; usprivacy=1NNN; visitor-id=da97a56c-761c-4483-b86e-f3c9b0ec6135; content-targeting=US,TX,IRVING,623,-96.9488,32.8139,75014-75017+75038-75039+75060-75063; device-characterization=false,false; feature-flags=j%3A%7B%22speedcurve%22%3Afalse%2C%22sentry%22%3Afalse%7D',
    "Cache-Control": "no-cache",
    "User-Agent": "PostmanRuntime/7.32.3",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

response = requests.request("GET", url, headers=headers, data=payload, timeout=5)

soup = bs4.BeautifulSoup(response.content, "html.parser")
results = soup.find_all(class_="d-flex mb-0_75 mb-md-1_5 col-12 col-md-6")

car_data = dict()

for idx, car_result in enumerate(results):
    # get Year, Make, Model and Trim
    yearMakeModelAndTrim = car_result.find("a", class_="usurp-inventory-card-vdp-link")[
        "aria-label"
    ]
    car_id_key = create_car_id_key(yearMakeModelAndTrim, idx)
    year, make, model, trim = extractYearMakeModelTrimTuple(yearMakeModelAndTrim)
    car_data.update({car_id_key: dict()})
    car_data[car_id_key].update(
        {"year": year, "make": make, "model": model, "trim": trim}
    )

    # get Miles traveled
    miles = get_neighbor_relative_to_title_tag(car_result.find(title="Car Mileage"))
    cleaned_miles = cleanMiles(miles)
    car_data[car_id_key].update({"miles": cleaned_miles})

    vehicleInfoClass = car_result.find(class_="vehicle-info d-flex flex-column p-1")

    # get Offer traveled
    offerTag = vehicleInfoClass.find(class_="usurp-inventory-card-vdp-link")
    offerDollarAmount = cleanOffer(offerTag)
    car_data[car_id_key].update({"offer": offerDollarAmount})

    print(
        "year: {}, trim: {}, miles: {}, offer: {}".format(
            year, trim, cleaned_miles, offerDollarAmount
        )
    )

    # TODO: Get # of drivers

    # TODO: Get Location (city)

    # TODO: Get Location (state)


# print(car_data)
# print(results)

# print(response.text)
