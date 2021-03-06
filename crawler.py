import requests
from bs4 import BeautifulSoup
import lxml
import re
from metadata_generate import metadata_generate
from mongodb_manager import Database

#for url validation
regex_url = re.compile(
        r'^(?:http|ftp)s?://|' # http:// or https://...        r'^(?://)' # ...or a netloc
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

regex_tel = re.compile(
  r'^(tel:)'
)

def pagegetter(url):
  """
  Takes in url and returns HTML page. 
  
  Parameters:
    URL as string
  """
  try:
    response = requests.get(url)
  except:
    return None
  finally:
      return response.text

def soupify (page, url):
  """
  Returns all the links in <a> tags from a page 

  Parameters: 
    HTML page formatted as string
    Url that 
  """
  soup = BeautifulSoup(page, 'lxml')
  links = []
  tel = []
  for a in soup.find_all('a', href=True):

    if re.match(regex_url, a['href']):
      links.append({"url":a['href'], "valid":True})

    
    elif re.match(regex_tel, a['href']):
      tel.append(a['href'])
    
    else:
      links.append({"url":a['href'], "valid":False})

  page = {
    'url': url,
    'links_on_page': links,
    'tel_on_page': tel
  }

  page = metadata_generate(page)

  return page


def program_loop(main_url):
  """
  Runs through and grabs each link from a page.
  Then updates a database with those links and iterates
    through them visiting each one
  
  Parameters
    Main_Url which is the starting url
  """
  PageDB = Database(main_url)
  # Put Base page into array
  link = {"page":{"url":main_url}}
  
  page = pagegetter(link['page']['url'])
  returned_page = soupify(page, link['page']['url'])
  PageDB.insert_links(returned_page['links_on_page'])
  PageDB.insert_page(returned_page)
  links = PageDB.get_links(100)

  while(PageDB.has_more_links()):
    for link in links:
      page = pagegetter(link['page']['url'])
      if page != None:
        returned_page = soupify(page, link['page']['url'])
        PageDB.insert_links(returned_page['links_on_page'])
        PageDB.insert_page(returned_page)
      else:
        PageDB.update_bad_link(link['page']['url'])

    links = PageDB.get_links(100)
  
  
if __name__ == "__main__":
  program_loop("https://regent.edu")
  print("Done")