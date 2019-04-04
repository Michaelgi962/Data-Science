import requests # For website connections
from urllib import request # For website connections
from bs4 import BeautifulSoup # For HTML parsing
from contextlib import closing

#Search for the Job Title: Data Scientist
#Search for the Location: Indiana
url = "https://www.monster.com/jobs/search/?q=Data-Scientist&where=IN"
def jobPostingURL(url):
	'''

	This function returns the url of each job listing for a job search on the monster website

	input:
		->a url from monster for a search of a Job Title and Location
	output:
		-> a list containing:
			-> the url to a job posting
			-> the title of a job posting
	'''
	url += state




#Access the website
response = requests.get(url)
print(response) #Response 200 means the get request was a success
#requests.text returns the full html file from the url

soup = BeautifulSoup(response.text,"html.parser")
#BeautifulSoup reformats the html output from response.text

print(soup.body.h2)

#Check if a job url on the search page matches the url at a destination
##example_monster_URL_1
href_1="https://job-openings.monster.com/senior-data-scientist-remote-fort-wayne-in-us-cybercoders/206651308"

##Actual_URL
Actual_URL_1 = "https://job-openings.monster.com/senior-data-scientist-remote-fort-wayne-in-us-cybercoders/206651308"

print("Actual_URL_1 is real_url: ", href_1 == Actual_URL_1)

