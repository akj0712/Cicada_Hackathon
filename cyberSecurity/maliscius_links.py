import virustotal_python
from pprint import pprint
from base64 import urlsafe_b64encode
import json

with open('all_links.json') as f:
  data = json.load(f)

links=[]
for url in data:
    with virustotal_python.Virustotal("0142620545336231b49ce757e2962e57fe16f91268475ff16b906fda10cd431f") as vtotal:
        try:
            resp = vtotal.request("urls", data={"url": url}, method="POST")
            url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
            report = vtotal.request(f"urls/{url_id}")
            val1= report.data['attributes']['last_analysis_stats']['malicious']
            if val1>0:
                links.append(url)
        except virustotal_python.VirustotalError as err:
            print(f"Failed to send URL: {url} for analysis and get the report: {err}")

# url = ["facebook.com","http://jamogames.com/templates/JLHk/"]
with open("maliscius_links.json", "w") as outfile:
            json.dump(links, outfile)
# print(links)