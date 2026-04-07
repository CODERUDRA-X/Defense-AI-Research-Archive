import urllib.request
import datetime
import random
import re

# 1. TIMING & DATA
now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")
day_of_year = now.timetuple().tm_yday

# 2. THE 20 SACRED PROTOCOLS
gita_protocols = [
    {
        "hook": "Focus on the Logic, not the Green Box.",
        "verse": "Karma-any-evadhika-raste ma phaleshu kadachana...",
        "interpretation": "You have a right to perform your prescribed duties (Logic), but you are not entitled to the fruits (Green Squares) of your actions. Let not the reward of the streak be your motive."
    },
    {
        "hook": "One-Pointed Intelligence (The Focus).",
        "verse": "Vyavasayatmika buddhir ekeha kuru-nandana...",
        "interpretation": "Concentrate on one complex architecture at a time. A fragmented mind creates buggy code; a unified mind builds the future. Multitasking is a fragmentation of power."
    },
    {
        "hook": "Precision is the Ultimate Yoga.",
        "verse": "Yoga karmasu kaushalam...",
        "interpretation": "Excellence in your logic is a spiritual practice. In Defense-AI, precision is the divine difference between a mission's success and a system's failure."
    },
    {
        "hook": "Action in Inaction: The Stealth Bot.",
        "verse": "Karmanyakarma yah pashyed akarmani cha karma yah...",
        "interpretation": "Seeing action in inaction—like a bot working silently while the developer rests. True intelligence is efficient, invisible, and persistent."
    },
    {
        "hook": "Uplift your System by your Own Effort.",
        "verse": "Uddhared atmanatmanam natmanam avasadayet...",
        "interpretation": "You are your own Root Access. Elevate your status through your own hard-coded will. Never let your inner system crash due to external doubt."
    },
    {
        "hook": "Knowledge is the Supreme Weapon.",
        "verse": "Nahi jnanena sadrisham pavitram iha vidyate...",
        "interpretation": "Verily, there is nothing as pure as knowledge. Master the underlying architecture to master the machine. AI is the tool, but your intellect is the Master Key."
    },
    {
        "hook": "Be Steady Amidst the Runtime Errors.",
        "verse": "Siddhy-asiddhyoh samo bhutva samatvam yoga uchyate...",
        "interpretation": "Stay equanimous in success (compilation) and failure (bugs). Balance is the true system status. A steady pulse builds stable systems."
    },
    {
        "hook": "The Mind is like a Restless Bug.",
        "verse": "Chanchalam hi manah krishna pramathi balavad dridham...",
        "interpretation": "The mind is turbulent and strong like an unoptimized loop. But through constant practice (debugging) and detachment, it can be tamed and redirected."
    },
    {
        "hook": "Follow your Svadharma (Your Own Path).",
        "verse": "Sreyan sva-dharmo vigunah para-dharmat svanusthitat...",
        "interpretation": "Build your own Defense-AI path, even if imperfect, rather than following a perfect path that isn't yours. Authenticity is the best encryption."
    },
    {
        "hook": "The Fire of Knowledge Burns Errors.",
        "verse": "Jnanagnih sarva-karmani bhasma-sat kurute tatha...",
        "interpretation": "The fire of true understanding burns all past misconceptions and coding errors into ashes. Learn the 'Why' and the 'How' will fix itself."
    },
    {
        "hook": "Clarity is the Best IDE.",
        "verse": "Tatra tam buddhi-samyogam labhate paurva-dehikam...",
        "interpretation": "When clarity of thought is achieved, the logic flows without the need for external tools. Your mind is the most powerful processor ever built."
    },
    {
        "hook": "Endure the Heat of the Deadline.",
        "verse": "Matra-sparshas tu kaunteya shitosna-sukha-duhkha-dah...",
        "interpretation": "Deadlines and bugs are like seasons; they come and go. Endure them with a steady pulse and unwavering focus on the deployment."
    },
    {
        "hook": "Seeing the Unified Swarm in All.",
        "verse": "Vidya-vinaya-sampanne brahmane gavi hastini...",
        "interpretation": "A master sees the same underlying logic in a single line of code and a massive neural network. Everything is connected through the source code of reality."
    },
    {
        "hook": "The Lotus Leaf Logic (Pure Execution).",
        "verse": "Brahmany adhaya karmani sangam tyaktva karoti yah...",
        "interpretation": "Work without attachment, like water on a lotus leaf. Let bugs touch your code, but never let them touch your spirit or your determination."
    },
    {
        "hook": "Steady Engagement leads to Victory.",
        "verse": "Yatra yogeshwarah krishno yatra partho dhanur-dharah...",
        "interpretation": "Where there is Vision (Wisdom) and Execution (The Bow), victory and innovation are certain. Combine your data science with action."
    },
    {
        "hook": "The Silence of Deep Work.",
        "verse": "Maunam chaivasti guhyanam jnanam jnanavatam aham...",
        "interpretation": "Silence is the secret of deep architecture. In the quietest mind, the most complex and elegant logic is compiled and born."
    },
    {
        "hook": "Determination of the S-Rank Builder.",
        "verse": "Dhritua yaya dharayate manah-pranendriya-kriyah...",
        "interpretation": "Through unwavering determination, control the mind, the life-force, and the keyboard towards one singular goal: The Mission."
    },
    {
        "hook": "Every Project has its own Smoke (Bugs).",
        "verse": "Saha-jam karma kaunteya sa-dosam api na tyajet...",
        "interpretation": "Every undertaking is clouded by defects, as fire is by smoke. Accept the bugs as part of the process, but never stop the development."
    },
    {
        "hook": "Master the Self, Master the Environment.",
        "verse": "Jitamanah prashantashya paramatma samahitah...",
        "interpretation": "For one who has conquered the mind, the heat of the deadline and the cold of failure are exactly the same. You remain the Master of the Mainframe."
    },
    {
        "hook": "Sacrifice of Knowledge (Open Source).",
        "verse": "Sreyan dravya-mayaj jnanat jnana-yajnah parantapa...",
        "interpretation": "The sacrifice of sharing knowledge (Open Source/Community) is higher than mere accumulation of private code. To teach is to master."
    }
]

