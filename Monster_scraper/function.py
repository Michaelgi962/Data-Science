# Get the text data from the first job posting
import requests # For website connections
from bs4 import BeautifulSoup # For HTML parsing
import time

url = "https://www.monster.com/jobs/search/?q=Data-Scientist&where=IN"

#Access the website
response = requests.get(url)
##print(response)  #Response 200 means the get request was a success

#Store the html code in a Beautiful Soup object
soup = BeautifulSoup(response.text,"html.parser")

#Access the first URL containing HTML object called 'a'
##print(soup.a)
#Access the first URL with the
##print(soup.a.get('href'))

#Access every URL with the find_all function
##print(soup.find_all('a'))

#Access every URL within the list of returned urls from findall
for link in soup.find_all('a'):
    print(link.get('href'))

#Find a way to identify the urls for job postings
##first job post url   https://job-openings.monster.com/senior-data-scientist-remote-fort-wayne-in-us-cybercoders/206651308

##second job post url   https://job-openings.monster.com/special-agent-indianapolis-in-us-federal-bureau-of-investigation/fa3446b9-ab92-413e-951c-abd2d5f41b01

## a job opening always begins with 'https://job-openings.monster.com'