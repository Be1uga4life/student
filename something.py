import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('table', class_="tableList js-dataTooltip")
so = s.find_all('a', class_="authorName")

authorname=[]
for soh in so:
    pentis = soh.get_text()
    authorname.append(pentis.strip())


so = s.find_all('a', class_="bookTitle")
# print(so)
titles=[]
for soh in so:
    pentis = soh.get_text()
    titles.append(pentis.strip())
# content = so.find_all('span')

reee = s.find_all('span', class_="greyText smallText uitext")
digits_as_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ratings=[]
for oun in reee:
    pentis = oun.get_text()
    # print(pentis)
    if pentis[2] in digits_as_strings:
        ratings.append(float(pentis[2:6].strip()))
    elif pentis[17] in digits_as_strings:
        ratings.append(float(pentis[17:21].strip()))

for i in range(len(ratings)):
    emoji = ""
    if ratings[i] >= 4:
        emoji += '❤'
    elif ratings[i] >= 3:
        emoji += '👍'
    else:
        emoji += '👎'
    print(titles[i], "by: ", authorname[i], "with a rating of: ", ratings[i], emoji)
