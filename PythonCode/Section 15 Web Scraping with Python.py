# ------------------------ Section 15: Section 15 Web Scraping with Python is from part 116 to 124   -----------------------------

# # # # # # # # # #  part 116 ( Introduction to Web Scraping) # # # # # # # # #

"""

#HTML AND CSS concepts
# Scraping Guidelines
# Keep in mind you should always have permission for the website you are scraping!
# Check a websites terms and conditions for more info.
# Also keep in mind that a computer can send requests to a website very fast,
# so a website may block your computer's ip address if you send too many requests too quickly.
# Lastly, websites change all the time! You will most likely need to
# update your code often for long term web-scraping jobs.

"""

# # # # # # # # # #  part 117 ( Setting Up Web Scraping Libraries) # # # # # # # # #

"""
# important rules to follow and understand

#1. Always be respectful and try to get premission to scrape, do not bombard a website with scraping requests,
#  otherwise your IP address may be blocked!
#2. Be aware that websites change often, meaning your code could go from working to totally broken
#  from one day to the next.
#3. Pretty much every web scraping project of interest is a unique and custom job, so try your best to
# generalize the skills learned here.

#WE need to install these libraries to work with Webscraping
# pip install requests
# pip install lxml
# pip install bs4

"""

# # # # # # # # # #  part 118 ( Python Web Scraping - Grabbing a Title) # # # # # # # # #

"""
#############Example Task 0 - Grabbing the title of a page
import requests
req = requests.get('http://www.example.com')
print(type(req))
print(req.text)# showing the content of the req object (all tags) (TEXT WILL SHOW THE GIANT TEXT FROM THAT OBJECT)


#LXML is running in the backend of the BEAUTIFUL SOUP because it can recognze the HTML tags,CSS tag...etc
import bs4
soup = bs4.BeautifulSoup(req.text,'lxml')
print(soup) # NOW we have the elements as it shows in the browser and we need to select ITEMS we needed

site_title = soup.select('title')# notice that the result here is a list because it can contain more than one object

site_p =soup.select('p')
print(site_title) # one hit
print(site_p) #multiple hits
print(site_title[0]) # first element
print(site_title[0].getText()) # the text of the first element
print(site_p[0].getText())
print(type(site_p[0]))

"""
# # # # # # # # # #  part 119 ( Python Web Scraping - Grabbing a Class) # # # # # # # # #


# # # # # # # # # #  part 120 ( Advanced Python Objects Assessment Test) # # # # # # # # #
# # # # # # # # # #  part 121 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
# # # # # # # # # #  part 122 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
# # # # # # # # # #  part 123 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
# # # # # # # # # #  part 124 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
