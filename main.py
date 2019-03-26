#############################################
#
#    Shell stories
#     by Josh Belmar
#      1/12/2019
# 
# ###########################################

#NOTES:  1) Add more artwork and have it randomly choose
#        2) Consider adding a feature to save authors, and to give prefrence to them while loading random quotes
#           - This would look like adding blocks[rnd].text to an array(100 of them ?), then searching the names from the save file and give prefrence to them in the 
#           - random choice if present.

from bs4 import *
import subprocess, re, datetime, requests, random
from art import ship,tree,book

def get_quotes():
    rnd = random.randrange(len(blocks)-1)
    for q in blocks:
        if re.search('Click to tweet', q.text):
            cleaned_quotes.append(q.text[:-15])
        cleaned_quotes.append(q.text)
    return cleaned_quotes[rnd]
  

def banner():
    subprocess.call('clear')
    art = ['book()', 'tree()', 'ship()']
    #art = ["south_park()"]
    choice = art[random.randint(0,len(art)-1)]
    #choice = array[random.randint(0,len(array))]
    exec(choice)
        
# Initalize storage
quotes_categories = ['Quote of the Day','Love Quote of the Day','Art Quote of the Day','Nature Quote of the Day','Funny Quote of the Day']
random_quotes_url = "http://wisdomquotes.com/inspirational-quotes/"
urls = ["http://wisdomquotes.com/inspirational-quotes/"]
quotes = []
cleaned_quotes = []
#liked_authors = []
#Request site
site_data = requests.get(random_quotes_url)
content = site_data.content

#Soup initialization
soup = BeautifulSoup(content, 'html.parser')

#Grab all blockquote tags 
blocks = soup.find_all('blockquote')

#Prints Banner
banner()

# Random quote
quote = get_quotes()
print(quote)
