import urllib.request
import xml.etree.ElementTree as ET
import datetime

# Fetch latest paper on Defense AI / Drone Swarms
url = 'http://export.arxiv.org/api/query?search_query=all:drone+AND+all:AI&sortBy=submittedDate&sortOrder=desc&max_results=1'
response = urllib.request.urlopen(url).read()
root = ET.fromstring(response)

# Parse and format data
namespace = {'atom': 'http://www.w3.org/2005/Atom'}
entry = root.find('atom:entry', namespace)
title = entry.find('atom:title', namespace).text.replace('\n', ' ')
link = entry.find('atom:id', namespace).text

# Append to daily log
date_str = datetime.datetime.now().strftime("%Y-%m-%d")
with open('README.md', 'a') as f:
    f.write(f"\n### {date_str}\n* **{title}**\n* [Read Paper]({link})\n")
