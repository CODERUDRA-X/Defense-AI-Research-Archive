import urllib.request
import xml.etree.ElementTree as ET
import datetime

# Guaranteed query to hit results (Artificial Intelligence)
url = 'http://export.arxiv.org/api/query?search_query=all:artificial+intelligence&sortBy=submittedDate&sortOrder=desc&max_results=1'

try:
    # Fetch and decode the data
    response = urllib.request.urlopen(url).read().decode('utf-8')
    root = ET.fromstring(response)

    # ArXiv XML namespace strict parsing
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    entry = root.find('atom:entry', ns)

    if entry is not None:
        title = entry.find('atom:title', ns).text.replace('\n', ' ').strip()
        link = entry.find('atom:id', ns).text.strip()
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Force write to README
        with open('README.md', 'a', encoding='utf-8') as f:
            f.write(f"\n\n### 🛡️ Defense & AI Log: {date_str}\n* **Title:** {title}\n* **Link:** [Read Full Paper]({link})\n")
        
        print("SUCCESS: Paper aggressively added to README!")
    else:
        print("ERROR: API returned data, but no paper entry was found.")

except Exception as e:
    print(f"CRITICAL ERROR: {e}")
