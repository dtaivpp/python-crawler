# Python Crawler

The intent of this project is to experiment with a web crawler that visist a page, collects all the links, and then creates some metadata about the url. 

# Process 
The crawler starts in crawler.py where it is fed a base url. From the base url it will collect all the url's on the page and create entries for each of them in a links table. Then it will start to iterate over the linkes (only links with the same base url would be visited to limit the scope of this project). Th