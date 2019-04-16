import pymongo
from reduce_pages import reduce_page

class MongoDB:
  def __init__(self, base_url):
    # Database name and client
    self.db_name = base_url

    self.client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create / Grab Database name
    self.db = self.client[self.db_name]
    
    # Create / Grab Collections
    self.pages_collection = self.db["pages"]

  def insert_links(self, url_array):
 
    for link in url_array:
      self.insert_page(link)


  def insert_page(self, updated_page):
    if self.pages_collection.count_documents( { "_id": updated_page['url'] } ) > 0:
        # If the link exists update its data 

        page_tmp = reduce_page(
          updated_page,
          self.pages_collection.find_one( { "_id": updated_page['url'] } )
        )

        # Replace old page entry in datbase
        self.pages_collection.replace_one(
          {"_id": updated_page['url']},
          page_tmp
        )

    else:
        # If the page doesnt 
        updated_page['visited'] = False
        page_tmp = {"_id": updated_page['url'],
                    "page": updated_page}

        # Insert document
        self.pages_collection.insert_one(page_tmp)

  def return_records(self,num_records):
    cursor = self.pages_collection.find({"visited": False}, limit=num_records)
    return cursor
