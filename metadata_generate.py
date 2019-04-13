from urllib.parse import urlparse
import re

def metadata_generate(page):
  metadata = {
    "url": page['url'],
    "internal_links": 0,
    "external_links": 0, 
    "telephone_nums": len(page['tel']),
  }
  
  metadata['url_components'] = url_components(page['url'])
  
  # Iterate over links
  for link in page['links']:
    # Link meta breaks out all of the url components 
    link_meta = url_components(link)

    if link_meta['netloc_min'] == metadata['url_components']['netloc_min']:
      metadata['internal_links'] += 1
    else: 
      metadata['external_links'] += 1
      
  return metadata

def url_components(url):
  components = urlparse(url)
  url_components = {
    "scheme": components[0],
    "netloc": components[1],
    "path": components[2],
    "params": components[3],
    "query": components[4],
    "fragment": components[5]
  }

  # Netloc min is the base url without www. or a port number
  url_components['netloc_min'] = re.sub("^www.|:.*$", "", url_components['netloc'])
  return url_components
