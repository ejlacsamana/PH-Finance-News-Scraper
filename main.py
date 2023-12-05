from requests_html import HTMLSession
import csv
import pandas as pd

session = HTMLSession()

url = 'https://business.inquirer.net/category/latest-stories'
news_list = []

for i in range(2, 5):
    r = session.get(url)
    articles = r.html.find('#ch-ls-head')

    for item in articles:
        news_item = item.find('h2', first=True)
        news_date = item.find('#ch-postdate', first=True)
        result = news_date.text.split('BY:\xa0 ')
        news_article = {
        'title': news_item.text,
        'link': news_item.absolute_links,
        'date': result[0]
        }
        news_list.append(news_article)
    url = f'https://business.inquirer.net/category/latest-stories/page/{i}'

data = [
    ['Headline', 'Link', 'Date Published']
]

for i in news_list:
    title = i['title']
    link = i['link'].pop()
    date_published = i['date']
    new_entry = [title, link, date_published]
    data.append(new_entry)

filename = r'D:\Documents\Finance News.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

df = pd.read_csv(filename, encoding='ISO-8859-1')
for i, row in df.iterrows():
    link = row[1]
    r = session.get(link)
    scraped_content = r.html.find('p')
    first_element = scraped_content[1]
    news_content = first_element.text
    print(news_content)
    r.close()
    print(len(scraped_content))
    # Loop on the scraped content
    # Append to list each line
    # If statements link if blank or unnecessary sentence
