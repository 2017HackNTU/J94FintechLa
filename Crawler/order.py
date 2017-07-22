# encoding: utf-8
import urllib
from urllib.request import urlopen

# url = "http://24h.pchome.com.tw/?m=shopcar&f=modifyShopCar&BUY_TYPE=BIGCAR"

# from_data = {
#     "G":[{"TI":"DGAD68-A90081P4E-000"}, {"TI":"DGAD68-A90084ZNI-000"}, {"TI":"DGAD68-A90084ZOL-000"}, {"TI":"DGAD68-A90085KT9-000"}], 
#     "A":"", 
#     "B":"", 
#     "TB":"24H", 
#     "TP":2, 
#     "T":"ADD", 
#     "TI":"DGAD7P-A9007UFW1-000", 
#     "RS":"DGAD7P", 
#     "YTQ":1
# }
try: 
    url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
    headers = {};
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0';

    form_data = {
        "StartStation": "977abb69-413a-4ccf-a109-0272c24fd490", 
        "EndStation": "f2519629-5973-4d08-913b-479cce78a356",
        "SearchDate": "2016/01/10",
        "SearchTime": "17:00",
        "SearchWay":"DepartureInMandarin",
        "RestTime":"",
        "EarlyOrLater":""
    }
    form_data = urllib.parse.urlencode(form_data)
    form_data = form_data.encode('ascii')

    req = urllib.request.Request(url, data=form_data, headers=headers)
    with urllib.request.urlopen(req) as response:
        responseData = str(response.read().decode('utf-8'))
    saveFile = open('withHeaders.txt','w', encoding='utf8');
    saveFile.write(responseData);
    saveFile.close();
except Exception as e:
    print(str(e));