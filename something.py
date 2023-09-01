import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('table', class_="tableList js-dataTooltip")
so = s.find_all('a', class_="authorName")

authorname = []
for soh in so:
    pentis = soh.get_text()
    authorname.append(pentis.strip())

so = s.find_all('a', class_="bookTitle")
titles = []
for soh in so:
    pentis = soh.get_text()
    titles.append(pentis.strip())

reee = s.find_all('span', class_="greyText smallText uitext")
digits_as_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ratings = []
for oun in reee:
    pentis = oun.get_text()
    if pentis[2] in digits_as_strings:
        ratings.append(float(pentis[2:6].strip()))
    elif pentis[17] in digits_as_strings:
        ratings.append(float(pentis[17:21].strip()))

# Create an HTML table
html_table = "<table border='1'><tr><th>Title</th><th>Author</th><th>Rating</th><th>Emoji</th></tr>"

for i in range(len(ratings)):
    emoji = ""
    if ratings[i] >= 4:
        emoji += '❤'
    elif ratings[i] >= 3:
        emoji += '👍'
    else:
        emoji += '👎'
    
    # Add row to the table
    html_table += f"<tr><td>{titles[i]}</td><td>{authorname[i]}</td><td>{ratings[i]}</td><td>{emoji}</td></tr>"

# Close the table
html_table += "</table>"

print(html_table)

with open('novel.md', 'w', encoding='utf-8') as html_file:
    html_file.write(html_file)
