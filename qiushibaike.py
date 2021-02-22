import requests
from lxml import etree

base_url = "https://www.qiushibaike.com/text/page/{}"
page = input("please print page num:")
headers = {
    'User-Agent': 'Mozilla/5.0'
}
res = requests.get(base_url.format(page),headers)
html = res.text
#print(html)

con = etree.HTML(html)
print(con.xpath("//div[contains(@class,'article block')]//span/text()"))
