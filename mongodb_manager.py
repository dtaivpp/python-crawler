import pymongo
from reduce_pages import reduce_pages

class Database:
  def __init__(self, base_url):
    # Database name and client
    self.db_name = "Regent" #base_url

    self.client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create / Grab Database name
    self.db = self.client[self.db_name]
    
    # Create / Grab Collections
    self.pages_collection = self.db["pages"]

  def insert_links(self, url_array):
    """Inserts a list of pages. 
    Parameter
     in Array of pages
    """
    for link in url_array:
      self.insert_page(link)


  def insert_page(self, updated_page):
    """Takes in a single page to be inserted"""
    if self.pages_collection.count_documents( { "_id": updated_page['url'] } ) > 0:
        # If the link exists update its data 

        page_tmp = reduce_pages(
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

  def get_links(self,num_records):
    """
    Returns the number of records requested that have not been visited.
    
    Parameters:
      Number of records to return
    """
    cursor = self.pages_collection.find({"page.visited": False, "page.valid": True}, limit=num_records)
    return cursor

  def has_more_links(self):
    num_documents = self.pages_collection.count_documents({"page.visited": False, "page.valid": True})
    if num_documents > 0:
      return True
    else:
      return False

  def update_bad_link(url):
    self.pages_collection.update_one({"_id":url}, {"$set": {"page.visited": True, "page.valid": False}})