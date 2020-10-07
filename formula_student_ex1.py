# importing the libraries
from bs4 import BeautifulSoup
import csv
import requests

url="https://www.formulastudent.de/academy/20200829-waymo/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

gdp_table = soup.find("table", attrs={"class": "overview"})
gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows

inf = []
inf.append(["team_name","category","country","city","university"])

for data2 in gdp_table_data:
	td = data2.find_all("td")
	a = td[0].text.replace('\n', '').strip()
	b = td[5].text.replace('\n', '').strip()
	c = td[3].text.replace('\n', '').strip()
	d = td[2].text.replace('\n', '').strip()
	e = td[1].text.replace('\n', '').strip()
	inf.append([a,b,c,d,e])
with open('teams.csv', 'w', encoding="utf-16", newline='') as file:
	writer = csv.writer(file, delimiter='\t')
	writer.writerows(inf)
