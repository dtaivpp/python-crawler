import pymongo

class MongoDB:
  def __init__(self, base_url):
    # Database name and client
    self.db_name = base_url

    self.client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create / Grab Database name
    self.db = self.client[self.db_name]
    
    # Create / Grab Collections
    self.pages_collection = self.db["pages"]

  def imsert_links(self, url_array):

    for link in url_array:
      # Check if the link is in the collection
      if self.pages_collection.count_documents({"_id": link['url']  }) > 0:
        # If the link exists update its data 
        


      else: 
        # Otherwise create an entry and update its links from 


        