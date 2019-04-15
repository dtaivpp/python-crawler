from urllib.parse import urlparse
import re

def metadata_generate(page):
  # Create basic metadata structure
  metadata = {
    "url": page['url'],
    "internal_links": 0,
    "external_links": 0, 
    "telephone_nums": len(page['tel']),
    "url_components": url_components(page['url'])
  }
  
  # Iterate over links updating their data/metadata
  for link in page['links_on_page']:
    # Link creates url_compontents attribute of link 
    link['metadata']['url_components'] = url_components(link['url'])

    # If the link belongs to the primary page
    if link['metadata']['url_components']['netloc_min'] == metadata['url_components']['netloc_min']:
      metadata['internal_links'] += 1
      link['internal'] = True
    else: 
      metadata['external_links'] += 1
      link['interal'] = False
    
    link['metadata']['links_to_page'] = 1
    link['links_to_page'] = [ page['url'] ]

  page['metadata'] = metadata

  return page

def metadata_generate_short (url):
  return url_components(url)

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
