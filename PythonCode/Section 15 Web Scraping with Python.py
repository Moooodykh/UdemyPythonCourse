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
from enum import unique
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
"""
import requests,bs4

# Syntax to pass to the .select() method
# Match Results
#
# soup.select('div')
# All elements with the <div> tag
#
# soup.select('#some_id')
# The HTML element containing the id attribute of some_id
#
# soup.select('.notice')
# All the HTML elements with the CSS class named notice
#
# soup.select('div span')
# Any elements named <span> that are within an element named <div>
#
# soup.select('div > span')
# Any elements named <span> that are directly within an element named <div>, with no other element in between
#
req = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(req.text,'lxml')
print(soup)
print('*'*100)
site_toctext = soup.select('.toctext') #choosing the class named = toctext, TOCTEXT just came from inspection of the webpage that we
# are looking for
print(site_toctext)
first_element = site_toctext[0]
print (first_element)
print (first_element.text)

#running of all elements from that class
for item in soup.select('.toctext'):
    print(item.text)
"""

# # # # # # # # # #  part 120 ( Python Web Scraping - Grabbing an Image) # # # # # # # # #

"""
import  bs4,requests,os

req = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(req.text,'lxml')
print(soup)
ul_select = soup.select('ul li')

print('*'*100)
print(ul_select)

img_elements = soup.select('img')
print(img_elements) #many pictures will be back, it is good to search for either class or ID
first_element = img_elements[0]
#each image has a SRC url
pictures = soup.select('.thumbimage')
print('*'*100)
#more than one picture
for pic in pictures:
    print(pic)
    #Check the SRC and copy it to the browser to be sure enough that picture is what we try to find

computer = pictures[0] # first element
print(computer['class'])
print(computer['src'])
print(os.getcwd())
# this soup tag is like a dictionary
image_url = 'https:'+computer['src']
image_link = requests.get(image_url)
print(image_link.content) #binary representation of the picture
f = open('computer_image.jpg',mode='wb')
f.write(image_link.content) ###########CONTENT
f.close()

"""


# # # # # # # # # #  part 121 ( Python Web Scraping - Book Examples Part One) # # # # # # # # #
# # # # # # # # # #  part 122 ( Python Web Scraping - Book Examples Part two) # # # # # # # # #
""" 
# we will deal with www.toscrape.com
### GOAL  IS TO PRINT ALL BOOKS WHICH HAS 2 STAR RATING
### I need to find the Title
### I need to find how to solve 2 star rating
import requests,bs4

req = requests.get('http://books.toscrape.com/catalogue/page-1.html')
page_nr = 1
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
requ = requests.get(base_url.format(page_nr))
soup = bs4.BeautifulSoup(requ.text,'lxml')

books = soup.select('.product_pod')
#showing that it contain 20 elements as shows in one page
print(len(books))
print(books[0])

book_tile = books[0].select('a')[1]['title']
print(book_tile)


boook = books[0].select('.star-rating.Three')
print(boook)

book_names = list()


for n in range(1,51):
    #passing the page number to the link
    req = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(req.text,'lxml')
    #choosing the book object
    books = soup.select('.product_pod')
    for book in books:
        #if the book object rated to two stars , find the title and add it to the name list
        if book.select('.star-rating.Two'):
            book_title = book.select('a')[1]['title']
            book_names.append(book_title)

print(book_names)
"""

# # # # # # # # # #  part 123 - 124 ( Python Web Scraping - Excersize Overview & solution) # # # # # # # # #
"""
import bs4
import requests

Authors_names = set()
web_url = 'http://quotes.toscrape.com/'
req = requests.get(web_url)
soup =bs4.BeautifulSoup(req.text,'lxml')
# print(soup)
qutoes = soup.select('.quote')
print(len(qutoes))

#TASK: Get the names of all the authors on the first
# Authors NAMES
for author in qutoes:
    author_name = author.select('small')[0].getText()
    ### OR
    #qutoes[0].select('.author')[0].getText()
    Authors_names.add(author_name)

print(Authors_names)

# TASK: Create a list of all the quotes on the first page.
print('*'*100)
quote_list = list()
for quote in qutoes:
    quote_text = quote.select('.text')[0].getText()
    quote_list.append(quote_text)

print(quote_list)

#TASK: Inspect the site and use Beautiful Soup to extract the top ten tags 
# from the requests text shown on the top right from the home page 
# (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are
#  also tags underneath each quote, try to find a class only present 
# in the top right tags, perhaps check the span.

print('-'*100)
tag_soup = bs4.BeautifulSoup(req.text,'lxml')
tags = tag_soup.select('.tag-item')
tags_texts = list()
for tag in tags:
    tag_text = tag.select('a')[0].getText()
    tags_texts.append(tag_text)

print(tags_texts)


#TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website.
#  Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out
#  how to check that your loop is on the last page with quotes. For debugging purposes,
#  I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, 
# but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, 
# perhaps use try/except for this, its up to you!
print('+'*100)

import bs4,requests
unique_authors = set()
counter = 1
run = True

while run:
    page_url = 'http://quotes.toscrape.com/page/{}/'
    req =requests.get(page_url.format(counter))
    soup_element = bs4.BeautifulSoup(req.text,'lxml')
    quotos = soup_element.select('.quote')
    if quotos == []:
        run = False
    else:
        counter +=1 
        for quote in quotos:
            author_name = quote.select('.author')[0].getText()
            unique_authors.add(author_name)
        
print(unique_authors)
print(len(unique_authors))


#### TEACHER SOLUTION
page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)
    
    # Obtain Request
    res = requests.get(page_url)
    
    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break
    
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
        
    # Go to Next Page
    page += 1
    
"""