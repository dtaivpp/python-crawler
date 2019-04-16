
def reduce_page(updated_page, db_page):
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
  db_page['links_to_page'] += updated_page['links_to_page']
  db_page['metadata']['links_to_page'] += updated_page['metadata']['links_to_page']
  return db_page


def _visited_page(updated_page, db_page):
  # Instead of updating the db entry with all the updates we will 
  # update the updated page with info from the db_page
  updated_page['links_to_page'] = db_page['links_to_page'] 
  updated_page['metadata']['links_to_page'] = db_page['metadata']['links_to_page']
  return updated_page