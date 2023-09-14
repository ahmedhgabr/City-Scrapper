import requests
from bs4 import BeautifulSoup
import csv


input = input("Enter the city (eg. Berlin/Bonn/..) : ")

page = requests.get(f"https://rentola.de/en/for-rent?location={input}")
final_data = []

def main(page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    properties = soup.find_all("div", "caption text-center")
    
    for property in properties:
        find_property_data(property)

def find_property_data(property):
    data = property.find_all("div", "prop-value")
    bathroom = data[0].text.strip()
    bedroom = data[1].text.strip()
    type = data[2].text.strip()
   
    price = property.parent.find("b").text
    final_data.append( {"Type": type,"Price": price , "Bedroom": bedroom, "Bathrooms": bathroom})


main(page)


open_file = open(f"{input}.csv", "w")
csv_writer = csv.writer(open_file)
csv_writer.writerow(["Type", "Price", "Bedrooms", "Bathrooms"])
for data in final_data:
    csv_writer.writerow([data["Type"], data["Price"], data["Bedroom"], data["Bathrooms"]])
open_file.close()
