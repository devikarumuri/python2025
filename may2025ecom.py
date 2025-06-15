import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/tyy/4io/~cs-xj7gdemumj/pr?sid=tyy,4io&collection-tab-name=Redmi+Note+12+Pro+5G&param=6765363&otracker=clp_banner_1_13.bannerX3.BANNER_mobile-phones-big-saving-days-jan23-56hj-store_FMM4NVEBNJK7&fm=neo%2Fmerchandising&iid=M_75a6c7e3-723f-4a0b-89f7-0f66d112fff6_13.FMM4NVEBNJK7&ppt=hp&ppn=homepage&ssid=2bmt249nlc0000001678801426964")

#print(response)

soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_='KzDlHZ')
#print(names)
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
#print(name)

prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
#print(prices)
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
#print(price)
ratings=soup.find_all('div',class_='XQDdHH')
#print(ratings)
rate=[]
for i in ratings[0:10]:
    d=i.get_text()
    rate.append(float(d))
#print(rate)

images=soup.find_all('img',class_='DByuf4')
#print(images)
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
#print(image)

df=pd.DataFrame()
#print(df)

df['Names']=name
df['Prices']=price
df['Ratings']=rate
df['Images']=image
#print(df)
df.to_csv('Mobilesdatamay2025.csv')




