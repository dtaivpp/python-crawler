
def reduce_page(updated_page, db_page):
  new_page = {}

  if hasattr(db_page, 'visisted'):
    if db_page['visited']:
      pass
