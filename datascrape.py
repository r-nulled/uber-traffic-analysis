from bs4 import BeautifulSoup as BS
from selenium import webdriver
from functools import reduce
from datetime import date, timedelta
from dateutil import parser, rrule
import pandas as pd
import time

#this function loads the content of wunderground
def render_page(url):
    #you must download chrome webdriver and upload its path onto here
    driver = webdriver.Chrome('/Users/deanlong/Desktop/chromedriver')
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r


# function uploads content of webpage onto list and separates list's contents
def scraper(page, dates):
    output = pd.DataFrame()

    for d in dates:
        url = str(str(page) + str(d))
        r = render_page(url)

        soup = BS(r, "html.parser")
        container = soup.find('lib-city-history-observation')
        check = container.find('tbody')

        data = []

        for c in check.find_all('tr', class_='ng-star-inserted'):
            for i in c.find_all('td', class_='ng-star-inserted'):
                trial = i.text
                trial = trial.strip('  ')
                data.append(trial)

        i = 0
        length = len(data)
        timelist = []
        templist = []
        humidlist = []
        windlist = []
        while i < length:
            timelist.append(data[i])
            templist.append(data[i+1])
            humidlist.append(data[i+3])
            windlist.append(data[i+5])
            i += 10

        Temperature = pd.DataFrame(templist,columns= ['Temperature'])
        Time = pd.DataFrame(timelist,columns = ['Time'])
        Humidity = pd.DataFrame(humidlist,columns=['Humidity'])
        WindSpeed = pd.DataFrame(windlist,columns=['WindSpeed'])

        dfs = [Temperature, Time, Humidity, WindSpeed, ]

        df_final = reduce(lambda left, right: pd.merge(left, right, left_index=True, right_index=True), dfs)

        df_final['Date'] = str(d)

        output = output.append(df_final)

        output = output[['Date', 'Time', 'Temperature','Humidity','WindSpeed']]

    return output


start_date = "2019-04-01"
end_date = "2020-02-29"
start = parser.parse(start_date)
end = parser.parse(end_date)
dates = list(rrule.rrule(rrule.DAILY, dtstart=start, until=end))

page = 'https://www.wunderground.com/history/daily/us/ny/new-york-city/KLGA/date/'

df = scraper(page, dates)
df.to_csv("data/output.csv")