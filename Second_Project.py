# Install required packages
!pip install pandas
!pip install requests
!pip install bs4
!pip install plotly
import requests
import pandas as pd
from bs4 import BeautifulSoup

# we must use the request library to downlaod the webpage, and extract the text. We will extract Reliance stock data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text

!pip install html5lib
# Next we must parse the text into html using beautiful_soup
soup = BeautifulSoup(data, 'html5lib')

# Now we can turn the html table into a pandas dataframe
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    
    # We can now print out the dataframe
netflix_data.head(10)

# We can also use the pandas read_html function using the url
read_html_pandas_data = pd.read_html(url)

# Or we can convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup))

# Beacause there is only one table on the page, we just take the first table in the list returned
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()

# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html. Save the text of the response as a variable named html_data.

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data = requests.get(url).text

# Parse the html data using beautiful_soup.
beautiful_soup = BeautifulSoup(html_data, "html5lib")

# Question 1 What is the content of the title attribute:
beautiful_soup.find("title")

# Using beautiful soup extract the table with historical share prices and store it into a dataframe named amazon_data. The dataframe should have columns Date, Open, High, Low, Close, Adj Close, and Volume. Fill in each variable with the correct data from the list col
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    
#     Print out the first five rows of the amazon_data dataframe you created.

amazon_data.head().

# Question 2 What is the name of the columns of the dataframe
amazon_data.keys()

# Question 3 What is the Open of the last row of the amazon_data dataframe?
amazon_data.iloc[-1][1]
