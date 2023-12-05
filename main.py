from requests_html import HTMLSession
import openpyxl
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

data = []

for i in news_list:
    title = i['title']
    link = i['link'].pop()
    date_published = i['date']
    new_entry = [title, link, date_published]
    data.append(new_entry)

filename = r'D:\Documents\Finance News.xlsx'

df = pd.DataFrame(data, columns=['Headline', 'Link', 'Date Published'])
df.to_excel(filename, index=False)


df = pd.read_excel(filename)
for i, row in df.iterrows():
    link = row[1]
    r = session.get(link)
    scraped_content = r.html.find('p')
    first_element = scraped_content[1]
    news_content = first_element.text
    r.close()
    article_content = []
    for element in scraped_content:
        text = element.text
        if 'Subscribe to our daily newsletter' in text or 'By providing an email address. I agree to the Terms of Use and acknowledge that I have read the Privacy Policy.' in text or 'Subscribe to our business news' in text or 'We use cookies to ensure you get the best experience on our website.' in text or 'READ: ' in text or '/File photo' in text or text == '':
            pass
        else:
            article_content.append(text)
    merged_content = '\n'.join(article_content)
    df.at[i, 'Content'] = merged_content

df.to_excel(filename, index=False)