from bs4 import BeautifulSoup
import requests
import pandas as pd

"""
Tutorial I am using: Alex The Analyst Web Scraping Videos
Website I am scraping: https://www.scrapethissite.com/pages/forms/
"""

# saving url as var to make it neater
url = 'https://www.scrapethissite.com/pages/forms/'

"""
requests.get() is a HTTP GET request to the url passed in and returns the response from the server
Useful attributes and methods:
.text --> response content as a string
.status_code --> HTTP status code of response (ex. 200 is good, 404 is bad)
"""
page = requests.get(url)

# BeautifulSoup(response from request as text, form that text is in/appropriate parser)
# soup is now a BeautifulSoup instance, allows us to parse through data
soup = BeautifulSoup(page.text, 'html.parser')

# .find_all returns a list of all occurences of 'div'
all_divs = soup.find_all('div')


# I will attempt to grab the first row of information and append into a dataframe

# Obtain column names for dataframe using column names from table on website
column_names = soup.find('tr')
column_titles = soup.find_all('th')
final_titles = []
for column in column_titles:
    final_titles.append(column.text.strip())

# Create dataframe with column names
df = pd.DataFrame(columns=final_titles)

# Grab first row of data
first_row = soup.find_all('tr')[1]
row_data = first_row.find_all('td')
insert_this = []

# Append data to dataframe
for data in row_data:
    insert_this.append(data.text.strip())

df.loc[0] = insert_this
print(df)

# Export as .csv file
df.to_csv('/Users/sophiayau/Desktop/istryingoutwebscraping/first_row_data.csv', index = False)




