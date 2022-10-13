# html parsing is a process of extracting data from html files
from bs4 import BeautifulSoup
import lxml
with open('sample.html') as html_file:
    contents = html_file.read()
# html.parser tells the beautiful soup that the language is html
# html.parser may not work for all html files, so we can use lxml
soup = BeautifulSoup(contents, 'html.parser')
print(soup.prettify())
print(soup.title)
# The soup object is a tree of all the tags and text in the html file
# prints the first li tag in the html file
print(soup.li.string)
# to get them all, we can use find_all()
all_list_items = soup.find_all('li')
for tag in all_list_items:
    print(tag.getText())
all_a_tags = soup.find_all('a')

for tag in all_a_tags:
    # to get an attribute value, we use .get('attribute')
    print(tag.get('href'))

# getting elements by class and id
# we can use .find_all('tag', {'class': 'class_name'})
# find_all() returns a list of all the tags that match the criteria, find() returns the first one only

ul = soup.find("ul", {"class": "list"})
print(ul)

# Selecting elements by css selectors
url = soup.select_one("ul a")
print(url)
# to get all the links, we can use .select()
urls = soup.select("ul a")
print(urls)

name = soup.select_one("#name")
print(name)