protocol_index = day_of_year % len(gita_protocols)
p = gita_protocols[protocol_index]

# 3. GENERATE THE CLEAN GOLDEN SCROLL SVG
svg_code = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="400" rx="10" fill="#0d1117"/>
  <rect x="10" y="10" width="780" height="380" rx="8" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="6 6"/>
  <text x="50%" y="70" text-anchor="middle" fill="#D4AF37" font-family="Georgia, serif" font-size="28" font-weight="bold" letter-spacing="3">THE DHARMA OF ACTION</text>
  
  <text x="50%" y="140" text-anchor="middle" fill="#F5F5DC" font-family="Georgia, serif" font-size="22" font-style="italic">"{p['verse']}"</text>
  
  <line x1="250" y1="190" x2="550" y2="190" stroke="#D4AF37" stroke-width="0.5"/>
  
  <text x="50%" y="240" text-anchor="middle" fill="#D4AF37" font-family="Verdana, sans-serif" font-size="16" font-weight="bold" letter-spacing="1">PROTOCOL {protocol_index+1:02d} // {p['hook'].upper()}</text>
  
  <foreignObject x="80" y="270" width="640" height="100">
    <div xmlns="http://www.w3.org/1999/xhtml" style="color: #C0C0C0; font-family: Georgia, serif; font-size: 18px; text-align: center; line-height: 1.5; text-shadow: 1px 1px 2px #000;">
      {p['interpretation']}
    </div>
  </foreignObject>
  
  <text x="50%" y="370" text-anchor="middle" fill="#D4AF37" font-size="24">❈</text>
</svg>"""

with open('gita_verse.svg', 'w', encoding='utf-8') as f:
    f.write(svg_code)

# 4. ARXIV RESEARCH LOGIC
fallback_facts = ["Autonomous navigation relies on sensor fusion.", "YOLOv11 is peak edge detection.", "Swarm logic is decentralized."]
try:
    url = 'http://export.arxiv.org/api/query?search_query=all:drone+AND+all:ai&max_results=1&sortBy=submittedDate&sortOrder=descending'
    response = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
    if "<entry>" in response:
        t_start = response.find('<title>') + 7
        t_end = response.find('</title>')
        title = response[t_start:t_end].replace('\n', ' ').strip()
        l_start = response.find('<id>') + 4
        l_end = response.find('</id>')
        link = response[l_start:l_end].strip()
        log_entry = f"\n* **[Research]** {title} - [Access Paper]({link})\n"
    else: raise Exception()
except:
    log_entry = f"\n* **[Defense-AI Fact]** {random.choice(fallback_facts)} (API Offline)\n"

# 5. UPDATE README.MD (FIXED MARKERS)
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# YE HAIN ASLI MARKERS
start_marker = "< ! - - GITA_START - - >"
end_marker = "< ! - - GITA_END - - >"

gita_readme_block = f"""{start_marker}
<div align="center">
  <img src="gita_verse.svg" width="100%" alt="Sacred Protocol" />
</div>
{end_marker}"""

# Accurate Regex to find and replace only between markers
pattern = re.compile(rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)

if pattern.search(content):
    content = re.sub(pattern, gita_readme_block, content)
else:
    # If markers not found, add to top
    content = gita_readme_block + "\n\n" + content

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content + f"### Log: {date_str}{log_entry}")
