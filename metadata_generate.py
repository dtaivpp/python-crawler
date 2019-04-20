from urllib.parse import urlparse
import re

def metadata_generate(page):
  """
  Generate the metadata object for a visited page

  Parameters: 
    Page object with 'url' property
  """
  # Create basic metadata structure
  metadata = {
    "internal_links": 0,
    "external_links": 0, 
    "telephone_nums": len(page['tel_on_page']),
    "url_components": _url_components(page['url'])
  }
  
  # Iterate over links updating their data/metadata
  for link in page['links_on_page']:
    link['links_to_page'] = []
    link['metadata'] = {}
    # Link creates url_compontents attribute of link 
    if link["valid"]:
      link['metadata']['url_components'] = _url_components(link['url'])

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
  """
  Generate a small metadata object (for link only)

  Parameters:
    Just a url
  """
  return _url_components(url)

def _url_components(url):
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

