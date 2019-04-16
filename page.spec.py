
db_page = {
  "_id": "url",
  "page": {},
}

page_visited = {
    "url": 'url', # This page's url Required
    "visited": True,  # Values T/F, Updated On Visited
    "valid": True,    # Values T/F, Updated On Visited
    "links_on_page": ["url's"],   # Updated On Visited
    "links_to_page": ["url from"],# Not Updated on Visited
    "tel_on_page": ["telephone numbers"], # Updated on Visited
    "metadata": {
        "internal_links": 0, # Num Required, Updated On Visited 
        "external_links": 0, # Num Required, Updated On Visited
        "telephone_nums": 0, # Num Required, Updated On Visited
        "links_to_page": 0,  # Num Required, Updated On Visited
        "url_components": {   
            "scheme": "http/s",
            "netloc": "www.regent.edu:80",
            "netloc_min": "regent.edu",
            "path": "/home",
            "params": "params",
            "query": "query",
            "fragment": "fragment",
        }
    }
}

page_meta_min = {
  "url": 'url', # This page's url Required
  "links_to_page": ["url from"], # Updated Every Update Cycle
  "visited": False, # 
    "metadata": {
        "links_to_page": 0, # Num Required Updated Every Update Cycle
        "url_components": {   
          "scheme": "http/s",
          "netloc": "www.regent.edu:80",
          "netloc_min": "regent.edu",
          "path": "/home",
          "params": "params",
          "query": "query",
          "fragment": "fragment"
        }
    }
}

