
def reduce_pages(updated_page, db_page):
  """Takes in an updated_page and a database_page
  and returns a merged one"""
  # If the new page is visited then we need to update the visited info 
  if hasattr(updated_page, 'visited'):
    # Use Change to Visited State
    return _visited_page(updated_page, db_page)
  else: 
    # Update state
    return _update_page(updated_page, db_page)


def _update_page(updated_page, db_page):
  """Takes in an updated page and a database page to make an update
  Returns a db formatted page"""
  if hasattr(updated_page, 'links_to_page'):
    db_page['page']['links_to_page'] += updated_page['links_to_page']
  
  if hasattr(db_page['page']['metadata'], 'links_to_page'):
    db_page['page']['metadata']['links_to_page'] += updated_page['metadata']['links_to_page']
  elif (hasattr(updated_page['metadata'], 'links_to_page')):
    db_page['page']['metadata']['links_to_page'] = updated_page['metadata']['links_to_page']

  return db_page


def _visited_page(updated_page, db_page):
  """Takes in an updated page and a database page to change it to visited
  Returns a db formatted page"""
  # Instead of updating the db entry with all the updates we will 
  # update the updated page with info from the db_page
  updated_page['links_to_page'] = db_page['page']['links_to_page'] 
  updated_page['metadata']['links_to_page'] = db_page['page']['metadata']['links_to_page']
  return {"_id":updated_page['url'],"page":updated_page}