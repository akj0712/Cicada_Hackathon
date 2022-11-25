import virustotal_python
from pprint import pprint
from base64 import urlsafe_b64encode

url = 'https://techcommunity.microsoft.com/t5/excel/excel-data-uploaded-to-virus-total-and-results-returned/m-p/793659'

with virustotal_python.Virustotal("0142620545336231b49ce757e2962e57fe16f91268475ff16b906fda10cd431f") as vtotal:
    try:
        resp = vtotal.request("urls", data={"url": url}, method="POST")
        # Safe encode URL in base64 format
        # https://developers.virustotal.com/reference/url
        url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
        report = vtotal.request(f"urls/{url_id}")
        # pprint(report.object_type)
        
        val= report.data['attributes'].get('last_analysis_results')
        pprint(val)
        # pprint(report.data)
        tlist=[]
        fav=0
        ud=0
        for data in val:
            tlist.append(val[data]['category'])
            if val[data]['category']=='harmless':
                fav+=1
            if val[data]['category']=='undetected':
                ud+=1
        # print(len(tlist))
        # print(ud)
        total= len(tlist)

        fav_per= ((fav*1.0)/(total-ud))*100.0
        print(fav_per)



    except virustotal_python.VirustotalError as err:
        print(f"Failed to send URL: {url} for analysis and get the report: {err}")