import urllib.request
import datetime
import random

# YAHAN CHANGE KIYA HAI: Added %H:%M:%S for unique commits
date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Fallback intelligence if the API fails
fallback_facts = [
    "Swarm drones use decentralized logic to coordinate without a central leader.",
    "YOLOv8 is highly effective for real-time threat detection in edge devices.",
    "Autonomous navigation relies heavily on sensor fusion (LiDAR + Radar + Vision)."
]

try:
    url = 'http://export.arxiv.org/api/query?search_query=all:drone&max_results=1'
    response = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
    
    if "<entry>" in response:
        # Extract title and link securely
        t_start = response.find('<title>') + 7
        t_end = response.find('</title>')
        title = response[t_start:t_end].replace('\n', ' ').strip()
        
        l_start = response.find('<id>') + 4
        l_end = response.find('</id>')
        link = response[l_start:l_end].strip()
        
        log_entry = f"\n* **[Research]** {title} - [Link]({link})\n"
    else:
        raise Exception("API empty")
        
except Exception:
    # Plan B: Inject custom fact to ensure green commit
    fact = random.choice(fallback_facts)
    log_entry = f"\n* **[Defense-AI Fact]** {fact}\n"

with open('README.md', 'a', encoding='utf-8') as f:
    f.write(f"### Log: {date_str}{log_entry}")
