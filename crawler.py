import requests
from bs4 import BeautifulSoup
import lxml
import re
#for url validation
regex_url = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

regex_tel = re.compile(
  r'^(tel:)'
)

# {
#   {key:"https://regent.edu", value: {visited: True}}
#   {key:"https://regent.edu/home", {visited: False}}
#   {key:"https://regent.edu/page1", {visited: False}}
#}


link_dict = dict()


def pagegetter(url):
  response = requests.get(url)
  return response.text

def soupify (page):
  soup = BeautifulSoup(page, 'lxml')
  links = []
  tel = []
  bad_urls =[]
  for a in soup.find_all('a', href=True):
    if re.match(regex_url, a['href']):
      links.append(a['href'])
      print(a['href'])
    elif re.match(regex_tel, a['href']):
      tel.append(a['href'])
    else:
      bad_urls.append(a['href'])

  page = {
    'links': links,
    'tel': tel,
    'bad_urls': bad_urls
  }

  return page

def linkmanager(arr_links):
  for link in arr_links:
    if link_dict.get(link) == None:
      link_dict[link] = {'visited': False}



#Returns Html page
page = pagegetter("http://regent.edu")

#Adds Page to Dictionary with visited
link_dict["http://regent.edu"] = {"visited": True}

# Go through and pull out all links
returned_links = soupify(page)

# Add all links to our dict
linkmanager(returned_links)


# Go through all the links we got from soupify line 40 and visit them and get their links
for link in returned_links:
  if link_dict[link]['visited'] == False:
    page = pagegetter(link)
    link_dict[link] = {'visited': True}
    returned_links = soupify(page)   
    linkmanager(returned_links) 
    print('Done') 

