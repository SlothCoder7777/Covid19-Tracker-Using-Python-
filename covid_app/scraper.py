import requests
from bs4 import BeautifulSoup

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", id="main_table_countries_today")
    rows = table.tbody.find_all("tr")

    data = []
    for row in rows[:50]:
        cols = row.find_all("td")
        if cols and len(cols) > 6:
            country = cols[1].text.strip()
            total_cases = cols[2].text.strip().replace(",", "")
            total_deaths = cols[4].text.strip().replace(",", "")
            total_recovered = cols[6].text.strip().replace(",", "")
            data.append({
                "country": country,
                "cases": int(total_cases) if total_cases.isdigit() else 0,
                "deaths": int(total_deaths) if total_deaths.isdigit() else 0,
                "recovered": int(total_recovered) if total_recovered.isdigit() else 0
            })
    return data
