
page = {
    "url": {
        "visited": True, # Not Required, Values T/F
        "valid": True, # Not Required, Values T/F
        "links_on_page": ["url's"], # Required
        "links_to_page": ["url from"],
        "metadata": {
            "url": 'url', # This page's url Required
            "internal_links": 0,# Num Required 
            "external_links": 0, # Num Required
            "telephone_nums": 0, # Num Required
            "links_to_page": 0, # Num Required
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
}