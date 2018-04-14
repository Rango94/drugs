import requests
from lxml import etree
import time
import codecs
import random
urls=[]
for i in range(3175):
    urls.append("http://data.qgyyzs.net/list.aspx?ClassID=gcyp&terms=cpleibie&key=%D6%D0%D2%A9&p="+str(i+1)+"&isint=0")
headers = {'User-Agent': 'alexkh'}
fo=codecs.open("Drugs_c.txt","w","utf-8")
headers=[]
# header = {'Cookie' : 'rpln_guide=1; TIEBA_USERTYPE=26aac53c8dd34f8265bc3afb; bdshare_firstime=1454400287585; BIDUPSID=445BDAE5291A8082504B28A8B222428F; BAIDUID=9898ADD03EE8046FCEF6715C7507BCA9FG=1; PSTM=1456401045; TIEBAUID=69f9537ad7e26c90dcfeb337; BDUSS=khLY1k5ajNtUDRJRHBLc0VDbkJ1Nm8yfmlGOS01bFJ4VUI0bkFSUGNHbEltMzlYQVFBQUFBJCQAAAAAAAAAAAEAAABLl9EpSDk5MjEwOTg5OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgOWFdIDlhXW; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1447_19860_17001_11506_20592_20848_20856_20836_20771_20781; LONGID=701601611; wise_device=0',
#                   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
#                   'Accept-Language' : 'zh-CN,zh;q=0.8',
#                   'Connection' : 'keep-alive',
#                   'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#                   'Upgrade-Insecure-Requests' : '1',
#                   }
# headers.append(header)
# header = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
#                   }
# headers.append(header)
# header={'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
#            'Connection': 'Keep-Alive',
#     "User-Agent":"user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1"
#         }
# headers.append(header)
# header={
# 'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.15"
#         }
#
# headers.append(header)
# header={
# 'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#     "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.370.0 Safari/533.4"
#         }
# headers.append(header)
#
# header={
# 'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#     "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.1 Safari/532.9"
#         }
# headers.append(header)
#
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 "}
headers.append(header)
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 "}
headers.append(header)
header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"}
headers.append(header)
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}
headers.append(header)
header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7"}
headers.append(header)
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"}
headers.append(header)
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
headers.append(header)
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"}
headers.append(header)

for i in urls:
    fo=codecs.open("Drugs_c.txt","a","utf-8")
    try:
        page=requests.get(i,headers=headers[random.randint(0,len(headers))],timeout=20).text
        print(i)
    except:
        print("wrong")
        urls.append(i)
        continue
    html=etree.HTML(page)
    for i in html.xpath("//td[1]/div/a/text()"):
        fo.write(i+"\t")
    fo.write("\n")
    time.sleep(0.5)
    fo.close()


