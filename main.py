import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.gov.uk/government/collections/export-from-africa-to-the-uk'
htmldata = requests.get(url)
htmldata=htmldata.content
soup = BeautifulSoup(htmldata, 'html.parser')

div = soup.find_all('div', class_='responsive-bottom-margin')
div = div[1]
print(div)
li=[]
for row in div.find_all('h3',class_='group-title'):
    li.append(row.text)

an = div.find_all_next('a')
li0=[an[1].text]
li1=[i.text for i in an[2:6:+1]]
li2=[i.text for i in an[6:12:+1]]
li3=[i.text for i in an[12:14:+1]]
l=[li0,li1,li2,li3]
dic={}
for i in range(len(li)):
    dic.update({li[i] : l[i]})

df=pd.DataFrame({ key:pd.Series(value) for key, value in dic.items() })

df.to_csv('data.csv',index=False)
