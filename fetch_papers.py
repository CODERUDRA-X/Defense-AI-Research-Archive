import urllib.request
import xml.etree.ElementTree as ET
import datetime

# Cleaned up API query for ArXiv
url = 'http://export.arxiv.org/api/query?search_query=all:drone+AI&sortBy=submittedDate&sortOrder=desc&max_results=1'

try:
    response = urllib.request.urlopen(url).read()
    root = ET.fromstring(response)

    namespace = {'atom': 'http://www.w3.org/2005/Atom'}
    
    # Check if we got any entries back
    entry = root.find('atom:entry', namespace)
    
    if entry is not None:
        title = entry.find('atom:title', namespace).text.replace('\n', ' ')
        link = entry.find('atom:id', namespace).text

        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        with open('README.md', 'a') as f:
            f.write(f"\n### {date_str}\n* **{title}**\n* [Read Paper]({link})\n")
        print(f"Successfully added paper: {title}")
    else:
        print("No papers found in the response.")

except Exception as e:
    print(f"An error occurred: {e}")
